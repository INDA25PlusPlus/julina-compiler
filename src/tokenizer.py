
keywords = {"while": "loop", "write": "output", "if": "condition"}


def is_letter(c: str):
    return ord("a") <= ord(c) <= ord("z") or ord("A") <= ord(c) <= ord("Z")

def is_digit(c: str):
    return c.isnumeric()

def is_character(c: str):
    return is_letter(c) or is_digit(c) or c == "_"
  

def tokenize(program: str):

    tokens = []
    #program = program.replace(" ", "")
    print(program)

    i = 0
    while i < len(program):
        c = program[i]

        if c.isspace(): 
            i += 1
            continue

        # Keywords or identifiers
        if is_letter(c):
            start = i
            while i < len(program) and is_character(program[i]):
                i += 1
            word = program[start:i]
            if word in keywords:
                tokens.append((keywords[word], word))
            else:
                tokens.append(("variable", word))
            continue

        # Numbers
        elif is_digit(c):
            start = i
            while i < len(program) and is_digit(program[i]):
                i += 1
            tokens.append(("integer", program[start:i]))
            continue

        
        # Assign
        elif c == "=":
            tokens.append(("assign", c))
            i += 1
            continue
        
        # Operators and symbols
        elif c in "+-<>":
            tokens.append(("binop", c))
            i += 1
            continue
        
        elif c in ";(){}":
            tokens.append(("symbol", c))
            i += 1
            continue


        # Logical operators
        elif c in "&|=":
            if i + 1 < len(program) and program[i + 1] == c: 
                tokens.append(("binop", c + c))
                i += 2
            continue

        else:
            print(f"Invalid character!!: {c}")
            exit(1)

    return tokens



# print(tokenize('a = 2 + 3; while (a < 10) { write(a); a = a + 1;}'))