Technical Review
################

This section includes instructions to reproduce the results of the analysis.


.. _load_software:
Load software 
+++++++++++++

Login to the IceCube cluster. You can login to cobalts to create jobs files. Single jobs can be run on cobalts, but if you want to run multiple jobs, you should login to NPX (condor). These instructions load the software to run my analysis. If you would like to install the software on your own, there are instructions below.

.. code-block:: bash 

    # load cvmfs python 
    eval $(/cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/setup.sh)

    # load icetray
    /cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/RHEL_7_x86_64/metaprojects/icetray/v1.10.0/env-shell.sh

    # load python environment
    source /data/user/pgutjahr/software/virtual_envs/tensorflow_gpu_py3-v4.3.0/bin/activate


Simulation 
++++++++++

The simulation is officially done via the IceProd framework. If you need further information, you find the source code for IceProd `here <https://github.com/WIPACrepo/iceprod>`_. 
The datasets used in this analysis are  `22774 <https://iceprod.icecube.aq/dataset/c36ef7701a1411ef8f0100505684797b>`_, `22775 <https://iceprod.icecube.aq/dataset/e54edc3e1a1411ef9bc700505684797b>`_, `22776 <https://iceprod.icecube.aq/dataset/01d37eb41a1511ef9bc700505684797b>`_, `22777 <https://iceprod.icecube.aq/dataset/166e92b41a1511efb0bb00505684797b>`_ and `22778 <https://iceprod.icecube.aq/dataset/2f0f7dba1a1511ef8ebc00505684797b>`_. 

Reconstruction
++++++++++++++

Detailed information about the reconstructions are provided :ref:`here <CNN_reconstructions paragraph>`. That paragraph describes the fundamental ideas of the CNN based reconstruction, the features, the training data, and the evaluation. 
The networks used to reconstruct energies, direction and geometries are stored here: 

* /data/user/pgutjahr/exported_models/atmospheric_muon_leading/Old_CORSIKA/loose_precuts

and the network used to apply the pre-cut to remove low energy events at an early stage is stored here:

* /data/user/pgutjahr/exported_models/atmospheric_muon_leading/Old_CORSIKA/

To apply a network using the `ic3-processing <https://github.com/mhuen/ic3-processing>`_ framework, you can add the following dicts to your ``tray_segments`` list. At first, you have to apply the time window cleaning via: 

.. code-block:: yaml

    {
        # add cleaned muon pulses
        ModuleClass: 'ic3_processing.modules.pulses.cleaning.apply_time_window_cleaning',
        ModuleKwargs: {},
    }

Then, you get the cleaned pulses on which the networks are trained, named ``SplitInIceDSTPulsesTWCleaning6000ns``. To apply the pre-cut network, you can use the following code: 

.. code-block:: yaml 

    {
        # run dnn-reco for pre cut
        ModuleClass: 'ic3_processing.modules.reco.reco.apply_dnn_reco',
        ModuleTimer: True,
        ModuleKwargs: {
            cfg: {
                    # global settings shared for all DNN-reco modules
                    add_dnn_reco: True,
                    DNN_batch_size: 1,
                    DNN_excluded_doms: [
                        'SaturationWindows', 'BadDomsList', 'CalibrationErrata',
                    ],
                    DNN_partial_exclusion: True,

                    DNN_reco_configs: [
                    {
                        pulse_map_string: SplitInIceDSTPulsesTWCleaning6000ns,
                        DNN_model_names: [
                            'precut_surface_bundle_energy_3inputs_6ms_01',
                        ],
                        DNN_ignore_misconfigured_settings_list: [],
                        DNN_models_dir: '/data/user/pgutjahr/exported_models/atmospheric_muon_leading/Old_CORSIKA/',
                    },
                ],
            },
        },
    }

The other three networks are applied in the same way, but they are stored at a different location, as mentioned above. 

.. code-block:: yaml 

    {
        # run dnn-reco for model evaluation
        ModuleClass: 'ic3_processing.modules.reco.reco.apply_dnn_reco',
        ModuleTimer: True,
        ModuleKwargs: {
            cfg: {
                    # global settings shared for all DNN-reco modules
                    add_dnn_reco: True,
                    DNN_batch_size: 1,
                    DNN_excluded_doms: [
                        'SaturationWindows', 'BadDomsList', 'CalibrationErrata',
                    ],
                    DNN_partial_exclusion: True,

                    DNN_reco_configs: [
                    {
                        # models trained on cleaned pulses, 9 inputs
                        pulse_map_string: SplitInIceDSTPulsesTWCleaning6000ns,
                        num_data_bins: 9,
                        DNN_model_names: [
                            'direction_9inputs_6ms_medium_02_03',
                            'leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02',
                            'track_geometry_9inputs_6ms_medium_01',
                        ],
                        DNN_ignore_misconfigured_settings_list: [],
                        DNN_models_dir: '/data/user/pgutjahr/exported_models/atmospheric_muon_leading/Old_CORSIKA/loose_precuts',
                    },
                ],
            },
        },
    }

