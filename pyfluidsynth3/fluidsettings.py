from ctypes import byref, c_char_p, c_double, c_int

class FluidSettings(object):
    ''' Represents the FluidSynth settings as defined in settings.h. A instance of this class 
    can be used like an array aka like the fluidsettings_t object. This means you can get/set 
    values using brackets (See example below).
    
    This class is inspired by the FluidSettings object from pyfluidsynth by MostAwesomeDude.
    
    Example:
    fluidsettings = FluidSettings( handle )
    fluidsettings['audio.driver'] = 'alsa'
    
    Constants:
    FLUID_NO_TYPE -- Settings type: Undefined type.
    FLUID_NUM_TYPE -- Settings type: Numeric (double).
    FLUID_INT_TYPE -- Settings type: Integer.
    FLUID_STR_TYPE -- Settings type: String.
    FLUID_SET_TYPE -- Settings type: Set of values.
    QUALITY_LOW -- Quality preset: Low.
    QUALITY_MED -- Quality preset: Medium.
    QUALITY_HIGH -- Quality preset: High.
    FALSE -- Settings boolean value for false/off/no/0.
    TRUE -- Settings boolean value for true/on/yes/1.
    
    Member:
    handle -- The handle to the FluidSynth library. Should be FluidHandle but a raw handle will 
               probably work, too (FluidHandle).
    quality -- The last quality preset used (string).
    settings -- The FluidSynth settings object (fluidsettings_t).
    '''
    
    (FLUID_NO_TYPE, 
     FLUID_NUM_TYPE, 
     FLUID_INT_TYPE, 
     FLUID_STR_TYPE,
     FLUID_SET_TYPE) = range(-1, 4)
     
    QUALITY_LOW = 'low'
    QUALITY_MEDIUM = 'med'
    QUALITY_HIGH = 'high'
    
    FALSE = 0
    TRUE = 1

    def __init__( self, handle ):
        ''' Create new FluidSynth settings instance using the given handle. Default quality is set 
        to medium. '''
        self.handle = handle
        self.settings = self.handle.new_fluidsettings()
        self.quality = self.QUALITY_MEDIUM

    @property
    def quality( self ):
        ''' Returns the last quality preset used. '''
        return self._quality

    @quality.setter
    def quality( self, quality ):
        ''' Sets the given quality preset. '''
        self._quality = quality
        
        if quality == self.QUALITY_LOW:
            self['synth.chorus.active'] = self.FALSE
            self['synth.reverb.active'] = self.FALSE
            self['synth.sample-rate'] = 22050
            
        elif quality == self.QUALITY_MEDIUM:
            self['synth.chorus.active'] = self.FALSE
            self['synth.reverb.active'] = self.TRUE
            self['synth.sample-rate'] = 44100
            
        elif quality == self.QUALITY_HIGH:
            self['synth.chorus.active'] = self.TRUE
            self['synth.reverb.active'] = self.TRUE
            self['synth.sample-rate'] = 44100

    def __del__( self ):
        ''' Deletes the FluidSynth settings object. '''
        self.handle.delete_fluidsettings( self.settings )

    def __getitem__( self, key ):
        ''' Returns the value of the given settings key. '''
        key_type = self.handle.fluidsettings_get_type( self.settings, key )
        
        if key_type == self.FLUID_NUM_TYPE:
            val = c_double()
            func = self.handle.fluidsettings_getnum
        elif key_type == self.FLUID_INT_TYPE:
            val = c_int()
            func = self.handle.fluidsettings_getint
        elif key_type == self.FLUID_STR_TYPE:
            val = c_char_p()
            func = self.handle.fluidsettings_getstr
        else:
            raise KeyError( key )

        if func( self.settings, key, byref(val) ):
            return val.value
        else:
            raise KeyError( key )

    def __setitem__( self, key, value ):
        ''' Sets the value of the given settings key to value. '''
        key_type = self.handle.fluidsettings_get_type( self.settings, key )
        
        if key_type == self.FLUID_STR_TYPE:
            if not self.handle.fluidsettings_setstr( self.settings, key, value ):
                raise KeyError( key )
            
        else:
            # Coerce string value to integer before going further.
            value = self.__coerce_to_int( value )
            
            if key_type == self.FLUID_NUM_TYPE:
                if not self.handle.fluidsettings_setnum( self.settings, key, value ):
                    raise KeyError( key )
                
            elif key_type == self.FLUID_INT_TYPE:
                if not self.handle.fluidsettings_setint( self.settings, key, value ):
                    raise KeyError( key )
                
            else:
                raise KeyError( key )
            
    def __coerce_to_int( self, stringValue ):
        ''' Turn a string into an integer. '''
        try:
            return int( stringValue )
        except ValueError:
            return int( stringValue.lower() not in ('false', 'no', 'off') )