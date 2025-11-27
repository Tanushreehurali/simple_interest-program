import sys

# Check if all 3 arguments are provided
if len(sys.argv) != 4:
    print("Usage: python simple_interest.py <principal> <rate> <time>")
    sys.exit(1)

# Read values from command line
principal = float(sys.argv[1])
rate = float(sys.argv[2])
time = float(sys.argv[3])

# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

print(f"The simple interest is: {simple_interest}")