To reproduce the analysis, of course, the networks do not need to be trained again. The networks are already trained and stored in the locations mentioned above.
However, if you want to train the networks again, you have to instal the dnn_reco framework on your local machine that provides a GPU. Then, you have to create the training data on the IceCube cluster. For this, we use 
`ic3-processing <https://github.com/mhuen/ic3-processing>`_. The config files to create the training data can be found here:

* `training data configs <https://github.com/icecube/dnn_selections/tree/main/resources/configs/atmospheric_muon_leading/processing/training_data>`_ 

The pre-cut network is trained on IceCube Level2 after applying the muon filter. The other three networks are trained on our Level3, after applying a pre-cut of 200 TeV on the estimated bundle energy at surface. 
These data need to be transferred to your local machine, where you can train the networks. 

The architectures of the networks are defined in these configs:  

* `pre-cut <https://github.com/icecube/dnn_selections/blob/main/resources/configs/atmospheric_muon_leading/dnn_reco/L2/precut/precut_surface_bundle_energy_3inputs_6ms_01.yaml>`_

* `Energy <https://github.com/icecube/dnn_selections/blob/main/resources/configs/atmospheric_muon_leading/dnn_reco/L3/energy/leading_bundle_surface_leading_bundle_energy_inputs9_6ms_01.yaml>`_

* `Direction <https://github.com/icecube/dnn_selections/blob/main/resources/configs/atmospheric_muon_leading/dnn_reco/L3/direction/direction_9inputs_6ms_01.yaml>`_

* `Geometry <https://github.com/icecube/dnn_selections/blob/main/resources/configs/atmospheric_muon_leading/dnn_reco/L3/track_geometry/track_geometry_9inputs_6ms_01.yaml>`_

Process data to Level 5 
+++++++++++++++++++++++

Config locations
----------------

The processing is done with `ic3-processing <https://github.com/mhuen/ic3-processing>`_, which I can highly recommend to use. You can define all your steps, functions and modules in a single config file. This makes it easy to reproduce the analysis. The config files used to process the CORSIKA datasets, NuGen datasets and the burnsample to level 4 can be found here:

* `Level 4 config CORSIKA <https://github.com/icecube/dnn_selections/blob/main/resources/configs/atmospheric_muon_leading/processing/Evaluation/CORSIKA_v1100/level4.yaml>`_ 

* `Level 4 config NuGen <https://github.com/icecube/dnn_selections/blob/main/resources/configs/atmospheric_muon_leading/processing/Evaluation/CORSIKA_v1100/level4_NuGen.yaml>`_

* `Level 4 config burnsample <https://github.com/icecube/dnn_selections/blob/main/resources/configs/atmospheric_muon_leading/processing/Evaluation/CORSIKA_v1100/level4_exp.yaml>`_

The final cuts to process the data to Level 5 are then performed in the analysis notebooks by applying the function ``apply_quality_cuts``, which can be found `here <https://github.com/icecube/dnn_selections/blob/main/dnn_selections/selections/atmospheric_muon_leading/selection/quality_cuts.py>`_. Additionally, the configs mentioned above apply only a pre-cut of 200 TeV on the bundle energy at surface. Thus, when you load the data in a 
notebook, you also have to apply the cut ``DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01_bundle_energy_in_mctree > 5e5`` to reach Level 4 as described in this analysis. 

Config explanation
------------------

In the following, I will explain the structure of the config files using the Level 4 config file for the CORSIKA datasets as an example. The config files are structured in a way that you can easily add or remove modules. 
At first, you define the resources needed for the jobs and some dagman settings, which do not need to be adapted. For the resources, you can decide whether the job should use a GPU or not. When you don't run the job on a 
GPU, you should set ``gpus: 0`` and ``has_avx2: True`` and ``has_ssse3: True``. The networks used in this analysis are also fast on a CPU as stated in the selection section in :numref:`DNN_reconstruction_runtimes`. 
What often needs to be adjusted is the memory. 
Then, you define your input and output patterns. The input pattern is the path to the input files, which are stored on the IceCube cluster. The output pattern is the path where the output files are stored. The output files are named according to the dataset number and run number.
Here, the Level 2 production files in i3-format are loaded. 

