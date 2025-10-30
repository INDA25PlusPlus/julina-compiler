
# Instructions

## Running the compiler

To compile a .julina file:
    paste 'python3 src/compiler.py src/examples/myprog.julina' in the terminal

To compile the default fibonacci example:
    'python3 src/compiler.py src/examples/fibonacci.julina'
    or simply 'python3 src/compiler.py'

The generated code will appear in:
    src/compiled_files


Optional: Add a custom filename of the output file, eg. 'python3 src/compiler.py src/examples/myprog.julina src/compiled_files/FILE_NAME.py'
(By default output filename is same as input file but with .py extension instead of .julina)

## Running the generated Python program

To compile fibonacci:
    python3 src/compiled/fibonacci.py
