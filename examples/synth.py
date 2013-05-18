from pyfluidsynth3 import fluidaudiodriver, fluidhandle, fluidsettings, fluidsynth

import sys
import time

''' Based on the examples from pyfluidsynth by MostAwesomeDude. '''

if len( sys.argv ) < 3:
    print( "Usage: %s library soundfont.sf2".format(sys.argv[0]) )
    sys.exit()

handle = fluidhandle.FluidHandle( sys.argv[1] )
settings = fluidsettings.FluidSettings( handle )
synth = fluidsynth.FluidSynth( handle, settings )
driver = fluidaudiodriver.FluidAudioDriver( handle, synth, settings )

synth.load_soundfont( sys.argv[2] )

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