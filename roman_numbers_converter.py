def to_roman(n):
    nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    symbols = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i, result = 12, ''

    while n:
        div = n // nums[i]
        n %= nums[i]
        while div:
            result += symbols[i]
            div -= 1
        i -= 1

    return result


def from_roman(r_num):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
              'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    i, result = 0, 0
    
    while i < len(r_num):
        if i + 1 < len(r_num) and r_num[i:i+2] in romans:
            result += romans[r_num[i:i+2]]
            i += 2
        else:
            result += romans[r_num[i]]
            i += 1
            
    return result

while True:
    to_conv = input('Enter roman or arabic number: ')

    if to_conv.isalpha():
        try:
            print(from_roman(to_conv.upper()))
        except:
            print('Error: Wrong characters in roman number')
    elif to_conv.isdigit():
        try:
            print(to_roman(int(to_conv)))
        except:
            print('Error: Numbers not right...')
    else:
        print('Error: unconvertable value')

    cmd = input("Press ENTER to try again... ")
    if cmd:
        quit()