.. code-block:: yaml 

    #------------------------------
    # General job submission config
    #------------------------------

    keep_crashed_files: False

    resources:
            # If gpus == 1 this will be run on a GPU with
            gpus: 1
            cpus: 1
            memory: 6gb # often this needs to be adjusted
            # has_avx2: True # set to true, if gpu is not used
            # has_ssse3: True # set to true, if gpu is not used

    dagman_max_jobs: 5000
    dagman_submits_interval: 500
    dagman_scan_interval: 1
    dagman_submit_delay: 0

    # If true, the input files will first be checked for corruption.
    # Note that this will take a while, since each input file has to be
    # iterated through. You generally only want to set this to true if you
    # are merging a number of input files of which some are known to be corrupt.
    exclude_corrupted_input_files: False

    #------------------------------
    # Define Datasets to process
    #------------------------------

    #------
    # common settings shared by all datasets
    #------
    i3_ending: 'i3.zst'
    n_runs_per_merge: 100
    in_file_pattern: '/data/sim/IceCube/2023/generated/CORSIKA_EHISTORY/filtered/level2/CORSIKA-in-ice/{dataset_number}/{folder_num_pre_offset_n_merged:04d}000-{folder_num_pre_offset_n_merged:04d}999/Level2_IC86.2024_corsika.{dataset_number:06d}.{run_number:04d}*.{i3_ending}'
    out_file_pattern: '{data_type}_{step}.{dataset_number:06d}.{run_number:04d}XX'
    out_dir_pattern: '{data_type}/{dataset_number}/{step}'
    folder_pattern: '{folder_num_pre_offset:04d}000-{folder_num_pre_offset:04d}999'
    folder_offset: 0
    n_jobs_per_folder: 1000

    # do not count weight frames first, assume every input file is 1 run
    n_files_is_n_runs: False

    gcd: '/cvmfs/icecube.opensciencegrid.org/data/GCD/GeoCalibDetectorStatus_2020.Run134142.Pass2_V0.i3.gz'
    #------

    datasets:

        datasets_100per_merge__10000_runs :

            cycler:
                dataset_number: [22774]

            runs_range: [0, 100] # set the number of runs to process, here 100 files are merged to one, using the key n_runs_per_merge in the global settings above
            data_type: CORSIKA

            step: 'level4'

        datasets_10per_merge__10000_runs :

            n_runs_per_merge: 10
            in_file_pattern: '/data/sim/IceCube/2023/generated/CORSIKA_EHISTORY/filtered/level2/CORSIKA-in-ice/{dataset_number}/{folder_num_pre_offset_n_merged:04d}000-{folder_num_pre_offset_n_merged:04d}999/Level2_IC86.2024_corsika.{dataset_number:06d}.{run_number:05d}*.{i3_ending}'
            out_file_pattern: '{data_type}_{step}.{dataset_number:06d}.{run_number:05d}X'

            cycler:
                dataset_number: [22776, 22777, 22778]

            runs_range: [0, 1000] # set the number of runs to process, here 10 files are merged to one, using the key n_runs_per_merge
            data_type: CORSIKA

            step: 'level4'

        datasets_10per_merge__20000_runs :

            n_runs_per_merge: 10
            in_file_pattern: '/data/sim/IceCube/2023/generated/CORSIKA_EHISTORY/filtered/level2/CORSIKA-in-ice/{dataset_number}/{folder_num_pre_offset_n_merged:04d}000-{folder_num_pre_offset_n_merged:04d}999/Level2_IC86.2024_corsika.{dataset_number:06d}.{run_number:05d}*.{i3_ending}'
            out_file_pattern: '{data_type}_{step}.{dataset_number:06d}.{run_number:05d}X'

            cycler:
                dataset_number: [22775] # set the number of runs to process, here 10 files are merged to one, using the key n_runs_per_merge

            runs_range: [0, 2000] # set the number of runs to process, here 10 files are merged to one, using the key n_runs_per_merge
            data_type: CORSIKA

            step: 'level4'

Then, general job templates and paths are defined. This doesn't need to be adjusted.

.. code-block:: yaml 

    # -------------------------------------------------------------
    # Define environment information shared across processing steps
    # -------------------------------------------------------------
    job_template: job_templates/cvmfs_python.sh
    script_name: general_i3_processing.py
    cuda_home: /data/user/mhuennefeld/software/cuda/cuda-11.8

    # add optional additions to the LD_LIBRARY_PATH
    # Note: '{ld_library_path_prepends}' is the default which does not add anything
    ld_library_path_prepends: '{ld_library_path_prepends}'

    # Defines environment variables that are set from python
    set_env_vars_from_python: {
        # 'TF_DETERMINISTIC_OPS': '1',
    }

In the next step, you can define several steps to run. Here, only one step is needed. For each step, you can load different python versions and icetray metaprojects. For example, this is necessary if a CORSIKA file was 
produced with an old software and the I3MCTree was not stored, but you would like to re-create the tree. For this, you need to run the exact same software that was used to create the CORSIKA file. Here, in step 1 you could 
re-create the I3MCTree, but in step 2 you can use the new software to process the data. In the list ``tray_segments``, you can define the actual processing steps. 

