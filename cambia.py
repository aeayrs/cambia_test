import argparse
def main():
    input_file=""
    output_file=""
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', action="store", dest="input_file", default="input.csv")
    parser.add_argument('--output_file', action="store", dest="output_file", default="output.csv")
    input_file=parser.parse_args().input_file
    output_file=parser.parse_args().output_file


if __name__ == '__main__':
    main()
