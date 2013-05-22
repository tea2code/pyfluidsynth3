# pyfluidsynth3

Python 3 binding for [FluidSynth](http://www.fluidsynth.org/). 

It is loosely based on the Python 2 binding projects [pyFluidSynth by Whitehead](http://code.google.com/p/pyfluidsynth/) and [pyfluidsynth by MostAwesomeDude](https://github.com/MostAwesomeDude/pyfluidsynth). Code snippets which are directly copied from one of the projects are marked. The licenses should allow this but please correct me if i'm wrong. I will try to implement at least all of the features of this projects. Maybe higher level features like support for the [abc notation](http://abcnotation.com/) will follow.

## License

Copyright 2013, Stefan Gfroerer aka tea2code.

Released under the [GNU Lesser GPL (LGPL)](http://www.gnu.org/copyleft/lesser.html).

### License of pyFluidSynth by Whitehead

Copyright 2008, Nathan Whitehead <nwhitehe@gmail.com>, maintained by Bart Spaans <onderstekop@gmail.com> 

Released under the LGPL

### License of pyfluidsynth by MostAwesomeDude

Copyright (c) 2009 Corbin Simpson

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

## Example

    from pyfluidsynth3 import fluidaudiodriver, fluidhandle, fluidsettings, fluidsynth
    import time
    
    handle = fluidhandle.FluidHandle( 'libfluidsynth.dll' )
    settings = fluidsettings.FluidSettings( handle )
    synth = fluidsynth.FluidSynth( handle, settings )
    synth.load_soundfont( 'soundfont.sf2' )
    driver = fluidaudiodriver.FluidAudioDriver( handle, synth, settings )
    
    synth.noteon( 0, 79, 1.0 )
    time.sleep( 1 )
    synth.noteoff( 0, 79 )

## Development

I normally prefer camel case function and variable names. But to give a uniform look with the native FluidSynth functions i used an underscore based style.

I tried to give every method a meaningful result which also matches more the original FluidSynth behavior. To make things easier FluidSynth results are translated if possible. For example methods like *noteon()* return a boolean instead of *FLUID_OK* or *FLUID_FAILED*.

If you try to access FluidSynth raw method you must encode every string parameter because of Python 3's navtive unicode support (which is by the way great). I added a utility method *fluidstring()* which does this.

## Known Issues

- Not all FluidSynth methods are implemented.
- The example sequencer.py seems not to work.