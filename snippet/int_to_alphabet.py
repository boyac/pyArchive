FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"
THOUSAND = "thousand"

def int_to_alphabet(number):
    words = []
    if number > 0:
        if number >= 1000:
            n = int(number / 1000)
            words.extend((FIRST_TEN[n-1], THOUSAND))
            number %= 1000
        if number >= 100:
            n = int(number / 100)
            words.extend((FIRST_TEN[n-1], HUNDRED))
            number %= 100
        if 20 <= number:
            words.append(OTHER_TENS[int(number / 10) - 2])
            number %= 10
        if 10 <= number <= 19:
            words.append(SECOND_TEN[number-10])
            number = 0
        if 0 < number:
            words.append(FIRST_TEN[(number)-1])

        return " ".join(words)

    elif number < 0:
        if abs(number) >= 1000:
            n = int(abs(number) / 1000)
            words.extend((FIRST_TEN[n-1], THOUSAND))
            number %= 1000
        if abs(number) >= 100:
            n = int(abs(number) / 100)
            words.extend((FIRST_TEN[n-1], HUNDRED))
            number %= 100
        if 20 <= abs(number):
            words.append(OTHER_TENS[int(abs(number) / 10) - 2])
            number %= 10
        if 10 <= abs(number) <= 19:
            words.append(SECOND_TEN[abs(number)-10])
            number = 0
        if 0 < abs(number):
            words.append(FIRST_TEN[abs(number)-1])

        return "negative " + " ".join(words)


lst = [0, 9, 11, 21, 30, 100, 1000, -9, -11, -21, -30, -100, -1000] # bugs at value -21, got no idea why
for i in lst:
    print int_to_alphabet(i)
