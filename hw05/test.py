def infinity(start):
    if start > 0:
        yield start
        yield from infinity(start - 1)

if __name__ == "__main__":
    t = infinity(10)
    for x in t:
        print(x) 