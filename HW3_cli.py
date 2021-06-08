""" CLI program to for HW3 homework """
# Put your name here
import argparse


if __name__ == "__main__":
    # Set up argparse parser and arguments here
    parser = argparse.ArgumentParser(epilog="Does print, combine, then len. If no flags given, does nothing.")
    # Add the arguments here
    parser.add_argument("-c", "--combine", help="Print input strings combined in a continuous string",action="store_true")
    parser.add_argument("-p", "--print", help="Just print the input stringsg",action="store_true")
    parser.add_argument("-l", "--len", help="Print the lengths of the input strings",action="store_true")
    parser.add_argument("texts",help="Input strings to operate on",nargs="+")
    args = parser.parse_args()
    # execute whatever the flags say to do here
    texts = args.texts
    if args.print:
        print(" ".join(texts))
    if args.combine:
        print("".join(texts))
    if args.len:
        for item in texts:
            print(len(item) , end = " ")
        print()

    # If you prefer to call a single main() function written above the
    # if __name__ == "__main__":
    # statement, that is OK with me.
    # The important thing is to make it work correctly. ;-)