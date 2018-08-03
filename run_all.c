{
  gROOT->ProcessLine(".L analyze.c");
  
  useWaveformFile("waveforms.root");
  readData("waveform_1.csv");
  makeHist("waveform_1");
  readData("waveform_2.csv");
  makeHist("waveform_2");
  ...
  ...
  ...
  
  examineWaveform("waveforms.root");
  signalStats("signal_stats");
  waveformAttributes("waveform_attributes");
}
