if datatype=="nue" or datatype=="numu":

    from icecube import neutrinoflux
    from icecube.weighting import get_weighted_primary, weighting
    if datatype=="numu":
        atmo=neutrinoflux.AtmosphericNeutrinoFlux("honda2006_numu","sarcevic_std_numu")
    elif datatype=="nue":
        atmo=neutrinoflux.AtmosphericNeutrinoFlux("honda2006_nue","sarcevic_std_nue") #
    astro=neutrinoflux.AstroNeutrinoFlux("W00_sum")
    #if nfiles!=0:
    #   nfiles = weighting.from_simprod(dataset)[0]

    '''
    not yet possible:
    tray.AddModule(WeightCalculator, 'honda2006',
        Dataset=dataset,
        Flux=atmo_numu.getFlux,
        If  =(lambda frame: (not frame.Has("honda2006")))
    )
    '''

    tray.AddModule(get_weighted_primary, "getPrimary",)

    def calcWeight(frame, Dataset="", Flux=None, Name=""):
        '''
        http://code.icecube.wisc.edu/projects/icecube/browser/IceCube/sandbox/jvansanten/weighting/trunk/resources/docs/index.rst
        '''
        if not "I3MCWeightDict" in frame:
            raise RuntimeError("I3MCWeightDict not found!")
        if not "MCPrimary" in frame:
            raise RuntimeError("MCPrimary not found!")

        energy = frame["MCPrimary"].energy
        ptype  = frame["MCPrimary"].type
        costheta=math.cos(frame["MCPrimary"].dir.zenith)
        oneweight = frame["I3MCWeightDict"]["OneWeight"]
        nevents = frame["I3MCWeightDict"]["NEvents"]

        flux = Flux.getFlux(ptype, energy, costheta)
        weight = flux * oneweight / (nevents / 2)
        #if NFiles!=0:
        #    weight/=NFiles
        frame['NeutrinoWeight_'+Name] = dataclasses.I3Double(weight)

    tray.AddModule(calcWeight, "calcWeight",
        Name = "Honda2006_Sarcevic-STD",
        Dataset = dataset,
        Flux    = atmo,
        #NFiles  = nfiles,
    )

    tray.AddModule(calcWeight, "calcWeightastro",
        Name = "W00_sum-STD",
        Dataset = dataset,
        Flux    = astro,
        #NFiles  = nfiles,
    )

elif datatype=="corsika":
    from icecube.weighting import WeightCalculator
    from icecube.weighting import fluxes
    tray.AddModule(WeightCalculator, 'GaisserH3aWeight',
               Dataset=dataset,
               Flux=fluxes.GaisserH3a(),
               If  =(lambda frame: (not frame.Has("GaisserH3aWeight")))
               )