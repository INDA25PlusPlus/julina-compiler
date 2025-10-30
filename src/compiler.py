
import os
import sys
from tokenizer import tokenize
from parser import parse, print_parser_tree
from transpiler import generate_python

# Input file
if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = "src/examples/fibonacci.julina"

# Output file
if len(sys.argv) > 2:
    output_file = sys.argv[2]
else:
    # Default: same name as input, but .py in compiled folder
    base_name = os.path.basename(input_file).replace(".julina", ".py")
    output_file = os.path.join("src/compiled_files", base_name)

source_code = open(input_file).read()
tokens = tokenize(source_code)
ast_root = parse(tokens)
# print_parser_tree(ast_root, 0)

python_code = generate_python(ast_root)

with open(output_file, "w") as f:
    f.write(python_code)