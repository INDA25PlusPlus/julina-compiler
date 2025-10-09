
keywords = ["while", "write", "if"]


def is_letter(c: str):
    return ord("a") <= ord(c) <= ord("z") or ord("A") <= ord(c) <= ord("Z")

def is_digit(c: str):
    return c.isnumeric()

def is_character(c: str):
    return is_letter(c) or is_digit(c) or c == "_"
  
def is_operation(c: str):
    return c == "+" or c == "-"



def tokenize(program: str):

    tokens = []
    program = program.replace(" ", "")

    i = 0
    while i < len(program):
        c = program[i]

        # Keywords or identifiers
        if is_letter(c):
            start = i
            while i < len(program) and is_character(program[i]):
                i += 1
            word = program[start:i]
            if word in keywords:
                tokens.append(("keyword", word))
            else:
                tokens.append(("identifier", word))
            continue

        # Numbers
        elif is_digit(c):
            start = i
            while i < len(program) and is_digit(program[i]):
                i += 1
            tokens.append(("integer", program[start:i]))
            continue

        # Operators and symbols
        elif c in "+-=;(){}<>":
            tokens.append(("symbol", c))
            i += 1
            continue

        # Logical operators
        elif c in "&|=":
            if i + 1 < len(program) and program[i + 1] == c: 
                tokens.append(("symbol", c + c))
                i += 2
            continue
        elif c in "<>":
            tokens.append(("symbol", c))
            i += 1
            continue

        else:
            print(f"Invalid character!!: {c}")
            exit(1)

    return tokens

