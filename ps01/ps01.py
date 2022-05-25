def variants(length):
    '''Returns the number of variants of a bit sequence with length is "length"'''
    return 2 ** length


if __name__ == '__main__':
    key_lengths = [8, 16, 32, 64, 128, 256, 512, 1024, 4069]
    print('Part 1')
    print()
    for length in key_lengths:
        print(f'For {length} bit key we have {variants(length)} possible keys.')


