from ctypes import cdll, c_char_p, c_double, c_int, c_void_p
from ctypes.util import find_library

import os

class FluidHandle():
    ''' Creates a handle to the FluidSynth library. A instance of this class can be used the same
    way any real library handle to FluidSynth can be used. It "implements" all necessary 
    FluidSynth functions.
    
    This class is inspired by the bindings from pyFluidSynth by Whitehead and pyfluidsynth by 
    MostAwesomeDude.
    
    Member:
    library_path -- The path of the loaded library (string).
    _handle -- The raw library handle. 
    '''
    
    def __init__( self, library_path = None ):
        self._handle = self.load_library( library_path )
        
        # From settings.h
        self.new_fluid_settings = self._handle.new_fluid_settings
        self.new_fluid_settings.argtypes = ()
        self.new_fluid_settings.restype = c_void_p
        
        self.delete_fluid_settings = self._handle.delete_fluid_settings
        self.delete_fluid_settings.argtypes = (c_void_p,)
        self.delete_fluid_settings.restype = None
        
        self.fluid_settings_get_type = self._handle.fluid_settings_get_type
        self.fluid_settings_get_type.argtypes = (c_void_p, c_char_p)
        self.fluid_settings_get_type.restype = c_int
        
        self.fluid_settings_getnum = self._handle.fluid_settings_getnum
        self.fluid_settings_getnum.argtypes = (c_void_p, c_char_p, c_void_p)
        self.fluid_settings_getnum.restype = c_int
        
        self.fluid_settings_getint = self._handle.fluid_settings_getint
        self.fluid_settings_getint.argtypes = (c_void_p, c_char_p, c_void_p)
        self.fluid_settings_getint.restype = c_int
        
        self.fluid_settings_getstr = self._handle.fluid_settings_getstr
        self.fluid_settings_getstr.argtypes = (c_void_p, c_char_p, c_void_p)
        self.fluid_settings_getstr.restype = c_int
        
        self.fluid_settings_setnum = self._handle.fluid_settings_setnum
        self.fluid_settings_setnum.argtypes = (c_void_p, c_char_p, c_double)
        self.fluid_settings_setnum.restype = c_int
        
        self.fluid_settings_setnum = self._handle.fluid_settings_setnum
        self.fluid_settings_setint.argtypes = (c_void_p, c_char_p, c_int)
        self.fluid_settings_setint.restype = c_int
        
        self.fluid_settings_setstr = self._handle.fluid_settings_setstr
        self.fluid_settings_setstr.argtypes = (c_void_p, c_char_p, c_char_p)
        self.fluid_settings_setstr.restype = c_int

    def load_library( self, library_path ):
        ''' Create new FluidSynth handle with given library path. If no specific path is given
        or the file doesn't exist this class will try to find the library based on some basic 
        heuristics. '''
        
        # TODO: Search in current directory.
        if not library_path or not os.path.isfile( library_path ):
            self.library_path = find_library('fluidsynth') or \
                                find_library('libfluidsynth') or \
                                find_library('libfluidsynth-1')
        else:
            self.library_path = library_path
            
        return cdll.LoadLibrary( self.library_path )