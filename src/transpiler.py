# transpilerar mitt språk till Python baserat på syntaxträdet

def generate_python(ast_root):

    all_lines = []

    for child in ast_root.children:
        result = generate_code(child, 0)
        all_lines.append(result)

    # returnera alla rader sammanslagna till en enda text (separerade med \n)

def generate_code(node, indent_level):
    
    lines = []
    indent = " "*(indent_level*4)

    if node.type == "block":
        for child in node.children:
            generate_code(child, indent_level)

    if node.type == "while":
        pass

    if node.type == "assign":
        pass

    if node.type == "write":
        pass



    for child in node.children:
        generate_code(child, indent_level+5)
