def rechner(n: int, d: int, a: list[int]):
    lst = []
    for x in range(len(a)):
        element = chr(a[x] ** d % n)
        lst.append(element)
    final = "".join(lst)
    print(final)

if __name__ == "__main__":
    rechner(559, 101, [553, 182, 544, 29, 553, 544, 553, 29, 553, 389])