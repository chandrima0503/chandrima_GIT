import sys
command = sys.argv[1]
fname = sys.argv[2]
file = open(fname, 'rt')
data = file.read()
if command == "-l":
    num_lines = 0
    for line in file:
        num_lines += 1
    print(num_lines, fname)
if command == '-w':
    words = data.split()
    print(len(words), fname)
if command == "-c":
    no_of_chars = len(data)
    print(no_of_chars, fname)
if command == "-n":
    for line in file:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isdigit()):
                    print(letter, end=" ")
if command == "-a":
    for line in file:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isalpha()):
                    print(letter, end=" ")
if command == '-h':
    print("-l: should display no. of lines present in a file \n -c: no. of characters present in a file \n -w: no. of words in a file \n -n: should display only numeric charcters in input file \n -a: should display only alphabets in input file \n -h: help message to run your program")

