def main():
    f = open('inputs/input.txt', 'r')
    rps = [x.strip().split() for x in f.readlines()]
    score = 0
    for i in range(len(rps)):
        a, b = rps[i]
        if a == 'A':
            if b == 'X':
                score += 3
            elif b == 'Y':
                score += 1
            else:
                score += 2
        if a == 'B':
            if b == 'Y':
                score += 2
            elif b == 'Z':
                score += 3
            else:
                score += 1
        if a == 'C':
            if b == 'Z':
                score += 1
            elif b == 'X':
                score += 2
            else:
                score += 3
        if b == 'Y':
            score += 3
        elif b == 'Z':
            score += 6
    print(score)


if __name__ == '__main__':
    main()
