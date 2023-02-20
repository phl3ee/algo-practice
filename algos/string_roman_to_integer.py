def romanToInt(s: str) -> int:

    print("Converting",s,"to numeral..")
    result = 0

    #mapping dictionary for numeral to integer values
    NumeralToInt = {
        "I"  : 1,
        "V"  : 5,
        "X"  : 10,
        "L"  : 50,
        "C"  : 100,
        "D"  : 500,
        "M"  : 1000
    }

    #mapping for exceptions/subtractions
    NumeralExceptions = {
        "IV" : 2,
        "IX" : 2,
        "XL" : 20,
        "XC" : 20,
        "CD" : 200,
        "CM" : 200
    }

    #sum all integer values
    for numeral in s:
        result = result + NumeralToInt[numeral]

    print("Result pre matchReduce is: ",result)
    #reduce by any exception matches
    for exception in NumeralExceptions.keys():
        if s.find(exception) > -1:
            print(exception)
            result = result - NumeralExceptions[exception]

    return result

print(romanToInt('III'))
print(romanToInt('IV'))
print(romanToInt('IX'))
print(romanToInt('XL'))
print(romanToInt('XC'))
print(romanToInt('CD'))
print(romanToInt('CM'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))
