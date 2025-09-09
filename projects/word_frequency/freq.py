import sys

"""
    Description: Opens the file as a command line argument, splits each word 
    and appends it to a list. Allows the ability to access each string individually

    Arguments: None

    Retuns: List of each indiviual word from the input file
"""

def make_list():
    words = []
    inFile = open(sys.argv[1], "r")        
    words = inFile.read()
    words = words.split()
    words = sorted(words)
    inFile.close()
    return words
        
"""
    Description: Uses a list and create a dictionary with the words as keys and the number
    of occurances as the value. Allows the ability to associate a count
    with each individual word

    Arguments: None

    Returns: Dictionary or key-value pairs of each word with corresponding count
"""

def make_di():
    words = make_list()
    words_di = {}
    num = 0

    # Counts the occurence of each word
    # and creates a key-value pair
    for i in words:
        num = words.count(i)
        num = str(num)

        # Makes sure repeat words are
        # not added multiple times to the dictionary
        if i in words_di:
            pass
        else:
            words_di[i] = num

    return words_di

"""
    Description: Output word, count, and relative frequency
    to an output file as a frequency table

    Arguments: None

    Returns: output file containg relative frequency table
"""

def output_file():
    if len(sys.argv) < 2:
        print("Too few arguments.  Usage:  python3 freq.py <input_file_name>")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many arguments.  Usage:  python3 freq.py <input_input_name>")
        sys.exit(1)
    else:
        outFile_name = sys.argv[1] + ".out"
        outFile = open(outFile_name, "w")

        words_di = make_di()
        words_list = make_list()
        total = len(words_list)

        # Loop through the dictionary, accessing
        # the key-value pairs 
        for i, j in words_di.items():
            # calulate relative frequency for
            # each word
            num = round(int(j) / total, 3)
            num = str(num)
            outFile.write(i + " " + j + " " + num + "\n")
        
        outFile.close()
        return outFile

if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to 
    # this exercise, so you should call your code from here.
    output_file()
