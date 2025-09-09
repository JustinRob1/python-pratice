# Unfair Dice Simulator

This project simulates rolling a biased (unfair) m-sided die and visualizes the results as a histogram.

## Features

- **Biased Dice Simulation:**  
  The program includes a function `biased_rolls` that simulates rolling an m-sided die `n` times, where each side has a user-specified probability. The function returns a list of the results.

- **Histogram Visualization:**  
  The `draw_histogram` function displays a frequency histogram of the simulated rolls, scaled to a fixed width using `#` and `-` characters for easy visualization in the terminal.

## Assumptions

- All inputs are positive integers or floats.
- The probability list contains only floating-point values and is passed in the correct order.
- Histogram bars are rounded to the nearest integer for display.

## File Structure

- `unfairDice.py` — Contains the main simulation and visualization functions.
- `submission_validator.py` — Script to validate the structure of your submission archive.

## Example

```python
prob_list = [0.1, 0.2, 0.3, 0.4]  # Probabilities for a 4-sided die
rolls = biased_rolls(prob_list, 4, 100)
draw_histogram(4, rolls, 20)