def counts_one_bit(x: int) -> int:
    counts = 0
    while x: # only false when x = 0
        counts += x & 1 # mask with & to extract only 1 the first bit
        x >>= 1 # shift to right 1 bit

    return counts

# return 1 if number of 1 bit is odd, else 0
def parity(x: int) -> int:
    parity = 0
    while x:
        # if the LSB is 1, flip parity, else do nothing
        # in details:
        # - parity = 0, lsb = 0 -> 0
        # - parity = 0, lsb = 1 -> 1
        # - parity = 1, lsb = 0 -> 1
        # - parity = 1, lsb = 1 -> 0
        parity ^= x & 1
        X >> 1

def lowest_bit_set(x: int) -> int:
    # lowest bit set is a set of bit
    # starting (from the left ofc) with a series of 0 
    # and end with the first one bit
    # e.g. LBS of 0b1010100 is 0b100

    # 1. first we flip the bit (take one's complement)
    # then [1, series of 0] become [0, series of 1]
    # 2. we add 1 to cancel out series of 1
    # notice that the carry stop at the [0] bit beautifully
    # 3. take & with the original word to extract the LBS

    # step 1 and 2 is just to get to two's complement/the negative value
    return x & -x

# parity and counts_one_bit both as O(n) complexity
# using lowest_bit_set as a help, we can do it with 0(k), as k is the number of one-bits
def partity_k(x: int) -> int:
    parity = 0
    while x:
        parity ^= 1
        # x & x-1 is x with lowest_bit_set set to 0 
        # (e.g. x = 0b1100, x-1 = 0b1011, x & x - 1 = ya see what's happening here, such magic :) )
        # ~ we erasing one one-bit at the time, 
        # starting from the least significant one-bit
        x = x & (x-1)

    return parity

# try to understand that algorithm on page 28

print(partity_k(24))
print(bin(24))
