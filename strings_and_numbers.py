def validate_int(cad):
    """Validates if a string has the format of an int.

    :param: cad: string to validate.
    :returns: Boolean
    """
    digit = 0
    result = True
    for i in cad:
        digit += 1
        if digit == 1 and i == '-':
            continue
        if i not in '0123456789':
            result = False
            break
    return result


def validate_float(cad):
    """Validates if a string has the format of a float.

    :param: cad: string to validate.
    :returns: Boolean
    """
    digit = 0
    has_period = False
    result = True
    for i in cad:
        digit += 1
        if digit == 1 and i == '-':
            continue
        if i == '.' and not has_period:
            has_period = True
            continue
        if i not in '0123456789':
            result = False
            break
    return result


def string_to_int(cad):
    """Converts a string to an integer.

    :param: cad: String to convert.
    :return: Integer
    """
    result = None
    digit = len(cad) - 1
    if validate_int(cad):
        result = 0
        position = 10 ** digit
        if cad[0] == '-':
            position = -1 * 10 ** digit
        for i in cad:
            if i == '1':
                result += 1 * position
            elif i == '2':
                result += 2 * position
            elif i == '3':
                result += 3 * position
            elif i == '4':
                result += 4 * position
            elif i == '5':
                result += 5 * position
            elif i == '6':
                result += 6 * position
            elif i == '7':
                result += 7 * position
            elif i == '8':
                result += 8 * position
            elif i == '9':
                result += 9 * position
            position //= 10
    return result


def string_to_float(cad):
    """Converts a string to a float.

    :param: cad: string to convert.
    :return: float
    """
    result = None
    if validate_float(cad):
        result = 0
        position = 1
        period_position = 0
        if cad[0] == '-':
            position = -1
        for i in cad:
            if i == '.':
                break
            period_position += 1
        position = position * 10 ** (len(cad) - 1)
        for i in cad:
            if i == '1':
                result += 1 * position
            elif i == '2':
                result += 2 * position
            elif i == '3':
                result += 3 * position
            elif i == '4':
                result += 4 * position
            elif i == '5':
                result += 5 * position
            elif i == '6':
                result += 6 * position
            elif i == '7':
                result += 7 * position
            elif i == '8':
                result += 8 * position
            elif i == '9':
                result += 9 * position
            elif i == '.':
                continue
            position /= 10
        if period_position > 0:
            result = result / (10 ** (len(cad) - period_position))
    return result


def round_num(num, decimal_places=2):
    """Rounds a float to the desired number of decimals.

    :param: num: Float to round.
    :param: decimal_places: Number of decimals to round. Default value = 2.
    :return: Float
    """
    factor = 10 ** (decimal_places + 1)
    print(f'The factor is {factor}')
    num = (num * factor + 5)//10
    print(f'The num is {num}')
    return num / (factor / 10)


def num_to_string(num, precision=14):
    """Converts any number into a String.

    :param: num: Int or float to convert.
    :param: precision: Number of decimals to maintain.
    :return: String
    """

    def conversion(current_digit, factor):
        if current_digit // factor == 9:
            return '9'
        elif current_digit // factor == 8:
            return '8'
        elif current_digit // factor == 7:
            return '7'
        elif current_digit // factor == 6:
            return '6'
        elif current_digit // factor == 5:
            return '5'
        elif current_digit // factor == 4:
            return '4'
        elif current_digit // factor == 3:
            return '3'
        elif current_digit // factor == 2:
            return '2'
        elif current_digit // factor == 1:
            return '1'
        elif current_digit // factor == 0:
            return '0'

    is_float = type(num) is float
    digits_flag = True
    divisor = decimal_place = 1
    counter = 0
    cad = ''
    if num < 0:
        cad = '-'
        num *= -1
    original_num = num

    while digits_flag:
        if num // divisor == 0:
            digits_flag = False
            divisor //= 10
        else:
            divisor *= 10
            counter += 1

    number_of_digits = counter
    if is_float:
        number_of_digits = counter + precision + 1
        decimal_place = num - num // 1

    for i in range(number_of_digits):

        if counter > 0:
            cad = cad + conversion(num, divisor)
            num = original_num % divisor
            if divisor != 1:
                divisor //= 10
            counter -= 1
        elif counter == 0:
            cad += '.'
            counter -= 1
        else:
            decimal_place *= 10
            decimal_place %= 10
            cad += conversion(decimal_place, 1)

    if is_float:
        while cad[len(cad)-1] == '0':
            cad = cad[0: len(cad) - 1]
            precision -= 1
        else:
            if cad[len(cad)-1] == '.':
                cad += '0'

        difference = original_num - abs(string_to_float(cad))
        while difference != 0:
            if difference > 0:
                if 4 < string_to_int(cad[len(cad) - 1]) < 9:
                    digit = str(int(cad[len(cad)-1]) + 1)
                    cad = cad[0:len(cad)-1] + digit
                elif string_to_int(cad[len(cad) - 1]) == 9:
                    cad = cad[0:len(cad) - 1]
                else:
                    digit = num_to_string(int(cad[len(cad) - 1]) + -1)
                    cad = cad[0:len(cad) - 1] + digit
            difference = original_num - string_to_float(cad)

    return cad


