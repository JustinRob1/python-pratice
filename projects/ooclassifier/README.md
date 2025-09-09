# ooclassifier

## Overview

This project implements a simple object-oriented text classifier in Python. It demonstrates basic concepts in text preprocessing, classification, and data partitioning, which is useful for machine learning workflows.

## Usage

The main script reads input data (from a file or stdin), processes it into training instances, applies preprocessing, and performs classification. The classifier can be configured to use a fixed list of target words or dynamically select them based on word frequency.

To run the program:
```sh
python3 ooclassifier.py [input_file]
```
If no input file is provided, it reads from `file.input.txt` or standard input.

## File Structure

- `ooclassifier.py` — Main implementation of the classifier and supporting classes.
- `test_ooclassifier.py` — Unit tests for the classifier and its components.
- `README` — This documentation file.

## Notes

- The code assumes valid input and does not include extensive error handling for preprocessing modes or input types.
- The classifier is intended for demonstration and educational use, not for production deployment.
