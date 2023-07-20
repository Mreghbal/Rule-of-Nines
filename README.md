# Burn Area Calculator

This is a Python code for calculating the estimated burn area using the Rule of Nines. The Rule of Nines is a method used to estimate the percentage of total body surface area (TBSA) affected by burns in adults. It divides the body into different regions, each representing a specific percentage of TBSA.

## Usage

To use this code, follow these steps:

1. Make sure you have Python installed on your system.
2. Clone or download the repository to your local machine.
3. Open the terminal or command prompt and navigate to the project directory.
4. Run the following command to execute the code:

   ```
   python calculate_burn_area.py
  `

5. Enter the patient's age when prompted and press Enter6. Enter the patient's weight (in kilograms) when prompted and press Enter.

The program will then calculate the estimated burn area percentage based on the Rule Nines and display the result.

## Requirements

This code requires Python 3.x to be installed on your system. If you don't have Python installed, you can download it from the official Python website: [python.org](https://www.python.org/).

## Input Validation

The code performs validation checks on the input values to ensure they are within the appropriate ranges:

- Age should be between 1 and 100.
- Weight should be greater than zero.

If any of the input values are invalid, a `ValueError` will be raised with an appropriate error message.

## Rule of Nines

The Rule of Nines percentages used in this code for different body parts are as follows:

- Head: 9%
- Arms: 9% (each arm- Chest: 18%
- Abdomen: 18%
- Back: 18%
- Groin: 1%
- Legs: 18% (each leg)

These percentages are based on the approximation that each body part represents a certain proportion of the total body surface area.

## Calculation

The code calculates the burn percentage using the following formula:

```
burn_percentage = (age / 9) * (weight / total_body_surface_area)
```

- `age` the patient's age.
- `weight` is the patient's weight in kilograms.
- `total_body_surface_area` is the sum of the Rule of Nines percentages for all body parts.

The burn percentage represents the estimated percentage of total body surface area affected by burns.

## Example Output

Here's an example output of running the code:

```
Enter the patient's age: 35
Enter the patient's weight (in kg): 70
The estimated burn area is 15.56%.
```

This means that, based on the patient's age and weight, approximately 15.56% of their total body surface area is estimated to be affected by burns.

---

Thank you for using the Burn Area Calculator! If you have any questions or suggestions, feel free to reach out. Happy coding! 🔥📈
