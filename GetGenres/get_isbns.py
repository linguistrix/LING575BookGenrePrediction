__author__ = 'Maria Antoniak'

# Input = filtered reviews files
# Output = file with all unique ISBN numbers (one per line)

import sys, os


def get_isbn_dict(in_directory_path):
    isbn_dict = {}
    for in_file_name in os.listdir(in_directory_path):
        if in_file_name.endswith('.txt'):
            sys.stderr.write('Processing ' + in_file_name + '\n')
            infile = open(in_directory_path + in_file_name, 'r')
            for line in infile:
                tokens = line.split()
                if line.strip():
                    if tokens[0] == 'product/productId:':
                        isbn = tokens[1]
                        isbn_dict[isbn] = 0
    return isbn_dict


def print_isbn_dict(isbn_dict, out_file_path):
    outfile = open(out_file_path, 'w')
    for isbn in isbn_dict:
        outfile.write(isbn + '\n')


def main():
    in_directory_path = sys.argv[1]
    out_file_path = sys.argv[2]
    isbn_dict = get_isbn_dict(in_directory_path)
    print_isbn_dict(isbn_dict, out_file_path)


if __name__ == '__main__':
    main()
