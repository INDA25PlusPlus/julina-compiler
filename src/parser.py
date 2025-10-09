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
    pass

    def recursion():
        pass