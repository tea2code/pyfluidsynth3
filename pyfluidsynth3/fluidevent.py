class FluidEvent():
    ''' Represents the FluidSynth event object as defined in event.h.
    
    This class is inspired by the FluidEvent object from pyfluidsynth by MostAwesomeDude. Method 
    documentation is mostly taken from FluidSynth's official API.

    Member:
    dest -- The destination field of a sequencer (short).
    event -- The FluidSynth event object (fluid_event_t).
    handle -- The handle to the FluidSynth library. Should be FluidHandle but a raw handle will 
              probably work, too (FluidHandle).
    source -- The source field of a sequencer (short).
    '''

    def __init__( self, handle ):
        ''' Create a new FluidSynth event instance using given handle object. '''
        self.handle = handle
        self.event = self.handle.new_fluid_event()
        self.source = -1
        self.dest = -1

    def __del__( self ):
        ''' Delete event instance. '''
        self.handle.delete_fluid_event( self.event )

    @property
    def source( self ):
        ''' Get the source field from a sequencer event structure. '''
        return self.handle.fluid_event_get_source( self.event )

    @source.setter
    def source( self, value ):
        ''' Set source of a sequencer event. '''
        self.handle.fluid_event_set_source( self.event, value )

    @property
    def dest( self ):
        ''' Get the destination field from a sequencer event structure. '''
        return self.handle.fluid_event_get_dest( self.event )

    @dest.setter
    def dest( self, value ):
        ''' Set destination of a sequencer event. '''
        self.handle.fluid_event_set_dest( self.event, value )

    def timer( self ):
        ''' Set a sequencer event to be a timer event. '''
        self.handle.fluid_event_timer( self.event, None )

    def volume( self, channel, value ):
        ''' Set a sequencer event to be a volume event. '''
        self.handle.fluid_event_volume( self.event, channel, value )

    def note( self, channel, key, velocity, duration ):
        ''' Set a sequencer event to be a note duration event. '''
        self.handle.fluid_event_note( self.event, channel, key, velocity, duration )

    def noteon( self, channel, key, velocity ):
        ''' Set a sequencer event to be a note on event. '''
        self.handle.fluid_event_noteon( self.event, channel, key, velocity )

    def noteoff( self, channel, key ):
        ''' Set a sequencer event to be a note off event. '''
        self.handle.fluid_event_noteoff( self.event, channel, key )

    def pitch_bend( self, channel, pitch ):
        ''' Set a sequencer event to be a pitch bend event. '''
        self.handle.fluid_event_pitch_bend( self.event, channel, pitch )

    def pitch_sens( self, channel, amount ):
        ''' Set a sequencer event to be a pitch wheel sensitivity event. An alias method 
        "pitch_wheelsens" exists. '''
        self.handle.fluid_event_pitch_wheelsens( self.event, channel, amount )
        
    pitch_wheelsens = pitch_sens

    def pc( self, a, b ):
        ''' Set a sequencer event to be a program change event. An alias method 
        "program_change" exists. '''
        self.handle.fluid_event_program_change( self.event, a, b )
        
    program_change = pc