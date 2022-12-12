def main():
    f = open('inputs/input.txt', 'r')
    calories = [x.strip() for x in f.readlines()]
    sum_calories = []
    cals = 0
    for c in range(len(calories)):
        cal = calories[c]
        if cal == '':
            sum_calories.append(cals)
            cals = 0
        else:
            cals += int(calories[c])
    sum_calories.append(cals)
    print(sum(sorted(sum_calories, reverse=True)[0:3]))


if __name__ == '__main__':
    main()
