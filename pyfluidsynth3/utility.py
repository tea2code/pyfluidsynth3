def fluidstring( string ):
    ''' Converts a Python string to a FluidSynth compatible string. '''
    ENCODING = 'utf-8'
    return string.encode( ENCODING )