def to_number(roman):
    numbers = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000,
               "V'": 5000}
    total = 0

    for i in range(len(roman)):
        if i > 0 and numbers[roman[i]] > numbers[roman[i - 1]]:
            total += numbers[roman[i]] - 2 * numbers[roman[i - 1]]
        else:
            total += numbers[roman[i]]
    return total


print(to_number("MCMVII"))
print(to_number("MMXI"))
print(to_number("XC"))
print(to_number("MCMXC"))

print("\n")

def to_roman1(sayilar):
    degerler = [
        5000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
    ]
    harfler = [
        "V'", "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
    ]
    roman = ""
    for i in range(len(degerler)):
        while sayilar >= degerler[i]:
            roman += harfler[i]
            sayilar -= degerler[i]

    return roman


print(to_roman1(178))
print(to_roman1(42))
print(to_roman1(5654))
print(to_roman1(1903))
