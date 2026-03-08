# Shipping Cost Calculator
 # Here is a new update by LoayCpp

def main():
    try:
        weight = float(input("Enter package weight (kg): "))
        rate = float(input("Enter shipping rate per kg: "))

        # Validate input
        if weight <= 0 or rate <= 0:
            print("Weight and rate must be positive numbers.")
            return

        shipping_cost = weight * rate

        print(f"Shipping Cost: {shipping_cost:.2f} USD")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
