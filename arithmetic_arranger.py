def arithmetic_arranger(problems, response=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    for i in problems:
        if i.find("+") == -1 and i.find("-") == -1:
            return "Error: Operator must be '+' or '-'."
    for i in problems:
        if i.find("+") != -1:
            numbers = i.split("+")
        else:
            numbers = i.split("-")
        for y in numbers:
            y = y.rsplit()[0]
            for d in y:
                if not d.isdigit():
                    return "Error: Numbers must only contain digits."
            if len(y) > 4:
                return "Error: Numbers cannot be more than four digits."

    first_line = ""
    second_line = ""
    third_line = ""
    four_line = ""
    first_or = 0
    for i in problems:
        longest = 0
        the_longest = 0

        if i.find("+") != -1:
            numbers = i.split("+")
            sign = "+"
        else:
            numbers = i.split("-")
            sign = "-"
        for y in numbers:
            if int(y) > int(longest):
                the_longest += 1
                longest = y.rsplit()[0]
        numbers[0] = numbers[0].rsplit()[0]
        numbers[1] = numbers[1].rsplit()[0]

        if response is True:
            if sign == "+":
                result = int(numbers[0]) + int(numbers[1])
            else:
                result = int(numbers[0]) - int(numbers[1])

        if the_longest == 1:
            numbers[1] = sign + " " * (len(numbers[0]) - len(numbers[1]) + 1) + numbers[1]
            numbers[0] = "  " + numbers[0]
        else:
            numbers[0] = " " * (len(numbers[1]) - len(numbers[0]) + 2) + numbers[0]
            numbers[1] = sign + " " + numbers[1]

        if first_or == 1:
            numbers[0] = "    " + numbers[0]
            numbers[1] = "    " + numbers[1]
            third_line = third_line + "    "
            if response is True:
                four_line += "    "

        if response is True:
            four_line += " " * ((len(longest) + 2) - len(str(result))) + str(int(result))

        first_line = first_line + numbers[0]
        second_line = second_line + numbers[1]
        third_line = third_line + ("-" * (len(longest) + 2))

        first_or = 1

    arranged_problems = first_line + "\n" + second_line + "\n" + third_line
    if response is True:
        arranged_problems += "\n" + four_line

    return arranged_problems
