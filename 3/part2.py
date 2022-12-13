def main():
    f = open('inputs/input.txt', 'r')
    lines = [x.strip() for x in f.readlines()]
    letters = []
    for x in range(0, len(lines), 3):
        l1 = lines[x]
        l2 = lines[x + 1]
        l3 = lines[x + 2]
        commons = list(set(l1).intersection(l2))
        letters.append(list(set(commons).intersection(l3))[0])
    values = []
    for letter in letters:
        if letter.islower():
            values.append(ord(letter) - ord('a') + 1)
        else:
            values.append(ord(letter) - ord('A') + 27)
    print(sum(values))


if __name__ == '__main__':
    main()
