"""
Stack Implementation
"""


class Stack:

    def __init__(self):
        self.items = []  # initializes an empty array to store the items

    def push(self, item):
        """
        adds elements the top (end) of the stack (array)
        """
        self.items.append(item)

    def pop(self):
        """
        returns and removes the element at the top (end) of the stack (array)
        """
        if not self.is_empty():
            return self.items.pop()

    def get_stack(self) -> list:
        """
        returns the elements in the stack
        """
        return self.items

    def is_empty(self) -> bool:
        """
        checks if the stack is empty
        """
        return self.items == []

    def peek(self):
        """
        takes a look at the element at the top (end) of the stack (array), without removing it
        """
        if not self.is_empty():
            return self.items[-1]

    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return str(self.items)


def is_match(p1: str, p2: str) -> bool:
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_parenthesis_balanced(parenthesis: str) -> bool:
    """
    checks if a string of parenthesis is balance '{()}'
    """
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(parenthesis) and is_balanced:
        paren = parenthesis[index]

        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False

        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


def reverse_string(stack, input_str):

    for i in range(len(input_str)):
        stack.push(input_str[i])
        rev_str = ""

    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


def convert_int_to_bin(stack, dec_num):
    if dec_num == 0:
        return 0

    while dec_num > 0:
        remainder = dec_num % 2
        stack.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not stack.is_empty():
        bin_num += str(s.pop())

    return bin_num


if __name__ == "__main__":
    par = "[{()}]"

    print(is_parenthesis_balanced(par))

    s = Stack()

    print(reverse_string(s, "Hello"))
