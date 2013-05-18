# pyfluidsynth3

Python 3 binding for [FluidSynth](http://www.fluidsynth.org/). 

It is loosely based on the Python 2 binding projects [pyFluidSynth by Whitehead](http://code.google.com/p/pyfluidsynth/) and [pyfluidsynth by MostAwesomeDude](https://github.com/MostAwesomeDude/pyfluidsynth). Code snippets which are directly copied from one of the projects are marked. The licenses should allow this but please correct me if i'm wrong. I will try to implement at least all of the features of this projects. Maybe higher level features like support for the [abc notation](http://abcnotation.com/) will follow.

## License

Copyright 2013, Stefan Gfroerer aka tea2code.

Released under the [GNU Lesser GPL (LGPL)](http://www.gnu.org/copyleft/lesser.html).

## Example

    from pyfluidsynth3 import fluidaudiodriver, fluidhandle, fluidsettings, fluidsynth
    import time
    
    handle = fluidhandle.FluidHandle( 'libfluidsynth.dll' )
    settings = fluidsettings.FluidSettings( handle )
    synth = fluidsynth.FluidSynth( handle, settings )
    synth.load_soundfont( 'soundfont.sf2' )
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

## Development

I normally prefer camel case function and variable names. But to give a uniform look with the native FluidSynth functions i used an underscore based style.

I tried to give every method a meaningful result which also matches more the original FluidSynth behavior. To make things easier a translated FluidSynth results if possible. For example return methods like *noteon()* a boolean instead of *FLUID_OK* or *FLUID_FAILED*.

If you try to access FluidSynth raw method you must encode every string parameter because of Python 3's navtive unicode support. I added a utility method *fluidstring()* which does this.