.. code-block:: yaml 

    #-----------------------------------------------
    # Define I3Traysegments for each processing step
    #-----------------------------------------------

    # a list of processing steps. Each processing step contains
    # information on the python and cvmfs environment as well as
    # a list of I3TraySegments/Modules that will be added to the I3Tray.
    # Any options defined in these nested dictionaries will supersede the
    # ones defined globally in this config.
    # Tray context can be accessed via "context-->key".
    # For nested dictionaries it's possible to do: "context-->key.key2.key3"
    # The configuration dictionary of the job can be passed via "<config>"
    # Special keys for the tray_segments:
    #       ModuleClass: str
    #           The module/segment to run.
    #       ModuleKwargs: dict
    #           The parameters for the specified module.
    #       ModuleTimer: str
    #           If provided, a timer for this module will be added.
    #           Results of all timers are saved in the frame key "Duration".
    processing_steps: [

        # -----------------
        # Processing step 1
        # -----------------
        {
            # Define environment for this processing step
            cvmfs_python: py3-v4.3.0,
            icetray_metaproject: icetray/v1.10.0,
            python_user_base_cpu: /data/user/pgutjahr/software/virtual_envs/tensorflow_gpu_py3-v4.3.0,
            python_user_base_gpu: /data/user/pgutjahr/software/virtual_envs/tensorflow_gpu_py3-v4.3.0,

            write_i3: False, # if True, i3 files are written
            write_hdf5: True, # if True, hdf5 files are written

            # define a list of tray segments to run
            tray_segments: [
                {
                    # load modules and do the actual stuff here...
                    # modules used for Level 4 are explained in detail below
                }
            ],
        },
    ]

The modules used in the tray segments are explained in detail below. The modules are loaded in the order they are defined in the list ``tray_segments``. 
The first module is the ``ic3_processing.modules.processing.filter_events.filter_streams`` module. This module is used to filter the streams of the input files. In this case, we only want to keep the ``InIceSplit`` stream.

.. code-block:: yaml 

    {
        # Only keep 'InIceSplit' stream
        ModuleClass: 'ic3_processing.modules.processing.filter_events.filter_streams',
        ModuleKwargs: {streams_to_keep: ['InIceSplit']},
    }

This module is followed by ``ic3_processing.modules.processing.filter_events.apply_l2_filter_mask``. This module is used to apply the muon filter. 

.. code-block:: yaml 

    {
        # Only keep events of the MuonFilter
        ModuleClass: 'ic3_processing.modules.processing.filter_events.apply_l2_filter_mask',
        ModuleKwargs: {filter_base_name: 'MuonFilter'},
    }

Then, ``ic3_processing.modules.processing.filter_events.I3OrphanFrameDropper`` is used to discard orphan Q-frames. This module is used to remove Q-frames that are not followed by P-frames.

.. code-block:: yaml 

    {
        # Discard orphan Q-frames
        ModuleClass: 'ic3_processing.modules.processing.filter_events.I3OrphanFrameDropper',
        ModuleKwargs: {OrphanFrameStream: 'Q'},
    }

Then, ``ic3_processing.modules.pulses.cleaning.apply_time_window_cleaning`` is used to apply the time window cleaning of 6 µs.

.. code-block:: yaml 

    {
        # add cleaned muon pulses
        ModuleClass: 'ic3_processing.modules.pulses.cleaning.apply_time_window_cleaning',
        ModuleKwargs: {},
    }

Then, ``ic3_processing.modules.reco.reco.apply_dnn_reco`` applies the DNN reconstruction as explained before.

.. code-block:: yaml

    {
        # run dnn-reco for pre cut
        ModuleClass: 'ic3_processing.modules.reco.reco.apply_dnn_reco',
        ModuleTimer: True,
        ModuleKwargs: {
            cfg: {
                    # global settings shared for all DNN-reco modules
                    add_dnn_reco: True,
                    DNN_batch_size: 1,
                    DNN_excluded_doms: [
                        'SaturationWindows', 'BadDomsList', 'CalibrationErrata',
                    ],
                    DNN_partial_exclusion: True,

                    DNN_reco_configs: [
                    {
                        pulse_map_string: SplitInIceDSTPulsesTWCleaning6000ns,
                        DNN_model_names: [
                            'precut_surface_bundle_energy_3inputs_6ms_01',
                        ],
                        DNN_ignore_misconfigured_settings_list: [],
                        DNN_models_dir: '/data/user/pgutjahr/exported_models/atmospheric_muon_leading/Old_CORSIKA/',
                    },
                ],
            },
        },
    }

The moduel ``ic3_processing.modules.processing.filter_events.filter_events`` applies cuts. Here, a pre-cut of 200 TeV on the bundle energy at surface is applied. The key is named ``bundle_energy_in_mctree``.

.. code-block:: yaml 

    {
        # apply loose pre-cut
        ModuleClass: 'ic3_processing.modules.processing.filter_events.filter_events',
        ModuleKwargs: {
            # Define a config where each entry must contain the fields
            # key, column, value, option, combination
            # filter options are greater_than, less_than, equal_to, unequal_to
            # combination options are: 'and', 'or'
            # Two masks: one for each combination type will be created
            # An event passes the filter if any of these two masks is True!
            filter_list: [
                {
                    'key': 'DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01',
                    'column': 'bundle_energy_in_mctree',
                    'value': !!float 2e5,
                    'option': 'greater_than',
                    'combination': 'and',
                },
            ],
        },
    }

