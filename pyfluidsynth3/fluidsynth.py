from . import fluiderror, utility

class FluidSynth():
    ''' Represents the FluidSynth synth object as defined in synth.h.
    
    This class is inspired by the FluidSynth object from pyfluidsynth by MostAwesomeDude. Method 
    documentation is mostly taken from FluidSynth's official API.
    
    Constants:
    FLUID_OK -- Value that indicates success.
    FLUID_FAILED -- Value that indicates failure.
    
    Member:
    handle -- The handle to the FluidSynth library. Should be FluidHandle but a raw handle will 
              probably work, too (FluidHandle).
    settings -- The settings object (FluidSettings).
    synth -- The FluidSynth synth object (fluid_synth_t).
    _sf_dict -- Dictionary of soundfonts (dict).
    '''

    FLUID_OK = 0
    FLUID_FAILED = -1

    def __init__( self, handle, settings ):
        ''' Creates a new FluidSynth synth instance using the given handle and settings. '''
        self.handle = handle
        self.settings = settings
        self.synth = self.handle.new_fluid_synth( self.settings.settings )
        self._sf_dict = {}
        
    def __del__( self ):
        ''' Removes all soundfonts and deletes synth instance. '''
        failed = []
        for sf in self._sf_dict:
            result = self.handle.fluid_synth_sfunload( self.synth, self._sf_dict[sf], True )
            if result is self.FLUID_FAILED:
                failed.append(sf)
        self.handle.delete_fluid_synth( self.synth )

        if failed:
            raise fluiderror.FluidError( "Couldn't unload soundfonts: {0}".format(failed) )

    def load_soundfont( self, sf, reload_presets = True ):
        ''' Load soundfont. If reload presets is true FluidSynth will reassign all MIDI channels. '''
        sf_raw = sf
        sf = utility.fluidstring( sf )
        
        if sf in self._sf_dict:
            result = self.handle.fluid_synth_sfreload( self.synth, self._sf_dict[sf] )
            if result is self.FLUID_FAILED:
                raise fluiderror.FluidError( "Couldn't reload soundfont {0}".format(sf_raw) )
            
        else:
            result = self.handle.fluid_synth_sfload( self.synth, sf, reload_presets )
            if result is self.FLUID_FAILED:
                raise fluiderror.FluidError( "Couldn't load soundfont {0}".format(sf_raw) )
            else:
                self._sf_dict[sf_raw] = result

    def unload_soundfont( self, sf, reload_presets = True ):
        ''' Unload soundfont. If reload presets is true FluidSynth will reassign all midi channels. '''
        sf_raw = sf
        sf = utility.fluidstring( sf )
        
        if sf not in self._sf_dict:
            raise fluiderror.FluidError( "Soundfont {0} never loaded".format(sf_raw) )
        
        result = self.handle.fluid_synth_sfunload( self.synth, self._sf_dict[sf], reload_presets )
        if result is self.FLUID_FAILED:
            raise fluiderror.FluidError( "Couldn't unload soundfont %s".format(sf_raw) )
        else:
            del self._sf_dict[sf_raw]

    def noteon( self, channel, pitch, velocity ):
        ''' Send a note-on event to a FluidSynth object. Returns true in case of success else 
        false. '''
        if isinstance( velocity, float ):
            velocity = int( velocity * 127 )
        result = self.handle.fluid_synth_noteon( self.synth, channel, pitch, velocity )
        return result == self.FLUID_OK

    def noteoff( self, channel, pitch ):
        ''' Send a note-off event to a FluidSynth object. Returns true in case of success else 
        false. '''
        result = self.handle.fluid_synth_noteoff( self.synth, channel, pitch )
        return result == self.FLUID_OK

    def cc( self, channel, control, value ):
        ''' Send a MIDI controller event on a MIDI channel. An alias method "constrol_change" 
        exists. Returns true in case of success else false. '''
        result = self.handle.fluid_synth_cc( self.synth, channel, control, value )
        return result == self.FLUID_OK

    control_change = cc

    def pitch_bend( self, channel, value ):
        ''' Set the MIDI pitch bend controller value on a MIDI channel. Returns true in case of 
        success else false. '''
        result = self.handle.fluid_synth_pitch_bend( self.synth, channel, value )
        return result == self.FLUID_OK

    def pitch_wheel_sens( self, channel, value ):
        ''' Set MIDI pitch wheel sensitivity on a MIDI channel. An alias method 
        "pitch_wheel_sensitivity" exists. Returns true in case of success else false. '''
        result = self.handle.fluid_synth_pitch_wheel_sens( self.synth, channel, value )
        return result == self.FLUID_OK

    pitch_wheel_sensitivity = pitch_wheel_sens

    def program_change( self, channel, program ):
        ''' Send a program change event on a MIDI channel. Returns true in case of success else 
        false. '''
        result = self.handle.fluid_synth_program_change( self.synth, channel, program )
        return result == self.FLUID_OK

    def bank_select( self, channel, bank ):
        ''' Set instrument bank number on a MIDI channel. Returns true in case of success else 
        false. '''
        result = self.handle.fluid_synth_bank_select( self.synth, channel, bank )
        return result == self.FLUID_OK