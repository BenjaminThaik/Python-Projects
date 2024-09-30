import math

# Resistor class to represent a resistor
class Resistor:
    def __init__(self, resistance):
        # Ensures the resistance is a positive value
        if resistance <= 0:
            raise ValueError("Resistance must be a positive value.")
        self.resistance = resistance

    def get_resistance(self):
        # Returns the resistance value of the resistor
        return self.resistance

    def __str__(self):
        # String representation of the resistor object (in ohms)
        return f"{self.resistance}Ω"

# Circuit class to simulate a collection of resistors
class Circuit:
    def __init__(self):
        # Initializes an empty list to store resistors
        self.resistors = []

    def add_resistor(self, resistor):
        # Adds a resistor to the circuit
        self.resistors.append(resistor)

    def total_resistance_series(self):
        # Calculates total resistance in series (sum of all resistances)
        total = sum(r.get_resistance() for r in self.resistors)
        return total

    def total_resistance_parallel(self):
        # Calculates total resistance in parallel using the reciprocal formula
        try:
            total_inverse = sum(1/r.get_resistance() for r in self.resistors)
            # Returns the reciprocal of the total inverse if not zero
            return 1 / total_inverse if total_inverse != 0 else float('inf')
        except ZeroDivisionError:
            return float('inf')

    def reset(self):
        # Resets the circuit by clearing the list of resistors
        self.resistors = []

    def view_resistors(self):
        # Displays all resistors in the circuit
        if not self.resistors:
            return "No resistors in the circuit."
        return ", ".join([str(r) for r in self.resistors])

# Main function to run the command-line interface for the circuit simulation
def main():
    # Initialize a circuit object
    circuit = Circuit()

    while True:
        # Display the menu for user interaction
        print("\n--- Circuit Simulation ---")
        print("1. Add a resistor")
        print("2. Calculate total resistance (Series)")
        print("3. Calculate total resistance (Parallel)")
        print("4. View resistors")
        print("5. Reset circuit")
        print("6. Exit")

        # Get user choice from the menu
        choice = input("Choose an option: ")

        if choice == "1":
            # Add a new resistor to the circuit
            try:
                resistance = float(input("Enter resistor value (in ohms): "))
                resistor = Resistor(resistance)
                circuit.add_resistor(resistor)
                print(f"Added resistor: {resistor}")
            except ValueError as e:
                print(e)

        elif choice == "2":
            # Calculate and display total resistance for series circuit
            if circuit.resistors:
                total_series = circuit.total_resistance_series()
                print(f"Total resistance in series: {total_series}Ω")
            else:
                print("No resistors in the circuit!")

        elif choice == "3":
            # Calculate and display total resistance for parallel circuit
            if circuit.resistors:
                total_parallel = circuit.total_resistance_parallel()
                print(f"Total resistance in parallel: {total_parallel:.2f}Ω")
            else:
                print("No resistors in the circuit!")

        elif choice == "4":
            # View all resistors in the circuit
            print("Current resistors: ", circuit.view_resistors())

        elif choice == "5":
            # Reset the circuit (remove all resistors)
            circuit.reset()
            print("Circuit reset.")

        elif choice == "6":
            # Exit the program
            print("Exiting simulation.")
            break

        else:
            # Handle invalid input
            print("Invalid choice, please select again.")

# Entry point of the script
if __name__ == "__main__":
    main()
