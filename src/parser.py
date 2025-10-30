from tokenizer import tokenize

class Node:
    def __init__(self, type_, value=None):
        self.type = type_    
        self.value = value      
        self.children = []       
        self.parent = None      

    def add_child(self, child):
        if child:
            self.children.append(child)
            child.parent = self 

    def __repr__(self):
        return f"Node({self.type!r}, {self.value!r})"



def parse(tokens):
    token_idx = 0

    def peek():
        return tokens[token_idx] if token_idx < len(tokens) else None
    
    def consume(expected_type=None, expected_val=None):
        nonlocal token_idx
        tok = peek()
        if not tok:
            raise SyntaxError("Expected end of input")
        if expected_type and tok[0] != expected_type:
            print(tok)
            raise SyntaxError(f"Expected type: {expected_type}, got type: {tok[0]}")
        if expected_val and tok[1] != expected_val:
            raise SyntaxError(f"Expected value: {expected_val}, got value: {tok[1]}")

        token_idx += 1
        return tok

    def parse_expression(): # <expression> ::= <term> <operation> <expression> | <term>, assumes a + b + c = (a + b) + c
        node = parse_term()
        
        while True:
            token_type, token_val = peek()
            if token_type == "binop" and token_val in ["+", "-"]:
                consume("binop")
                binop_node = Node("binop", token_val)
                left_child = node
                right_child = parse_term()

                binop_node.add_child(left_child)
                binop_node.add_child(right_child)

                node = binop_node 
            else:
                break

        return node
        

    def parse_term(): # <term> ::= <integer> | <identifier> 
        token_type, token_val = peek()
        
        if token_type == "integer":
            consume("integer")
            return Node(token_type, token_val)
        elif token_type == "variable":
            consume("variable")
            return Node(token_type, token_val)
        else:
            print(f"Unexpected token???: {token_type} {token_val}")

    def parse_assignment(): # <assignment> ::= <identifier> "=" <expression> ";"
        var_token = consume("variable")
        consume("assignment", "ar")
        assign_to = parse_expression()
        consume("symbol", ";")
        node = Node("assign", var_token[1])
        node.add_child(assign_to)
        return node

    def parse_if(): # <if-statement> ::= "if" "(" <condition> ")" "{" <compound-statement> "}"
        consume("condition", "om")
        consume("symbol", "(")
        condition = parse_expression()
        consume("symbol", ")")
        consume("symbol", "{")
        compound_statement = parse_compound_statement()
        consume("}")
        node = Node("if")
        node.add_child(condition)
        node.add_child(compound_statement)
        return node

    def parse_write(): # <write> ::= "write" "(" <expression> ")" ";"
        consume("output", "skriv")
        consume("symbol", "(")
        expression = parse_expression()
        consume("symbol", ")")
        consume("symbol", ";")
        node = Node("write")
        node.add_child(expression)
        return node
    
    def parse_condition(): # <condition> ::= <expression> <comparison-operation> <expression> | <expression> <comparsison-operation> <condition> 
        node = parse_expression()

        # assumes a < b < c = (a < b) < c

        while True:
            token_type, token_val = peek()
            if token_type == "binop" and token_val in ["samre", "battre", "||", "&&", "=="]:
                consume("binop")
                if token_val == "samre":
                    binop_node = Node("binop", "<")
                elif token_val == "battre":
                    binop_node = Node("binop", ">")
                else:
                    binop_node = Node("binop", token_val)
                left_child = node
                right_child = parse_expression()
                binop_node.add_child(left_child)
                binop_node.add_child(right_child)

                node = binop_node

            else:
                break
        
        return node

    def parse_while(): # <while-loop> ::= "while" "(" <condition> ")" "{" <compound-statement> "}"
        consume("loop", "medan")
        consume("symbol", "(")
        condition = parse_condition()
        consume("symbol", ")")
        consume("symbol", "{")
        compound_statement = parse_compound_statement()
        consume("symbol", "}")
        node = Node("while")
        node.add_child(condition)
        node.add_child(compound_statement)
        return node


    def parse_compound_statement(): # <compound-statement> ::= <statement> | <statement> <compound-statement>

        block = Node("block")

        while True:

            if peek() == None:
                break

            token_type, token_val = peek()
            
            if token_type == "loop":
                if token_val == "medan":
                    statement = parse_while()

            elif token_type == "output":
                if token_val == "skriv":
                    statement = parse_write()

            elif token_type == "condition": 
                if token_val == "om": 
                    statement = parse_if()

            elif token_type == "variable":
                statement = parse_assignment()

            elif token_type == "symbol":
                if token_val == "}": # end of loop
                    break


            else:
                raise SyntaxError (f"UNEXPECTED TOKEN: {token_type} {token_val}")

            block.add_child(statement)

        return block

    root = Node("program")
    root.add_child(parse_compound_statement())

    return root



# program = """
#         prev1 ar 0;
#         prev2 ar 1;
#         cur ar 1;
#         i ar 0;

#         skriv(prev1);
#         skriv(prev2);

#         medan (i samre 50) {

#             cur ar prev1 + prev2;
#             prev1 ar prev2;
#             prev2 ar cur;
#             i ar i + 1;
#             skriv(cur);
#         }
#         """

# tokens = tokenize(program)
# print(tokens)
# root = parse(tokens)


def print_parser_tree(node, indent):
    if node.value != None:
        print(f"{' '*indent} {node.type} {node.value}")
    else:
        print(f"{' '*indent} {node.type}")
    for child in node.children:
        print_parser_tree(child, indent+3)

#print_parser_tree(root, 0)