import argparse
import os
import binascii
import random

parser = argparse.ArgumentParser(description='PyHexInterpreter')
parser.add_argument('file', type=str, help='.bin file')
args = parser.parse_args()

with open(args.file, "r", encoding="utf-8") as file:
	path = os.environ.get("TEMP") + f"\\{random.randint(0, 872870)}.py"
	with open(path, "a", encoding="utf-8") as sec_file:
		sec_file.write(binascii.unhexlify(file.read()).decode())

os.system(f"{os.environ.get('APPDATA')}\\python_310\\python.exe {path}")
os.system(f"del {path}")