import sys


def txt_importer(path_file):
    if ".txt" not in path_file:
        sys.stderr.write(f"Formato inválido\n")

    try:
        with open(path_file, "r", encoding="utf-8") as file:
            text_file = file.read().splitlines()
            return text_file

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

# Ref: https://docs.python.org/3/library/stdtypes.html#functions splitlines()
# Ref: https://www.askpython.com/python/python-stdin-stdout-stderr
