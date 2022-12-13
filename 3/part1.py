def main():
    f = open('inputs/input.txt', 'r')
    lines = [x.strip() for x in f.readlines()]
    lines_split = []
    letters = []
    for i in lines:
        a = ''.join(sorted(i[0:len(i) // 2]))
        b = ''.join(sorted(i[len(i) // 2:]))
        lines_split.append((a, b))
    for a, b in lines_split:
        letters.append(list(set(a).intersection(b))[0])
    values = []
    for letter in letters:
        if letter.islower():
            values.append(ord(letter) - ord('a') + 1)
        else:
            values.append(ord(letter) - ord('A') + 27)
    print(sum(values))


if __name__ == '__main__':
    main()
