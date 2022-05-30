import functools

# Python has a method with the necessary functionality (int.from_bytes())
# But since something needs to be implemented ...

def hex_to_little_endian(byte_sequense):
    '''Return a little endian value of the byte sequense'''
    # inverse the byte sequense
    inversed_sequense = bytes(reversed(byte_sequense))
    return bytes_to_int(inversed_sequense)


def hex_to_big_endian(byte_sequense):
    '''Return a big endian value of the byte sequense'''
    return bytes_to_int(byte_sequense)


# Helper functions

def bytes_to_int(byte_sequense):
    '''Return a value of the byte sequense'''
    # I use reduce(). It doesn't read very well, but it is written quickly.
    return functools.reduce(lambda x, y: x * 256 + y, byte_sequense, 0)


if __name__ == '__main__':
    print('Vector 1')
    hex_string = 'ff00000000000000000000000000000000000000000000000000000000000000'
    byte_sequence = bytes.fromhex(hex_string)
    print(f'Value: 0x{hex_string}')
    print(f'Little-endian: {hex_to_little_endian(byte_sequence)}')
    print(f'Big-endian: {hex_to_big_endian(byte_sequence)}')
    print()
    
    print('Vector 2')
    hex_string = 'aaaa000000000000000000000000000000000000000000000000000000000000'
    byte_sequence = bytes.fromhex(hex_string)
    print(f'Value: 0x{hex_string}')
    print(f'Little-endian: {hex_to_little_endian(byte_sequence)}')
    print(f'Big-endian: {hex_to_big_endian(byte_sequence)}')
    print()
    
    print('Vector 3')
    hex_string = 'FFFFFFFF'
    byte_sequence = bytes.fromhex(hex_string)
    print(f'Value: 0x{hex_string}')
    print(f'Little-endian: {hex_to_little_endian(byte_sequence)}')
    print(f'Big-endian: {hex_to_big_endian(byte_sequence)}')
    print()
    
    print('Vector 4')
    hex_string = 'F000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    byte_sequence = bytes.fromhex(hex_string)
    print(f'Value: 0x{hex_string}')
    print(f'Little-endian: {hex_to_little_endian(byte_sequence)}')
    print(f'Big-endian: {hex_to_big_endian(byte_sequence)}')
    print()
