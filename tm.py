import timeit


def first():
    data = b'\x20\x00\x3C\x06\xA0\x00\x46\x00\x00\x00\x00\x00\x00\x00\xED\x03\x00\x00\x89\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.hex()
    d = int(data[8], 16)
    v1 = int(data[12], 16)
    v2 = int(data[13], 16)
    return d, v1, v2

def second():
    data = b'\x20\x00\x3C\x06\xA0\x00\x46\x00\x00\x00\x00\x00\x00\x00\xED\x03\x00\x00\x89\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    d = int(format(data[4], 'x')[0], 16)
    v1 = int(format(data[6], 'x')[0], 16)
    v2 = int(format(data[6], 'x')[1], 16)
    return d, v1, v2

f = timeit.timeit(first, number=10000)
s = timeit.timeit(second, number=10000)

print(f, s)