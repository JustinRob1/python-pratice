import sys

modes = ["keep-digits", "keep-symbols", "keep-stops"]

stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", 
"yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", 
"hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", 
"themselves", "what", "which","who", "whom", "this", "that", "these", "those", 
"am", "is", "are", "was", "were", "be","been", "being", "have", "has", "had", 
"having", "do", "does", "did", "doing", "a", "an","the", "and", "but", "if", 
"or", "because", "as", "until", "while", "of", "at", "by", "for", "with", 
"about", "against", "between", "into", "through", "during", "before", "after", 
"above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over",
"under", "again", "further", "then", "once", "here", "there", "when", "where", 
"why", "how", "all", "any", "both", "each", "few", "more", "most", "other", 
"some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", 
"too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

"""
    Description: Converts each alphabetic character in a list of strings to lowercase

    Arguments: List of inputed words

    Returns: None
"""
def to_lower(words):
     for i in range(len(words)):
          words[i] = words[i].lower()

"""
    Description: Removes every non alphanumeric character in a list of strings

    Arguments: List of inputed words

    Returns: None
"""
def remove_char(words):
     for i in range(len(words)):
          # loops through each character of each string and removes
          # every character if it is not alphanumeric
          words[i] = "".join(c for c in words[i] if c.isalnum())

"""
    Description: Removes every numeric character in a list of strings
    excpet when the entire string consists of only numbers

    Arguments: List of inputed words

    Returns: None
"""
def remove_num(words):
     for i in range(len(words)):
          # check if the string consists of only numbers
          if words[i].isdigit():
                continue
          else:
                # Loops through each character of the string and removes the numbers
                words[i] = "".join(n for n in words[i] if not n.isdigit())

"""
    Description: Removes every occurrence of the specified stop words in a list of strings

    Arguments: List of inputed words

    Returns: None
"""
def remove_stop(words):
     i = 0
     while i < len(words):
          if words[i] in stopwords:
                # pops out the stopwords
                words.pop(i)
          else:
                i += 1

"""
    Description: Prints out the new text as a spaced seperated string

    Arguments: None

    Returns: None
"""
def print_list():
    # reads in the input and splits it into
    # a list 
     input_string = input()
     words = input_string.split()
     my_str = ""

     if len(sys.argv) < 2:
        to_lower(words)
        remove_char(words)
        remove_num(words)
        remove_stop(words)
     else:
          if sys.argv[1] == "keep-digits":
                to_lower(words)
                remove_char(words)
                remove_stop(words)
          elif sys.argv[1] == "keep-stops":
                to_lower(words)
                remove_char(words)
                remove_num(words)
          elif sys.argv[1] == "keep-symbols":
                to_lower(words)
                remove_num(words)
                remove_stop(words)
     for i in words:
          my_str += ' ' + i
     print(my_str.strip())

if __name__ == "__main__":
     # Any code indented under this line will only be run
     # when the program is called directly from the terminal
     # using "python3 preprocess.py". This is directly relevant 
     # to this exercise, so you should call your code from here.
     if len(sys.argv) < 2:
        print_list()
     elif sys.argv[1] in modes:
        print_list()
     elif sys.argv[1] not in modes:
        print("Invalid argument.  Usage:  python3 preprocess.py <mode>")
        print("Valid <mode>.  <keep-symbols>  <keep-digits>  <keep-stops>")
        sys.exit()
     else:
        print("Too many argument.  Usage:  python3 preprocess.py <mode>")
        print("Valid <mode>.  <keep-symbols>  <keep-digits>  <keep-stops>")
        sys.exit()
