import sys

def seq():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(1, N + 1):
        if i not in s:
            s.append(i)
            seq()
            s.pop()
        
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    s = []

    seq()