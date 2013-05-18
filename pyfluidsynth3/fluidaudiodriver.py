class FluidAudioDriver():
    ''' Represents the FluidSynth audio driver object as defined in audio.h.
    
    This class is inspired by the FluidAudioDriver object from pyfluidsynth by MostAwesomeDude.

    Member:
    audio_driver -- The FluidSynth audio driver object (fluid_audio_driver_t).
    handle -- The handle to the FluidSynth library. Should be FluidHandle but a raw handle will 
              probably work, too (FluidHandle).
    '''
    
    def __init__( self, handle, synth, settings ):
        ''' Create a new FluidSynth audio driver instance using given handle, synth and settings
        objects. '''
        self.handle = handle
        self.audio_driver = handle.new_fluid_audio_driver( settings.settings, synth.synth )
        
    def __del__(self):
        ''' Delete the audio driver. '''
        self.handle.delete_fluid_audio_driver( self.audio_driver )