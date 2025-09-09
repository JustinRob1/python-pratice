# Password Validator

## Overview

This project provides a Python module for validating and generating passwords according to specific security criteria. It demonstrates basic string analysis, validation logic, and random password generation.

## Features

- **Password Validation:**  
  The [`validate`](passwordvalidate/passwordvalidate.py) function checks if a password is:
  - **Secure:** At least 8 characters, contains at least one uppercase letter, one lowercase letter, one digit, and one special character (from a defined set).
  - **Insecure:** At least 8 characters, but missing one or more required character types.
  - **Invalid:** Less than 8 characters or contains disallowed characters (spaces, `@`, `#`, or empty string).

- **Password Generation:**  
  The [`generate`](passwordvalidate/passwordvalidate.py) function creates a random password of length `n` (where `n >= 8`) that is guaranteed to be "Secure" according to the above criteria.

## Special Character Set

The set of allowed special characters is: `! - $ % ' ( ) * + , . / : ; < = > ? _ [ ] ^ ` { | } ~`

Note: Double quotes (`"`) and backslash (`\`) are intentionally excluded for simplicity.

## Usage

Import the module and use the functions as follows:

```python
from passwordvalidate import validate, generate

result = validate("My$ecureP4ssword")
print(result)  # Output: "Secure"

password = generate(12)
print(password)  # Output: A secure 12-character password

## File Structure

- passwordvalidate.py: Main implementation.
- submission_validator.py: Script for validating submission structure (for course use).

##  Assumptions 

- The password length for generation must be at least 8.
- Disallowed characters: space, @, #, and empty string.
- Only the specified special characters are considered valid.