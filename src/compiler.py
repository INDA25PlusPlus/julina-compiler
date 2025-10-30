
import os
from tokenizer import tokenize
from parser import parse, print_parser_tree
from transpiler import generate_python


source_code = open("src/examples/fibonacci.julina").read()
tokens = tokenize(source_code)
ast_root = parse(tokens)
print_parser_tree(ast_root, 0)

python_code = generate_python(ast_root)

with open("src/compiled/fibonacci.py", "w") as f:
    f.write(python_code)