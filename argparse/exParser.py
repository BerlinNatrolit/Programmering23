import argparse

parser = argparse.ArgumentParser(
                    prog="exParser",
                    description="This is an example used in KYH IoT dev23 of how the argparse library works.",
                    epilog="This is the epilog, just to show how this looks.")
parser.add_argument("-f", "--file", help="Input file")
parser.add_argument("-d", "--debug", action="store_true", help="Set the debug flag to get more information")
parser.add_argument("-v", '--version', action='version', version='%(prog)s 0.1')
parser.add_argument("numbers", nargs="+", type=int)

args = parser.parse_args()

if args.debug:
    print("We now have debug mode.")
else:
    print("Debug flag is not set.")

print(args.numbers)