After applying the pre-cut, again orphan Q-frames are discarded.

.. code-block:: yaml

    {
        # Discard orphan Q-frames
        ModuleClass: 'ic3_processing.modules.processing.filter_events.I3OrphanFrameDropper',
        ModuleKwargs: {OrphanFrameStream: 'Q'},
    }

The module ``ic3_labels.weights.segments.WeightEvents`` calculates the weights for the events. The weights are used to re-weight the events to the correct energy spectrum. The weights are calculated using the ``corsika`` and ``nugen`` files. The weights are stored in the output file. However, for the final weighting of the events we use `simweights <https://github.com/icecube/simweights>`_.

.. code-block:: yaml 

    {
        # compute weights
        ModuleClass: 'ic3_labels.weights.segments.WeightEvents',
        ModuleKwargs: {
            'infiles': context-->ic3_processing.infiles,
            'dataset_type': '{data_type}',
            'dataset_n_files': context-->ic3_processing.n_files,
            'dataset_n_events_per_run': -1,
            'dataset_number': '{dataset_number}',
            'check_n_files': ['corsika', 'nugen'],
            'add_mceq_weights': False,
            'mceq_kwargs': {
                'cache_file': '/data/ana/PointSource/DNNCascade/utils/cache/mceq.cache',
            },
        },
        ModuleTimer: True,
    }

The next module ``ic3_processing.modules.labels.primary.add_weighted_primary`` extracts the cosmic ray primary from the I3MCTree before the muon propagation and saves it as ``MCPrimary`` in the frame. This key 
is needed for the weighting.

.. code-block:: yaml 

    {
        # add weighted primary
        ModuleClass: 'ic3_processing.modules.labels.primary.add_weighted_primary',
        ModuleKwargs: {},
    }

The module ``ic3_processing.modules.labels.recreate_and_add_mmc_tracklist.RerunProposal`` runs PROPOSAL again to re-create the I3MCTree. In the simulation, the trees are not saved to reduce the disk space.   

.. code-block:: yaml 

    # -----------------
    # Recreate I3MCTree
    # -----------------
    {
        # Re-create I3MCTree
        ModuleClass: 'ic3_processing.modules.labels.recreate_and_add_mmc_tracklist.RerunProposal',
        ModuleKwargs: {
            'random_service_class': 'I3GSLRandomService',
        },
        ModuleTimer: True,
    }

The moduel ``dnn_selections.selections.atmospheric_muon_leading.ic3.labels.MCMostEnergeticMuonInside`` selects the most energetic muon of the muon bundle in the convex hull extended by 200 m and saves it as an I3Particle in the frame.

.. code-block:: yaml 

    # ----------
    # Add labels
    # ----------
    {
        # add labels: Most energetic muon in convex hull
        ModuleClass: 'dnn_selections.selections.atmospheric_muon_leading.ic3.labels.MCMostEnergeticMuonInside',
        ModuleKwargs: {
            AddPseudoMuon: True,
            ConvexHull: icecube_hull_ext_200,
            RunOnDAQFrames: True,
            OutputKey: 'MostEnergeticMuonInside',
        },
        ModuleTimer: True,
    }

The module ``dnn_selections.selections.atmospheric_muon_leading.ic3.labels.MCLabelsLeadingMuons`` adds many labels used in the analysis. For example, all information about the primary particle, the energy of the muon bundle at the entry and the surface, same for the leading muon, the entry position, the closest approach point to the center of the detector, the number of muons entering the detector, the number of coincident primaries, the stochasticity of the muon bundle and also the bundle radius. 

.. code-block:: yaml 

    {
        # add labels: MCLabelsLeadingMuons
        ModuleClass: 'dnn_selections.selections.atmospheric_muon_leading.ic3.labels.MCLabelsLeadingMuons',
        ModuleKwargs: {
            'OutputKey': 'MCLabelsLeadingMuons',
            'MostEnergeticMuonInsideKey': 'MostEnergeticMuonInside',
            'ConvexHull': icecube_hull_ext_200,
            'ComputeBundleRadius': False,
            'ComputeStochasticity': False,
            'FixMuonPairProductionBug': True,
        },
        ModuleTimer: True,
    }

The module ``dnn_selections.selections.atmospheric_muon_leading.ic3.labels.MCLabelsMostEnergeticMuonParentInfo`` adds the parent information of the most energetic muon. This is needed to tag a muon as prompt or conventional.

