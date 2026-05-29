import argparse

parser = argparse.ArgumentParser(description="simple calculator")

parser.add_argument("num1", type = float, help = "First number")
parser.add_argument("num2", type = float, help = "Second number")

parser.add_argument("operation", choices=["add","sub","div","mul"], help="operation to perform ")

args = parser.parse_args()

print(args)


