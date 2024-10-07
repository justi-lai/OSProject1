import sys

memloc = 0

mode = input().strip()
# mode = sys.stdin.readline().rstrip()

while mode != "halt":
    if mode == "read":
        print(memloc)
        sys.stdout.flush()
    elif mode == "write":
        memloc = int(sys.stdin.readline().rstrip())
    mode = input().strip()
    # mode = sys.stdin.readline().rstrip()