.. code-block:: yaml 

    {
        # add labels: MCLabelsMostEnergeticMuonParentInfo
        ModuleClass: 'dnn_selections.selections.atmospheric_muon_leading.ic3.labels.MCLabelsMostEnergeticMuonParentInfo',
        ModuleKwargs: {
            'OutputKey': 'MCLabelsMostEnergeticMuonParentInfo',
            'ConvexHull': icecube_hull_ext_200,
            'MostEnergeticMuonInsideKey': 'MostEnergeticMuonInside',
        },
        ModuleTimer: True,
    }

The module ``ic3_data.segments.CreateDNNData`` creates the training data for the DNN. For the pre-cut network only 3 input features are generated, for the other networks 9 input features are calculated. 

.. code-block:: yaml 

    ########################
    ### Check dnn input data
    ########################
    {
        # write DNN-reco training data to file [3 inputs, cleaned]
        ModuleClass: 'ic3_data.segments.CreateDNNData',
        ModuleKwargs: {
            NumDataBins: 3,
            RelativeTimeMethod: ,
            DataFormat: reduced_summary_statistics_data,
            PulseKey: SplitInIceDSTPulsesTWCleaning6000ns,
            DOMExclusions: ['SaturationWindows','BadDomsList','CalibrationErrata'],
            PartialExclusion: True,
            OutputKey: 'dnn_data_SplitInIceDSTPulsesTWCleaning6000ns',
        },
        ModuleTimer: True,
    },
    {
        # write DNN-reco training data to file [9 inputs, cleaned]
        ModuleClass: 'ic3_data.segments.CreateDNNData',
        ModuleKwargs: {
            NumDataBins: 9,
            RelativeTimeMethod: time_range,
            DataFormat: pulse_summmary_clipped,
            PulseKey: SplitInIceDSTPulsesTWCleaning6000ns,
            DOMExclusions: ['SaturationWindows','BadDomsList','CalibrationErrata'],
            PartialExclusion: True,
            OutputKey: 'dnn_data_inputs9_SplitInIceDSTPulsesTWCleaning6000ns',
        },
        ModuleTimer: True,
    }

The module ``icecube.common_variables.hit_statistics.I3HitStatisticsCalculator`` calculates some basic statistics based on the input pulses, like charge etc. These can be used for some low-level checks. However, they are not used in the analysis.

.. code-block:: yaml 

    ########################
    ### Add hit statistics
    ########################
    {
        # Add hit statistics
        ModuleClass: 'icecube.common_variables.hit_statistics.I3HitStatisticsCalculator',
        ModuleKwargs: {
            'PulseSeriesMapName': 'SplitInIceDSTPulses',
            'OutputI3HitStatisticsValuesName': HitStatistics_SplitInIceDSTPulses,
        },
    },
    {
        # Add hit statistics
        ModuleClass: 'icecube.common_variables.hit_statistics.I3HitStatisticsCalculator',
        ModuleKwargs: {
            'PulseSeriesMapName': 'SplitInIceDSTPulsesTWCleaning6000ns',
            'OutputI3HitStatisticsValuesName': HitStatistics_SplitInIceDSTPulsesTWCleaning6000ns,
        },
    }

The module ``Delete`` deletes some keys to reduce the size of the output files. This is not necessary, but it is recommended to do so.

.. code-block:: yaml 

    {
        # Delete keys to reduce space
        ModuleClass: 'Delete',
        ModuleKwargs: {Keys: [
            I3MCTree, MMCTrackList,
            I3MCTree_recreation_meta_info,
            InIceRawData, I3MCPulseSeriesMap,
            I3MCPulseSeriesMapParticleIDMap,
            I3MCPulseSeriesMapPrimaryIDMap,
        ]},
    }

After the processing is done, the output files are written. Here, you can define the file format and the streams that should be written. You also have to add the keys that should be written to the hdf5 files. 
Actually, some modules are written in a way, that they already append they produced keys to this list. For example, the DNN reconstruction modules append their keys to the list, which is why you don't find them in the list below.

.. code-block:: yaml 

    #--------------------
    # File output options
    #--------------------

    # write output as i3 files via the I3Writer
    write_i3: False
    write_i3_kwargs: {

        # only write these stream types,
        # i.e ['Q', 'P', 'I', 'S', 'M', 'm', 'W', 'X']
        'i3_streams': ['Q', 'P', 'I', 'S', 'M', 'm', 'W', 'X'],
    }

    # write output as hdf5 files via the I3HDFWriter
    write_hdf5: True
    write_hdf5_kwargs: {

        # sub event streams to write
        'SubEventStreams': ['InIceSplit'],

        # HDF keys to write (in addition to the ones in
        # tray.context['ic3_processing']['HDF_keys'])
        # Note: added tray segments should add outputs that should be written
        # to hdf5 to the tray context.
        'Keys': [

            # general
            'I3EventHeader',
            'DurationQ',
            'DurationP',

            # dnn reco input data
            'dnn_data_SplitInIceDSTPulsesTWCleaning6000ns_bin_values',
            'dnn_data_SplitInIceDSTPulsesTWCleaning6000ns_bin_indices',
            'dnn_data_SplitInIceDSTPulsesTWCleaning6000ns_global_time_offset',

            # labels
            'MCLabelsLeadingMuons',
            'MCLabelsMostEnergeticMuonParentInfo',

            # weighting
            'weights',
            'weights_meta_info',
            'MCPrimary',
            'I3MCWeightDict',
            'CorsikaWeightMap',

            # Filters
            'FilterMask',
            'QFilterMask',

            # Other
            'MostEnergeticMuonInside',

            'PolyplopiaPrimary',

            # Hit Statistics
            'HitStatistics_SplitInIceDSTPulses',
            'HitStatistics_SplitInIceDSTPulsesTWCleaning6000ns',

            # Snowstorm
            # 'SnowstormParameterRanges',
            'SnowstormParameters',
            # 'SnowstormParametrizations',
            # 'SnowstormProposalDistribution',
            'SnowstormParameterDict',
        ],
    }

