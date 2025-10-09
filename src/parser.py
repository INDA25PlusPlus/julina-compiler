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

        tok = peek()
        if not tok:
            raise SyntaxError("Expected end of input")
        if expected_type and tok[0] != expected_type:
            raise SyntaxError(f"Expected type: {expected_type}, got type: {tok[0]}")
        if expected_val and tok[1] != expected_val:
            raise SyntaxError(f"Expected value: {expected_val}, got value: {tok[1]}")

        token_idx += 1

    def parse_expression(): # <expression> ::= <term> <operation> <expression> | <term>
        parse_term()
        

    def parse_term():
        token_type, token_val = peek()
        
        if token_type == "integer":
            consume("integer")
            return Node(token_type, token_val)
        elif token_type == "variable":
            consume("variable")
            return Node(token_type, token_val)
        else:
            print(f"Unexpected token???: {token_type} {token_val}")

    def parse_assignment():
        pass

    def parse_if(): # <if-statement> ::= "if" "(" <condition> ")" "{" <compound-statement> "}"
        consume("condition", "if")
        consume("symbol", "(")
        condition = parse_expression()
        consume("symbol", ")")
        consume("symbol", "{")
        compund_statement = parse_compound_statement()
        consume("}")
        node = Node("if")
        node.add_child(condition)
        node.add_child(compund_statement)
        return node

    def parse_write():
        pass

    def parse_while():
        pass

    def parse_compound_statement():

        block = Node("Block")

        while True:

            token_type, token_val = peek()

            if token_type == "loop":
                if token_val == "while":
                    statement = parse_while()

            elif token_type == "output":
                if token_val == "write":
                    statement = parse_write()

            elif token_type == "condition": 
                if token_val == "if": 
                    statement = parse_if()

            block.add_child(statement)



    root = Node("program")
    root.add_child(parse_compound_statement())

    return root