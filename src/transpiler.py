# transpilerar mitt språk till Python baserat på syntaxträdet

def generate_python(ast_root):

    all_lines = []

    if ast_root.type == "program":
        ast_root = ast_root.children[0]

    for child in ast_root.children:
        result = generate_code(child, 0)
        all_lines.extend(result)

    return "\n".join(all_lines)




def gen_expr(node):

    if node.type == "variable" or node.type == "integer":
        return str(node.value)

    
    if node.type == "binop":
        op = node.value # +, -, <, > etc.
        # recursive
        left_text = gen_expr(node.children[0])
        right_text = gen_expr(node.children[1])

        return "(" + left_text + " " + op + " " + right_text + ")"

    


def generate_code(node, indent_level):
    
    lines = []
    indent = " "*(indent_level*4)

    if node.type == "block":
        for child in node.children:
            lines.extend(generate_code(child, indent_level+1))

    if node.type == "while":
        condition_node = node.children[0]
        block_node = node.children[1]

        condition = generate_code(condition_node, indent_level)
        while_block = generate_code(block_node, indent_level)

        lines.append(f"while {condition}:")
        lines.extend(while_block)

    
    if node.type == "binop":
        return gen_expr(node)

    if node.type == "assign":
       expression = gen_expr(node.children[0])
       lines.append(f"{indent}{node.value} = {expression}")


    if node.type == "write":
        lines.append(f"{indent}print({str(node.children[0].value)})")


    return lines