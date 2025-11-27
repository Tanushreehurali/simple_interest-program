import sys

if len(sys.argv) == 4:
    try:
        principal = float(sys.argv[1])
        rate = float(sys.argv[2])
        time = float(sys.argv[3])
    except ValueError:
        print("Error: principal, rate, and time must be numeric values.")
        sys.exit(1)
else:

    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (in %): "))
    time = float(input("Enter the time period (in years): "))

# Simple interest formula
simple_interest = (principal * rate * time) / 100

print(f"The simple interest is: {simple_interest}")
