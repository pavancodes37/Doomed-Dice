This project explores transforming a pair of dice to maintain the same sum probability distribution while adhering to certain constraints. The goal is to modify one or both dice such that they satisfy Loki's conditions while preserving the original sum distribution.

Features:

Calculate sum distributions and probabilities for two six-sided dice.

Transform the dice while preserving the sum probability distribution.

Generate a sum distribution matrix.

Requirements:

This project requires Python and the following libraries:

pip install numpy

Usage:

Running the Code in VS Code

Open VS Code and load the project folder.

Ensure you have Python installed and added to the system PATH.

Open a terminal in VS Code (Ctrl + ~ on Windows or Cmd + ~ on macOS).

Install required dependencies if not already installed:

pip install numpy

Run the script by executing:

python dice_simulation.py

Explanation:

calculate_distribution(die_a, die_b): Computes the sum distribution and probabilities for given dice.

undoom_dice(die_a, die_b): Modifies the dice to maintain probability distribution under given constraints.

create_sum_matrix(die_a, die_b): Generates a 6x6 sum distribution matrix.

Example Output:

Total possible combinations: 36 Sum Distribution: {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1} Probabilities: {2: 0.027, 3: 0.056, ..., 12: 0.027} Sum Distribution Matrix: [[ 2 3 4 5 6 7] [ 3 4 5 6 7 8] ... [ 7 8 9 10 11 12]] New Die A: [1, 1, 2, 2, 3, 4] New Die B: [5, 6, 7, 8, 9, 10]

License:

This project is licensed under the MIT License. Feel free to modify and distribute it.

Contributions:

Pull requests are welcome! If you find any issues or improvements, feel free to submit a PR or open an issue.
