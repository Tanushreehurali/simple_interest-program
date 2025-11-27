import sys

# Expecting: python simple_interest.py <principal> <rate> <time>
if len(sys.argv) != 4:
    print("Usage: python simple_interest.py <principal> <rate> <time>")
    sys.exit(1)

principal = float(sys.argv[1])
rate = float(sys.argv[2])
time = float(sys.argv[3])

simple_interest = (principal * rate * time) / 100

print(f"Principal: {principal}")
print(f"Rate: {rate}")
print(f"Time: {time}")
print(f"Simple Interest: {simple_interest}")
