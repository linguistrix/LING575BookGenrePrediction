__author__ = 'Maria Antoniak'

import sys, os

def main():
    in_directory_path = sys.argv[1]
    out_directory_path = sys.argv[2]
    for in_file_name in os.listdir(in_directory_path):
        if in_file_name.endswith('.txt'):
            sys.stderr.write('Processing ' + in_file_name + '\n')
            infile = open(in_directory_path + in_file_name, 'r')
            outfile = open(out_directory_path + in_file_name, 'w')
            has_isbn = False
            current_review_string = ''
            for line in infile:
                tokens = line.split()
                if line.strip():
                    current_review_string += line
                    if tokens[0] == 'product/productId:':
                        isbn = tokens[1]
                        if len(isbn) == 10 and isbn.isdigit():
                            has_isbn = True
                        else:
                            has_isbn = False
                    elif tokens[0] == 'review/text:':
                        if has_isbn:
                            outfile.write(current_review_string + '\n')
                        current_review_string = ''

if __name__ == '__main__':
    main()
