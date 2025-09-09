# Word Frequency Counter

This project is a simple Python script that reads a text file, counts the frequency of each unique word, and outputs a frequency table to a new file.

## Features

- **Reads Input File:**  
  The script takes a text file as a command-line argument, reads its contents, and splits it into individual words.

- **Word Counting:**  
  It counts the occurrences of each unique word and calculates the relative frequency (as a proportion of the total word count).

- **Sorted Output:**  
  The words are sorted alphabetically in the output.

- **Output File:**  
  Results are written to a new file with the same name as the input file, but with `.out` appended (e.g., `input.txt.out`). Each line contains the word, its count, and its relative frequency.

## Usage

Run the script from the command line:

```sh
python3 freq.py <input_file>

This will create a file named sample.txt.out with the frequency table.

## Output Format
The output file will contain lines formatted as follows:
```
word count relative_frequency
```

## Example
```
apple 3 0.150
banana 2 0.100
orange 1 0.050
```

## Notes and Assumptions 
- The script expects exactly one argument (the input file name).
- Words are split by whitespace and sorted alphabetically.
- The script does not perform advanced preprocessing (e.g., case normalization or punctuation removal).
- Output is written to a file in the same directory as the input.

## File Structure  
- `freq.py`: The main Python script that implements the word frequency counting functionality.
- `submission_validator.py`: Utility to validate the structure of your submission.