Job submission
--------------

Log in to NPX (condor). Then, load the software environment as described above :ref:`here <load_software>`.
Then, you have to create the job files. This is done via ``ic3-processing``:

.. code-block:: bash 

    ic3_create_job_files <path-to-config> -d <path-to-output-directory> -p <path-to-scratch-directory> --dagman

The tag ``-h`` can be used to get a list of all options. The output directory is the directory where the output files are stored. The scratch directory is the directory where the job files are stored. When I log in to the submitter, this command could look like this to create the job files to process CORSIKA datasets to Level 4:

.. code-block:: bash 

    ic3_create_job_files /home/pgutjahr/dnn_selections/resources/configs/atmospheric_muon_leading/processing/Evaluation/CORSIKA_v1100/level4.yaml -d /data/user/pgutjahr/CORSIKA -p /scratch/pgutjahr/CORSIKA --dagman

To submit the jobs, you have to execute the bash script ``start_dagman.sh``, like this:

.. code-block:: bash 

    /scratch/pgutjahr/CORSIKA/level4_0000/start_dagman.sh 

As usual, ``condor_q`` can be used to check the status of the jobs.

However, often jobs crash due to memory issues. Some jobs require more memory than others. Sometimes a single jobs needs up to 20 GB of memory. Setting the default to 20 GB is not a good idea, because then you 
get less jobs on the cluster and the processing will take much longer, and also other users will get less jobs because memory is limited. Instead, when all your jobs are either done or crashed, you can check the log files of the jobs that crashed. For this, I run: 

.. code-block:: bash 

    grep -r Error /scratch/pgutjahr/CORSIKA/level4_0000/logs/

For example, this will indicate that jobs have requested 6 GB of memory, but actually 10 are needed. Then, you can adjust this in the ``OneJob.submit`` file and submit the jobs again. To edit the file, you can use any text editor, 
like ``vim`` or ``nano``. 

.. code-block:: bash 

    vim /scratch/pgutjahr/CORSIKA/level4_0000/OneJob.submit
    # change request_memory = 6gb to request_memory = 10gb
    # save and exit

    # submit the jobs again, like you did before
    /scratch/pgutjahr/CORSIKA/level4_0000/start_dagman.sh 

This will submit only the crashed jobs again with the new memory request. If you some jobs fail again because a few jobs need even more memory, you can repeat this process. Sometimes, the jobs don't crash, but 
they end up being hold. In this case, just kill the jobs as usual by ``condor_rm <job_id>`` or ``condor_rm <user>`` when there was only one submit. 

Now we are done with the processing. In the output directory you will find the processed hdf5 files, which can now be loaded in the analysis notebooks.

Unfolding
+++++++++

Install software 
++++++++++++++++

.. note::
    These instructions install tensorflow software 2.14 for dnn_reco framework version 2. The models trained with dnn_reco version 1 are not compatible with the dnn_reco version 2, as mentioned in the release notes `here <https://github.com/icecube/dnn_reco/releases/tag/v2.0.0>`_. Thus, to reproduce the analysis with the exact same networks, dnn_reco v1 must be installed. However, you can also load the environment installed by myself, which is located in `/data/user/pgutjahr/software/virtual_envs/tensorflow_gpu_py3-v4.3.0`, as mentioned above.  

The following instructions to install the software are for the IceCube cluster and extracted from the intructions of the `dnn_reco <https://user-web.icecube.wisc.edu/~mhuennefeld/docs/dnn_reco/html/pages/installation.html>`_ framework.

