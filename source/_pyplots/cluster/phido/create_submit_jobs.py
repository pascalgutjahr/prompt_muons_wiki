# coding: utf-8

import os
import subprocess
import time


job_template = """#!/bin/sh
### this job is
#BS -N {}
### send mail to
#PBS -M givenname.surname@tu-dortmund.de
### send mail on (a)bortion, (b)egin, (e)nd; default is: (a)bortion
#PBS -m abe
### OR: send (n)o mail
### PBS -m n
### logfiles:
#PBS -o /home/$USER/jobs/logs/{}.log
#PBS -e /home/$USER/jobs/errors/{}.log
### use these resources
###  Wall time of 24 hour
#PBS -l walltime={}
###  1 node with 1 core (maximum: 8 cores per node)
#PBS -l nodes=1:ppn=1
###  30000 MB of memory
#PBS -l vmem={}mb
### pass environment variables
#PBS -V"""

job_dir = '/home/$USER/jobs/'
input_dir = '/fhgfs/users/$USER/IceCube/2013/sim/{}/L3/i3files'
command = '/fhgfs/users/$USER/Software/V04-11-02/build/env-shell.sh python\
 /home/$USER/scripts/weighting.py -i "{}" -o {} -n {} -d {} -f {}'

# job attributes
job = 'l3_weighting_new_id'
duration = "03:59:59"
vmem = "2000"
max_files = 100
# command specific options
data_sets = ['12550', '14550', '16550']
n_files = [300, 750, 60]
n_files = dict(zip(data_sets, n_files))
flux = 'honda2014_spl_solmin'

CORSIKA = False  # process multiple CORSIKA files to one output
pos = 3  # position of the run name when splitted
sep = '.'  # separator for splitting the run name

if CORSIKA:
    command += ' -c'


def output_format(file_name):
    file_name = file_name.replace('i3files', 'h5files_new_id')
    return file_name[:file_name.find('.i3')]

submitted = []
failed = []

# create job directory 
if not os.path.isdir(job_dir + job):
    os.makedirs(job_dir + job)

# create qsub files and submit jobs for all given files
for dataset in data_sets:
    if CORSIKA:
        '''
        Get max run number and create globable input file names representing
        the given number of files to process at once into one file
        '''
        files = os.listdir(input_dir.format(dataset))
        run_split = files[-1].split(sep)
        run_string = run_split[pos]

        to_process = []
        for run in range(0, int(run_string)):
            # get multiples of max_files of the run number
            if run % max_files == 0 and run >= max_files:
                # fill up decimal positions with markers for glob
                # while also filling up the values before the marker with 0's
                run_name = str(run).replace('0', '?').zfill(len(run_string))
                to_process.append(run_name)

        # include the files below the max_files marker
        to_process.append(to_process[0].replace('1','0'))

        file_names = [sep.join(run_split[:pos] + [run_name] + \
                      run_split[pos+1:]) for run_name in to_process]
    else:
        file_names = os.listdir(input_dir.format(dataset))
     
    # create qsub files
    for i, file_name in enumerate(file_names):
        job_name = job + '_' + dataset + '_' + str(i)
        input_file = os.path.join(input_dir.format(dataset), file_name)
        qsub_file = job + '/' + dataset + '_' + str(i) + ".qsub"
        with open(qsub_file, 'w') as file:
            output_file = output_format(input_file)
            if CORSIKA:
                output_file = output_file.replace('?', '0')
            file.write(job_template.format(job_name,
                                           job_name,
                                           job_name,
                                           duration,
                                           vmem))
            file.write("\n")
            file.write("\n")
            file.write(command.format(input_file,
                                      output_file,
                                      n_files[dataset],
                                      dataset,
                                      flux))
            file.close()

            # submit process
            if subprocess.check_output(['qsub',qsub_file]) == 0:
                failed.append(file_name)
                pass
            else:
                submitted.append(file_name)
                time.sleep(2)

if len(submitted) != 0:
    print('Successfully submitted jobs for the files:')
    print(submitted)
if len(failed) != 0:
    print('Failed submits for the files:')
    print(failed)
