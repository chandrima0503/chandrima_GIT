import sys
command = sys.argv[1]
fname = sys.argv[2]
file = open(fname, 'rt')
data = file.read()
if command == "-l":
    num_lines = 0
    with open(fname, "r") as f:
        for line in f:
            num_lines += 1
    print(num_lines, fname)
elif command == '-w':
    words = data.split()
    print(len(words), fname)
elif command == "-c":
    no_of_chars = len(data)
    print(no_of_chars, fname)
elif command == "-n":
    with open(fname, "r") as f:
        for line in f:
            words = line.split()
            for i in words:
                for letter in i:
                    if(letter.isdigit()):
                        print(letter, end=" ")
elif command == "-a":
    with open(fname, "r") as f:
        for line in f:
            words = line.split()
            for i in words:
                for letter in i:
                    if(letter.isalpha()):
                        print(letter, end=" ")
elif command == '-h':
    print("-l: should display no. of lines present in a file \n -c: no. of characters present in a file \n -w: no. of words in a file \n -n: should display only numeric charcters in input file \n -a: should display only alphabets in input file \n -h: help message to run your program")
else:
    print("Wrong option selected. Please do -h to check for available options")

