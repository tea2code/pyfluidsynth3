from ctypes import cdll, c_char_p, c_double, c_int, c_short, c_uint, c_void_p
from ctypes.util import find_library

import os

class FluidHandle():
    ''' Creates a handle to the FluidSynth library. A instance of this class can be used the same
    way any real library handle to FluidSynth can be used. It "implements" all necessary 
    FluidSynth functions.
    
    This class is inspired by the bindings from pyFluidSynth by Whitehead and pyfluidsynth by 
    MostAwesomeDude.
    
    Member:
    handle -- The raw library handle. 
    library_path -- The path of the loaded library (string).
    '''
    
    def __init__( self, library_path = None ):
        self.handle = self.load_library( library_path )
        
        # From settings.h
        self.new_fluid_settings = self.handle.new_fluid_settings
        self.new_fluid_settings.argtypes = ()
        self.new_fluid_settings.restype = c_void_p
        
        self.delete_fluid_settings = self.handle.delete_fluid_settings
        self.delete_fluid_settings.argtypes = (c_void_p,)
        self.delete_fluid_settings.restype = None
        
        self.fluid_settings_get_type = self.handle.fluid_settings_get_type
        self.fluid_settings_get_type.argtypes = (c_void_p, c_char_p)
        self.fluid_settings_get_type.restype = c_int
        
        self.fluid_settings_getnum = self.handle.fluid_settings_getnum
        self.fluid_settings_getnum.argtypes = (c_void_p, c_char_p, c_void_p)
        self.fluid_settings_getnum.restype = c_int
        
        self.fluid_settings_getint = self.handle.fluid_settings_getint
        self.fluid_settings_getint.argtypes = (c_void_p, c_char_p, c_void_p)
        self.fluid_settings_getint.restype = c_int
        
        self.fluid_settings_getstr = self.handle.fluid_settings_getstr
        self.fluid_settings_getstr.argtypes = (c_void_p, c_char_p, c_void_p)
        self.fluid_settings_getstr.restype = c_int
        
        self.fluid_settings_setnum = self.handle.fluid_settings_setnum
        self.fluid_settings_setnum.argtypes = (c_void_p, c_char_p, c_double)
        self.fluid_settings_setnum.restype = c_int
        
        self.fluid_settings_setint = self.handle.fluid_settings_setint
        self.fluid_settings_setint.argtypes = (c_void_p, c_char_p, c_int)
        self.fluid_settings_setint.restype = c_int
        
        self.fluid_settings_setstr = self.handle.fluid_settings_setstr
        self.fluid_settings_setstr.argtypes = (c_void_p, c_char_p, c_char_p)
        self.fluid_settings_setstr.restype = c_int
        
        # From synth.h
        self.new_fluid_synth = self.handle.new_fluid_synth
        self.new_fluid_synth.argtypes = (c_void_p,)
        self.new_fluid_synth.restype = c_void_p
        
        self.delete_fluid_synth = self.handle.delete_fluid_synth
        self.delete_fluid_synth.argtypes = (c_void_p,)
        self.delete_fluid_synth.restype = None
        
        self.fluid_synth_sfload = self.handle.fluid_synth_sfload
        self.fluid_synth_sfload.argtypes = (c_void_p, c_char_p, c_int)
        self.fluid_synth_sfload.restype = c_int
        
        self.fluid_synth_sfreload = self.handle.fluid_synth_sfreload
        self.fluid_synth_sfreload.argtypes = (c_void_p, c_uint)
        self.fluid_synth_sfreload.restype = c_int
        
        self.fluid_synth_sfunload = self.handle.fluid_synth_sfunload
        self.fluid_synth_sfunload.argtypes = (c_void_p, c_uint, c_int)
        self.fluid_synth_sfunload.restype = c_int
        
        self.fluid_synth_noteon = self.handle.fluid_synth_noteon
        self.fluid_synth_noteon.argtypes = (c_void_p, c_int, c_int, c_int)
        self.fluid_synth_noteon.restype = c_int
        
        self.fluid_synth_noteoff = self.handle.fluid_synth_noteoff
        self.fluid_synth_noteoff.argtypes = (c_void_p, c_int, c_int)
        self.fluid_synth_noteoff.restype = c_int
        
        self.fluid_synth_cc = self.handle.fluid_synth_cc
        self.fluid_synth_cc.argtypes = (c_void_p, c_int, c_int, c_int)
        self.fluid_synth_cc.restype = c_int
        
        self.fluid_synth_pitch_bend = self.handle.fluid_synth_pitch_bend
        self.fluid_synth_pitch_bend.argtypes = (c_void_p, c_int, c_int)
        self.fluid_synth_pitch_bend.restype = c_int
        
        self.fluid_synth_pitch_wheel_sens = self.handle.fluid_synth_pitch_wheel_sens
        self.fluid_synth_pitch_wheel_sens.argtypes = (c_void_p, c_int, c_int)
        self.fluid_synth_pitch_wheel_sens.restype = c_int
        
        self.fluid_synth_program_change = self.handle.fluid_synth_program_change
        self.fluid_synth_program_change.argtypes = (c_void_p, c_int, c_int)
        self.fluid_synth_program_change.restype = c_int
        
        self.fluid_synth_bank_select = self.handle.fluid_synth_bank_select
        self.fluid_synth_bank_select.argtypes = (c_void_p, c_int, c_int)
        self.fluid_synth_bank_select.restype = c_int
        
        # From audio.h
        self.new_fluid_audio_driver = self.handle.new_fluid_audio_driver
        self.new_fluid_audio_driver.argtypes = (c_void_p, c_void_p)
        self.new_fluid_audio_driver.restype = c_void_p
        
        self.delete_fluid_audio_driver = self.handle.delete_fluid_audio_driver
        self.delete_fluid_audio_driver.argtypes = (c_void_p,)
        self.delete_fluid_audio_driver.restype = None
        
        # From midi.h
        self.new_fluid_player = self.handle.new_fluid_player
        self.new_fluid_player.argtypes = (c_void_p,)
        self.new_fluid_player.restype = c_void_p
        
        self.delete_fluid_player = self.handle.delete_fluid_player
        self.delete_fluid_player.argtypes = (c_void_p,)
        self.delete_fluid_player.restype = c_int
        
        self.fluid_player_add = self.handle.fluid_player_add
        self.fluid_player_add.argtypes = (c_void_p, c_char_p)
        self.fluid_player_add.restype = c_int
        
        self.fluid_player_play = self.handle.fluid_player_play
        self.fluid_player_play.argtypes = (c_void_p,)
        self.fluid_player_play.restype = c_int
        
        self.fluid_player_stop = self.handle.fluid_player_stop
        self.fluid_player_stop.argtypes = (c_void_p,)
        self.fluid_player_stop.restype = c_int
        
        self.fluid_player_join = self.handle.fluid_player_join
        self.fluid_player_join.argtypes = (c_void_p,)
        self.fluid_player_join.restype = c_int
        
        # From event.h
        self.new_fluid_event = self.handle.new_fluid_event
        self.new_fluid_event.argtypes = ()
        self.new_fluid_event.restype = c_void_p
        
        self.delete_fluid_event = self.handle.delete_fluid_event
        self.delete_fluid_event.argtypes = (c_void_p,)
        self.delete_fluid_event.restype = None
        
        self.fluid_event_timer = self.handle.fluid_event_timer
        self.fluid_event_timer.argtypes = (c_void_p, c_void_p)
        self.fluid_event_timer.restype = None
        
        self.fluid_event_volume = self.handle.fluid_event_volume
        self.fluid_event_volume.argtypes = c_void_p, c_int, c_short
        self.fluid_event_volume.restype = None
        
        self.fluid_event_note = self.handle.fluid_event_note
        self.fluid_event_note.argtypes = (c_void_p, c_int, c_short, c_short, c_uint)
        self.fluid_event_note.restype = None
        
        self.fluid_event_noteon = self.handle.fluid_event_noteon
        self.fluid_event_noteon.argtypes = (c_void_p, c_int, c_short, c_short)
        self.fluid_event_noteon.restype = None
        
        self.fluid_event_noteoff = self.handle.fluid_event_noteoff
        self.fluid_event_noteoff.argtypes = (c_void_p, c_int, c_short)
        self.fluid_event_noteoff.restype = None
        
        self.fluid_event_pitch_bend = self.handle.fluid_event_pitch_bend
        self.fluid_event_pitch_bend.argtypes = c_void_p, c_int, c_int
        self.fluid_event_pitch_bend.restype = None
        
        self.fluid_event_pitch_wheelsens = self.handle.fluid_event_pitch_wheelsens
        self.fluid_event_pitch_wheelsens.argtypes = c_void_p, c_int, c_short
        self.fluid_event_pitch_wheelsens.restype = None
        
        self.fluid_event_program_change = self.handle.fluid_event_program_change
        self.fluid_event_program_change.argtypes = c_void_p, c_int, c_short
        self.fluid_event_program_change.restype = None
        
        self.fluid_event_get_source = self.handle.fluid_event_get_source
        self.fluid_event_get_source.argtypes = (c_void_p,)
        self.fluid_event_get_source.restype = c_short
        
        self.fluid_event_set_source = self.handle.fluid_event_set_source
        self.fluid_event_set_source.argtypes = (c_void_p, c_short)
        self.fluid_event_set_source.restype = None
        
        self.fluid_event_get_dest = self.handle.fluid_event_get_dest
        self.fluid_event_get_dest.argtypes = (c_void_p,)
        self.fluid_event_get_dest.restype = c_short
        
        self.fluid_event_set_dest = self.handle.fluid_event_set_dest
        self.fluid_event_set_dest.argtypes = (c_void_p, c_short)
        self.fluid_event_set_dest.restype = None

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