import argparse
import os
from pathlib import Path
def parse_input_file(input_filename, verbose):
    parsed_data = []
    working_dir = os.getcwd()
    if not input_filename.startswith('/'):
        input_filename = os.path.join(working_dir, input_filename)

    input_file = Path(input_filename)
    if input_file.is_file():
        with open(input_filename, 'r') as in_file:
            in_line = in_file.readline()
        in_file.close()
        if verbose:
            print("in_line='%s'" % in_line)
        parsed_data = in_line.rstrip().split(',')
        parsed_data = [x.strip() for x in parsed_data]
        processed_parsed_data = []
        for data_item in parsed_data:
            if data_item:
                processed_parsed_data.append(data_item)

    return processed_parsed_data

def write_output_file(output_filename, parsed_data, verbose):
    working_dir = os.getcwd()
    if not output_filename.startswith('/'):
        output_filename = os.path.join(working_dir, output_filename)
    output_file = Path(output_filename)
    out_line = ",".join(parsed_data)
    out_line += "\n"
    with open(output_file, 'w+') as out_file:
        out_file.write(out_line)
    out_file.close()

def main():
    input_file=""
    output_file=""
    parsed_data=[]
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', action="store", dest="input_file", default="input.csv")
    parser.add_argument('--output_file', action="store", dest="output_file", default="output.csv")
    parser.add_argument('--verbose', action="store_true", default=False, dest="verbose")
    input_file=parser.parse_args().input_file
    output_file=parser.parse_args().output_file
    verbose=parser.parse_args().verbose
    parsed_data = parse_input_file(input_file, verbose)
    if verbose:
        print(parsed_data)

    parsed_data.sort(reverse=True, key=str.lower)
    if verbose:
        print(parsed_data)
    write_output_file(output_file, parsed_data, verbose)

if __name__ == '__main__':
    main()
