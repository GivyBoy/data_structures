"""
String Algorithms
"""

"Problem 1: Look-and-Say Sequence"


def next_number(num: str) -> str:
    result = []
    i = 0
    while i < len(num):
        count = 1
        while i + 1 < len(num) and num[i] == num[i + 1]:
            i += 1
            count += 1
        result.append(str(count) + num[i])
        i += 1
    return ''.join(result)


"""
Problem 2: Spreadsheet Encoding
"""


def spreadsheet_encodeColumn(col: str) -> int:
    num = 0
    count = 0
    for i in reversed(range(len(col))):
        num += (26 ** count) * (ord(col[i]) - ord('A') + 1)
        count += 1

    return num


"""
Problem 3: is Palindrome
"""


# this implementation is not perfect! It looks pretty, but it needs `len(input) % 2 == 0`
def is_palindrome(words: str) -> bool:
    for i in range(len(words)):
        if words[i].isalnum() and words[~i].isalnum():
            if words[i].lower() != words[~i].lower():
                return False

    return True


s = "Was it a cat I saw"  # doesn't work with "Was it a cat I saw?"

"Better implementation - works all the time! Uses Two Pointer method"


def isPalindrome(words: str) -> bool:
    left = 0
    right = len(words) - 1

    while left < right:

        while not words[left].isalnum() and left < right:
            left += 1
        while not words[right].isalnum() and left < right:
            right -= 1

        if words[left].lower() != words[right].lower():
            return False

        left += 1
        right -= 1

    return True


"""
Problem 4: Is Anagram
"""


def is_anagram(words1: str, words2: str) -> bool:
    words1 = words1.replace(" ", "").lower()  # normalize string
    words2 = words2.replace(" ", "").lower()  # normalize string

    letters = dict()

    if len(words1) != len(words2):
        return False

    for i in words1:

        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1

    for j in words2:

        if j in letters:
            letters[j] -= 1
        else:
            letters[j] = 1

    for k in letters:
        if letters[k] != 0:
            return False

    return True


"""
Problem 5: Is Palindrome Permutation
"""


def is_palindromePermutation(input_str: str) -> bool:
    input_str = input_str.replace(" ", "").lower()  # normalizes the string
    letters = dict()

    for i in input_str:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1

    odd = 0
    for key, val in letters.items():
        if val % 2 != 0 and odd == 0:
            odd += 1
        elif val % 2 != 0 and odd != 0:
            return False
    return True


"""
Problem 6: Is Permutation
"""


def is_permutation(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False

    string1 = string1.lower()
    string2 = string2.lower()

    letters = dict()

    for i in string1:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    for j in string2:
        if j in letters:
            letters[j] -= 1
        else:
            return False

    return all(value == 0 for value in letters.values())


"""
Problem 7: Is Unique - are all the letters in a word unique?
"""


def is_unique(input_str: str) -> bool:

    input_str = input_str.lower()
    letters = dict()

    for i in input_str:

        if i in letters:
            return False
        else:
            letters[i] = 1

    return True


"""
Problem 8 - Integer to String
"""


def int_to_str(input_int):
    if input_int < 0:
        is_negative = True
        input_int *= -1
    else:
        is_negative = False

    output_str = []

    if input_int == 0:
        output_str.append('0')
    else:
        while input_int > 0:
            output_str.append(chr(ord('0') + input_int % 10))
            input_int //= 10
        output_str = output_str[::-1]

    output_str = ''.join(output_str)

    if is_negative:
        return '-' + output_str
    else:
        return output_str


"""
Problem 9: String to Integer
"""


def str_to_int(input_str):

    output_int = 0

    if input_str[0] == '-':
        start_idx = 1
        is_negative = True
    else:
        start_idx = 0
        is_negative = False

    for i in range(start_idx, len(input_str)):
        place = 10**(len(input_str) - (i+1))
        digit = ord(input_str[i]) - ord('0')
        output_int += place * digit

    if is_negative:
        return -1 * output_int
    else:
        return output_int