.. code-block:: bash 

    # load cvmfs python environment
    eval $(/cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/setup.sh)

    mkdir /data/user/{USER}/technical_review/virtual_envs

    cd /data/user/{USER}/technical_review/virtual_envs

    python -m virtualenv py3-v4.3.0_tensorflow2.14

    source py3-v4.3.0_tensorflow2.14/bin/activate

    # change activation script such that it prepends the path
    # to the virtual environment to the PYTHONPATH environment variable
    perl -i -0pe 's/_OLD_VIRTUAL_PATH\="\$PATH"\nPATH\="\$VIRTUAL_ENV\/bin:\$PATH"\nexport PATH/_OLD_VIRTUAL_PATH\="\$PATH"\nPATH\="\$VIRTUAL_ENV\/bin:\$PATH"\nexport PATH\n\n# prepend virtual env path to PYTHONPATH if set\nif ! \[ -z "\$\{PYTHONPATH+_\}" \] ; then\n    _OLD_VIRTUAL_PYTHONPATH\="\$PYTHONPATH"\n    export PYTHONPATH\=\$VIRTUAL_ENV\/lib\/python3.7\/site-packages:\$PYTHONPATH\nfi/' py3-v4.3.0_tensorflow2.14/bin/activate

    perl -i -0pe 's/        export PYTHONHOME\n        unset _OLD_VIRTUAL_PYTHONHOME\n    fi/        export PYTHONHOME\n        unset _OLD_VIRTUAL_PYTHONHOME\n    fi\n\n    if ! \[ -z "\$\{_OLD_VIRTUAL_PYTHONPATH+_\}" \] ; then\n        PYTHONPATH\="\$_OLD_VIRTUAL_PYTHONPATH"\n        export PYTHONPATH\n        unset _OLD_VIRTUAL_PYTHONPATH\n    fi/' py3-v4.3.0_tensorflow2.14/bin/activate

    pip install tensorflow==2.14 tensorflow_probability==0.22.1

    cat << 'EOF' >> py3-v4.3.0_tensorflow2.14/bin/activate
    export CUDA_HOME=/data/user/mhuennefeld/software/cuda/cuda-11.8
    export PATH=$PATH:${CUDA_HOME}/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${CUDA_HOME}/lib64
    EOF

    pip install pybind11

    export I3_BUILD=/cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/RHEL_7_x86_64/metaprojects/icetray/v1.12.0/

    export I3_SRC=/cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/metaprojects/icetray/v1.12.0/

    pip install git+ssh://git@github.com/icecube/TFScripts

    pip install git+ssh://git@github.com/icecube/ic3-labels

    pip install git+ssh://git@github.com/icecube/ic3-data

    ########################################################################
    # typically,
    # if there is a HDF5 version mismatch we must install h5py from source
    # Use: 'h5cc -showconfig' to obtain hdf5 configuration and library version
    # use: 'ls -lah $(which h5cc)' to obtain path to hdf5 directory
    pip uninstall h5py

    HDF5_VERSION=1.14.0 HDF5_DIR=/cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/RHEL_7_x86_64/spack/opt/spack/linux-centos7-x86_64_v2/gcc-13.1.0/hdf5-1.14.0-4p2djysy6f7vful3egmycsguijjddkah pip install --no-binary=h5py h5py==3.11.0
    ########################################################################

    mkdir /data/user/{USER}/technical_review/repositories 

    cd /data/user/{USER}/technical_review/repositories

    git clone https://github.com/mhuen/dnn_reco.git

    # install package
    pip install -e dnn_reco

    git clone https://github.com/mhuen/ic3-processing.git

    pip install -e ic3-processing

    # Now you can verify your installation. Log out from cobalt and log in again.
    # load icecube environment
    eval $(/cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/setup.sh)

    /cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/RHEL_7_x86_64/metaprojects/icetray/v1.12.0/env-shell.sh

    source /data/user/{USER}/technical_review/virtual_envs/py3-v4.3.0_tensorflow2.14/bin/activate

    echo $CUDA_HOME
    # this should print: /data/user/mhuennefeld/software/cuda/cuda-11.8

    python -c 'import tensorflow as tf; print(tf.__version__)'
    # this should print some information about about tensorflow, which can take up to a minute, the the last print should be: 2.14.0

    python -c 'import dnn_reco; import tfscripts; import ic3_labels; import ic3_data'
    # this should not print any error messages (Could not find TensorRT -- is expected)

    # install analysis repo
    cd /data/user/{USER}/technical_review/repositories

    git clone git@github.com:icecube/dnn_selections.git

    pip install -e dnn_selections

    cd dnn_selections

    git checkout -b AnalysisPipeline origin/AnalysisPipeline

.. note::
    The prebuilt tensorflow binary is built to use avx2 and ssse3 instructions among others.
    These are not available on cobalts 1 through 4.
    Attempting to import tensorflow will lead to an "illegal instructions"
    error. Therefore, if running on the cobalts, simply choose one of the
    newer machines: cobalt >=5.
    On NPX, if running CPU jobs, you can request nodes with avx2 and ssse3
    support by adding: ``requirements = (TARGET.has_avx2) && (TARGET.has_ssse3)``. This is only necessary for CPU jobs. For GPU jobs,
    these requirements should not be set.

