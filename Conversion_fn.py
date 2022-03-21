def romantoint(roman):
    """This function uses the concept of converting roman numerals to add the roman equivalent
    if the bigger one comes first  and subtracting if the smaller comes first"""

    int_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    int_value = 0
    l_roman = len(roman)
    for i in range(l_roman - 1):
        left = roman[i]
        right = roman[i + 1]
        if int_roman[left] < int_roman[right]:
            int_value -= int_roman[left]
        else:
            int_value += int_roman[left]
    int_value += int_roman[roman[-1]]  # adds the value of the last character in case of an odd length
    return int_value


def inttoroman(num):
    """
    THIS FUNCTION CONVERTS INTEGERS TO ROMAN NUMERALS
    USING A DICTIONARY CONTAINING THE 13 FUNDAMENTAL ROMAN NUMERAL EQUIVALENCE
    AND A LIST CONTAINING THE KEYS IN ORDER
    """

    int_roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
                 50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
    ordered_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    roman_numeral = ''
    if num == 0 or num >= 3999:  # set limit for integer input
        print('Limit exceeded!')

    else:
        for i in ordered_list:
            if num != 0:
                quotient = num // i
                if quotient != 0:  # outputs the roman numerals if the quotient is not zero
                    for x in range(quotient):
                        roman_numeral += int_roman[i]

            num = num % i  # get remainder for next iteration
    return roman_numeral
