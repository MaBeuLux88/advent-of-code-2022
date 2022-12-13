def main():
    f = open('inputs/input.txt', 'r')
    calories = [x.strip() for x in f.readlines()]
    sum_calories = []
    cals = 0
    for c in calories:
        if c == '':
            sum_calories.append(cals)
            cals = 0
        else:
            cals += int(c)
    sum_calories.append(cals)
    print(max(sum_calories))


if __name__ == '__main__':
    main()
