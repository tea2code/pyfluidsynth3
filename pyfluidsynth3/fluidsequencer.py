from . import constants, utility

class FluidSequencer( dict ):
    ''' Represents the FluidSynth sequencer object as defined in seq.h. A instance of this class 
    is a dictionary which maps FluidSynth objects to their sequencer id and client name.
    
    This class is inspired by the FluidSequencer object from pyfluidsynth by MostAwesomeDude. Method 
    documentation is mostly taken from FluidSynth's official API.
    
    Constants:
    BPM_DEFAULT -- Initial default value of beats per minute.
    TPB_DEFAULT -- Initial default value of ticks per beat.
    
    Member:
    handle -- The handle to the FluidSynth library. Should be FluidHandle but a raw handle will 
              probably work, too (FluidHandle).
    seq -- The FluidSynth sequencer object (fluid_sequencer_t).
    _bpm -- Current value of beats per minute (int).
    _tpb -- Current value of ticks per beat (int).
    '''
    
    BPM_DEFAULT = 120
    TPB_DEFAULT = 120

    def __init__( self, handle, *synths ):
        ''' Creates a new FluidSynth sequencer instance with the given handle. If not empty all
        FluidSynth objects will be registered to this sequencer. '''        
        super( FluidSequencer, self ).__init__()

        self.handle = handle
        self.seq = self.handle.new_fluid_sequencer()

        if synths:
            for synth in synths:
                self.add_synth( synth )

        self._bpm = self.BPM_DEFAULT
        self._tpb = self.TPB_DEFAULT

    def __del__( self ):
        ''' Deletes the sequencer instance. '''
        self.handle.delete_fluid_sequencer( self.seq )

    def __delitem__( self, key ):
        ''' Cancels the registration of a FluidSynth object to this sequencer. '''
        id, name  = self[key]
        self.handle.fluid_sequencer_unregister_client( self.seq, id )

        super( FluidSequencer, self ).__delitem__( key )

    @property
    def beats_per_minute( self ):
        ''' Returns the current beats per minute. '''
        return self._bpm

    @beats_per_minute.setter
    def beats_per_minute( self, value ):
        ''' Sets the beats per minute. '''
        self._bpm = value
        self.__update_tps()

    @property
    def ticks_per_beat( self ):
        ''' Returns the current ticks per beat. '''
        return self._tpb

    @ticks_per_beat.setter
    def ticks_per_beat( self, value ):
        ''' Sets the ticks per beat. '''
        self._tpb = value
        self.__update_tps()

    @property
    def ticks_per_second( self ):
        ''' Returns the number of ticks per second. '''
        return self.handle.fluid_sequencer_get_time_scale( self.seq )

    @ticks_per_second.setter
    def ticks_per_second( self, value ):
        ''' Sets the number of ticks per second. '''
        self.handle.fluid_sequencer_set_time_scale( self.seq, value )

    @property
    def ticks( self ):
        ''' Returns the current tick. '''
        return self.handle.fluid_sequencer_get_tick( self.seq )

    def add_synth( self, synth ):
        ''' Register a FluidSynth object and return id and client name. '''
        id = self.handle.fluid_sequencer_register_fluidsynth( self.seq, synth.synth )
        name = self.handle.fluid_sequencer_get_client_name( self.seq, id )

        self[synth] = id, name

        return id, name

    def is_dest( self, id ):
        ''' Check if a client is a destination client. Returns true if is destination client else 
        false. '''
        result = self.handle.fluid_sequencer_client_is_dest( self.seq, id )
        return result == constants.TRUE
        
    def send( self, event, timestamp, absolute = True ):
        ''' Schedule an event for sending at a later time. Returns true if success else false. '''
        result = self.handle.fluid_sequencer_send_at( self.seq, event.event, timestamp, absolute )
        return result == constants.OK

    def send_right_now(self, event):
        ''' Send an event immediately. '''
        self.handle.fluid_sequencer_send_now( self.seq, event.event )
        
    def __update_tps( self ):
        ''' Update ticks per second based on ticks per beat and beats per minute. '''
        self.ticks_per_second = ( self._tpb * self._bpm ) / 60.0