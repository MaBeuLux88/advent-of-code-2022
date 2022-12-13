def main():
    f = open('inputs/input.txt', 'r')
    rps = [x.strip().split() for x in f.readlines()]
    score = 0
    for a, b in rps:
        if a == 'A':
            if b == 'X':
                score += 3
            elif b == 'Y':
                score += 6
        if a == 'B':
            if b == 'Y':
                score += 3
            elif b == 'Z':
                score += 6
        if a == 'C':
            if b == 'Z':
                score += 3
            elif b == 'X':
                score += 6
        if b == 'X':
            score += 1
        elif b == 'Y':
            score += 2
        else:
            score += 3
    print(score)


if __name__ == '__main__':
    main()
