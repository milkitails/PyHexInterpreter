import argparse
import os
import binascii
import random

parser = argparse.ArgumentParser(description='PyHexInterpreter')
parser.add_argument('file', type=str, help='.bin file')
args = parser.parse_args()

with open(args.file, "r") as file:
	path = os.environ.get("TEMP") + f"\\{random.randint(0, 872870)}.py"
	with open(path, "a") as sec_file:
		sec_file.write(binascii.unhexlify(file.read()).decode())

os.system(f"python {path}")
os.system(f"del {path}")