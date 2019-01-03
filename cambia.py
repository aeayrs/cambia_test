import argparse
import os
from pathlib import Path
def parse_input_file(input_filename):
    parsed_data = []
    working_dir = os.getcwd()
    if not input_filename.startswith('/'):
        input_filename = os.path.join(working_dir, input_filename)

    input_file = Path(input_filename)
    if input_file.is_file():
        with open(input_filename, 'r') as in_file:
            in_line = in_file.readline()
        in_file.close()
        print("in_line='%s'" % in_line)
        parsed_data = in_line.rstrip().split(',')
        parsed_data = [x.strip() for x in parsed_data]
    return parsed_data

def main():
    input_file=""
    output_file=""
    parsed_data=[]
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', action="store", dest="input_file", default="input.csv")
    parser.add_argument('--output_file', action="store", dest="output_file", default="output.csv")
    input_file=parser.parse_args().input_file
    output_file=parser.parse_args().output_file
    parsed_data = parse_input_file(input_file)
    print(parsed_data)

if __name__ == '__main__':
    main()
