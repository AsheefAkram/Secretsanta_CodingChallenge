# Secret Santa Game

## Overview
The Secret Santa Game automates the process of assigning secret children to employees for a Secret Santa event. This program ensures that each employee gets a unique secret child while adhering to the constraints of not assigning the same secret child as in the previous year and avoiding self-assignment.

## Features
- Parses employee information from a CSV file.
- Ensures each employee gets a unique secret child.
- Avoids assigning the same secret child as in the previous year.
- Generates an output CSV file with the Secret Santa assignments.

## Installation

### Prerequisites
- Python 3.6+
- Pandas library

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/AsheefAkram/Secretsanta_CodingChallenge.git
    cd secretsanta
    ```

2. Create and activate a virtual environment:

    - **Windows:**

    ```sh
    python -m venv myenv
    myenv\Scripts\activate
    ```

    - **macOS/Linux:**

    ```sh
    python -m venv myenv
    source myenv/bin/activate
    ```

3. Install required libraries:

    ```sh
    pip install pandas
    ```

## Usage

1. Prepare the input CSV files:

    - `employees.csv`: Contains employee information.
    - `previous_assignments.csv`: Contains last year's Secret Santa assignments.

2. Update the `main` function in `secret_santa.py` with the paths to your input files:

    ```python
    employees_file = 'path_to_your_file/employees.csv'
    previous_assignments_file = 'path_to_your_file/previous_assignments.csv'
    output_file = 'path_to_your_file/secret_santa_assignments.csv'
    ```

3. Run the program:

    ```sh
    python secretsanta.py
    ```

4. Check the generated output file (`secret_santa_assignments.csv`) for the Secret Santa assignments.