def validate_num_in_range(cad, maxim, minim=0):
    """Validates if the string contains a number in the strings is a valid number and if it's in the selected range.

    :param: cad: String containing the number.
    :param: maxim: Upper limit in the range (not included).
    :param: minim: Lower limit in the range (included, default value = 0).
    :return: Boolean
    """
    if validate_int(cad) and (minim <= string_to_int(cad) < maxim):
        return False
    if validate_float(cad) and (minim <= string_to_float(cad) < maxim):
        return True
    return False


def test():
    print('validate_int():')
    print(f'int 256: {validate_int("256")}')
    print(f'int -256: {validate_int("-256")}')
    print(f'int 25a6: {validate_int("25a6")}')
    print(f'int 25.6: {validate_int("25.6")}')
    print(f'int -25.6: {validate_int("-25.6")}')
    print(f'int 25-6: {validate_int("25-6")}')
    print('\nvalidate_float():')
    print(f'float 256: {validate_float("256")}')
    print(f'float 25.6: {validate_float("25.6")}')
    print(f'float -25.6: {validate_float("-25.6")}')
    print(f'float -25.6.256: {validate_float("-25.6.256")}')
    print(f'float .256: {validate_float(".256")}')
    print(f'float 25.a6: {validate_float("25.a6")}')
    print(f'float 25.6-74: {validate_float("25.6-74")}')
    print(f'float 25a.6: {validate_float("25a.6")}')
    print('\nstring_to_int():')
    print(f'int 256: {string_to_int("256")}')
    print(f'int 32768: {string_to_int("32768")}')
    print(f'int -256: {string_to_int("-256")}')
    print(f'int -32768: {string_to_int("-32768")}')
    print(f'int 25a6: {string_to_int("25a6")}')
    print('\nstring_to_float():')
    print(f'float 256: {string_to_float("256")}')
    print(f'float 25.6: {string_to_float("25.6")}')
    print(f'float 32.768: {string_to_float("32.768")}')
    print(f'float -25.6: {string_to_float("-25.6")}')
    print(f'float -32.768: {string_to_float("-32.768")}')
    print(f'float -32.7a68: {string_to_float("-32.7a68")}')
    print('\nnum_to_string():')
    print(f'int to string 256: {num_to_string(256)}')
    print(f'int to string 32768: {num_to_string(32768)}')
    print(f'int to string -256: {num_to_string(-256)}')
    print(f'int to string -32768: {num_to_string(-32768)}')
    print(f'float to string 25.6: {num_to_string(25.6)}')
    print(f'float to string 32.769: {num_to_string(32.769)}')
    print(f'float to string -25.6: {num_to_string(-25.6)}')
    print(f'float to string -32.767: {num_to_string(-32.767)}')
    print(f'float to string -32.0: {num_to_string(-32.0)}')
    print(f'float to string 17.000001: {num_to_string(17.000001)}')
    print(f'float to string 23.999995199999: {num_to_string(23.999995199999)}')


if __name__ == '__main__':
    test()
