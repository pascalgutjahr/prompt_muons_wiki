import tables

# defining data types
FinalTableLayout = [('Run', Run.dtype),
                    ('Event', Event.dtype),
                    ('SubEvent', SubEvent.dtype),
                    ('Energy', energy.dtype),
                    ('ParticleType', ptype.dtype),
                    ('GenValues', genvalues.dtype),
                    ('TimeScale', WMAPtimescale.dtype)]

for Name, Short, Func in ChosenList:
    FinalTableLayout.append((Name,'<f8'))
if 'poly' in options.models:
    FinalTableLayout.append(('Polygonato','<f8'))

# set table type for dataset
Data = np.zeros((len(Run),), dtype=FinalTableLayout)
Data['Run']          = Run
Data['Event']        = Event
Data['SubEvent']     = SubEvent
Data['Energy']       = energy
Data['ParticleType'] = ptype
Data['GenValues']    = genvalues
Data['TimeScale']    = WMAPtimescale

for Name,S hort, Func in ChosenList:
    Data[Name] = Func(energy, ptype) / genvalues

if 'poly' in options.models:
    Data['Polygonato'] = WMAPweight * WMAPpolygonato * WMAPDiplopia / (WMAPtimescale * nfiles)

# open file for reading
OutFile = tables.openFile(options.outfile, 'w')
# store data in hdf5 file set '/' as root directory
A = OutFile.createTable('/', 'U_Weights', Data)
# close file
OutFile.close()
