import sys,codecs
N=sys.stdin.readline().rstrip()
def rot13(s):
    return ''.join([chr(x.islower() and ((ord(x) - 84) % 26) + 97
                        or x.isupper() and ((ord(x) - 52) % 26) + 65
                        or ord(x))
                    for x in s])
print(rot13(N))
