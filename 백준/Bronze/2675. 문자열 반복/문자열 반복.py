import sys

T = int(sys.stdin.readline())

for _ in range(T):
    R, S = map(str, sys.stdin.readline().split())
    R = int(R)
    seq = ''
    
    for i in S:
        seq += i * R

    print(seq)