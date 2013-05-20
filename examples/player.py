from pyfluidsynth3 import fluidaudiodriver, fluidhandle, fluidplayer, fluidsettings, fluidsynth

import sys

''' Based on the examples from pyfluidsynth by MostAwesomeDude. '''

if len( sys.argv ) < 4:
    print( "Usage: {0} library soundfont.sf2 song.mid".format(sys.argv[0]) )
    sys.exit()

handle = fluidhandle.FluidHandle( sys.argv[1] )
settings = fluidsettings.FluidSettings( handle )
synth = fluidsynth.FluidSynth( handle, settings )
driver = fluidaudiodriver.FluidAudioDriver( handle, synth, settings )
player = fluidplayer.FluidPlayer( handle, synth )

synth.load_soundfont( sys.argv[2] )

player.play( sys.argv[3] )
player.join()