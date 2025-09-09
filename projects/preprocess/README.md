# Text Preprocessing Utility

## Overview

This project provides a Python script for basic text preprocessing, designed to clean and normalize input text for downstream tasks such as natural language processing or machine learning. The script demonstrates modular preprocessing steps and flexible command-line usage, making it suitable for educational and portfolio purposes.

## Features

- **Lowercasing:**  
  Converts all alphabetic characters in the input to lowercase using [`to_lower`](preprocess/preprocess.py).

- **Symbol Removal:**  
  Removes all non-alphanumeric characters from each word using [`remove_char`](preprocess/preprocess.py).

- **Digit Removal:**  
  Removes numeric characters from words, except when the entire word is numeric, using [`remove_num`](preprocess/preprocess.py).

- **Stop Word Removal:**  
  Removes common English stop words from the input using [`remove_stop`](preprocess/preprocess.py).

- **Flexible Preprocessing Modes:**  
  By default, all preprocessing steps are applied. Optionally, the user can specify a mode via a command-line argument to skip one step:
  - `keep-digits`: Keeps digits (skips digit removal)
  - `keep-symbols`: Keeps symbols (skips symbol removal)
  - `keep-stops`: Keeps stop words (skips stop word removal)

- **Error Handling:**  
  The script checks for invalid or excessive command-line arguments and prints usage instructions if an error is detected.

## Usage

Run the script from the command line, optionally specifying a mode:

```sh
python3 [preprocess.py](http://_vscodecontentref_/0) [mode]

If no mode is specified, all preprocessing steps are performed.

## Example
$ python3 preprocess.py keep-digits
Enter text: The quick brown fox jumps over 13 lazy dogs!
Output: the quick brown fox jumps over 13 lazy dogs

## File Structure

- preprocess.py: Main implementation of the preprocessing logic.
- submission_validator.py: Script for validating submission structure (for course use).

## Assumptions 

- Input is a single line of text, processed as a list of words.
- Only one optional mode argument is supported.
- Invalid or excessive arguments result in an error message and program exit.
- Stop words are defined in a built-in list in the script.