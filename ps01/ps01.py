import secrets
import time
import itertools

def variants(length):
    '''Returns the number of variants of a bit sequence with length is "length"'''
    return 2 ** length


def how_long(key):
    '''Returns time in ms which needs to find the key'''
    start = time.time_ns()
    any(key == candidate for candidate in itertools.count())
    end = time.time_ns()
    return (end - start) // 1000000  # end and start in ns, but we need ms


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
    print()

    # Part 3. Finds keys and measures time
    print('Part 3, finds keys')
    print()
    # I measure time for 8, 16 and 32-bits keys
    # Attention! It can takes more then 3 min for finds 32 bit key.
    for length, key in itertools.islice(zip(key_lengths, keys), 3):
        print(f'For {length} bit key it takes {how_long(key)} ms')





