{
  gROOT->ProcessLine(".L analyze.c");
  
  useWaveformFile("waveforms.root");
  readData("CH1.csv");
  makeHist("CH1");
  readData("CH2.csv");
  makeHist("CH2");
  readData("CH3.csv");
  makeHist("CH3");
  readData("CH4.csv");
  makeHist("CH4");
  
  examineWaveform("waveforms.root");
  signalStats("signal_stats");
  waveformAttributes("waveform_attributes");
  noiseFFT("waveforms.root");
}
