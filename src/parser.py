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
    

    def parse_expression():
        pass

    def parse_assignment():
        pass

    def parse_write():
        pass

    def parse_while():
        pass

    def parse_compound_statement():
        pass


    root = Node("program")
    root.add_child(parse_compound_statement())

    return root