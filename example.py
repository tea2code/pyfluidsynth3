from pyfluidsynth3 import fluidaudiodriver, fluidhandle, fluidsettings, fluidsynth

import time

handle = fluidhandle.FluidHandle( 'F:/Programmieren/librarys/fluidsynth-bin/libfluidsynth.dll' )
settings = fluidsettings.FluidSettings( handle )
synth = fluidsynth.FluidSynth( handle, settings )

synth.load_soundfont( 'F:/Programmieren/librarys/fluidsynth-bin/FluidR3_GM.sf2' )

driver = fluidaudiodriver.FluidAudioDriver( handle, synth, settings )

seq = (79, 78, 79, 74, 79, 69, 79, 67, 79, 72, 79, 76,
       79, 78, 79, 74, 79, 69, 79, 67, 79, 72, 79, 76,
       79, 78, 79, 74, 79, 72, 79, 76, 79, 78, 79, 74,
       79, 72, 79, 76, 79, 78, 79, 74, 79, 72, 79, 76,
       79, 76, 74, 71, 69, 67, 69, 67, 64, 67, 64, 62,
       64, 62, 59, 62, 59, 57, 64, 62, 59, 62, 59, 57,
       64, 62, 59, 62, 59, 57, 43)

for note in seq:
    synth.noteon( 0, note, 1.0 )
    time.sleep( 0.1 )
    synth.noteoff( 0, note )