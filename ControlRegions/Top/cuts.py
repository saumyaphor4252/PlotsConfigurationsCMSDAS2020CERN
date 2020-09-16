# cuts

supercut = ' mll > 12 \
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>13 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
           '

## Signal regions
cuts['hww2l2v_13TeV'] = {
   'expr': 'bReq',
    # Define the sub-categorization of sr
   'categories' : {
      #
      'em' : ' multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)',
      #
   }
}

