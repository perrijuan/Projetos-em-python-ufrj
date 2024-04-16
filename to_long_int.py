#implementação da f(x) da biblioteca crypto....

def long_to_bytes(n):
    l = []
    x = 0
    off = 0
    while x != n:
        b = (n >> off) & 0xFF
        l.append( b )
        x = x | (b << off)
        off += 8
    l.reverse()
    return bytes(l)

def bytes_to_long(s):
    n = s[0]
    for b in (x for x in s[1:]):
        n = (n << 8) | b
    return n
