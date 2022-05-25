import secrets

def variants(length):
    '''Returns the number of variants of a bit sequence with length is "length"'''
    return 2 ** length


if __name__ == '__main__':
    key_lengths = [8, 16, 32, 64, 128, 256, 512, 1024, 4069]
    # Part 1. Variants of keys.
    print('Part 1')
    print()
    for length in key_lengths:
        print(f'For {length} bit key we have {variants(length)} possible keys.')
    print()
    # Part 2. Random keys
    print('Part 2')
    print()
    keys = [secrets.randbits(length) for length in key_lengths]
    for length, key in zip(key_lengths, keys):
        print(f'{length} bit key is {key}')


