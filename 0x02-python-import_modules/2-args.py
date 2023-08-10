#!/usr/bin/python3
def main():
    args = sys.argv
    num_arg = len(args)
    print(f"Number of arguments: {num_arg}")
    if num_arg == 0:
        print(".")
    else:
        for i in range(num_arg):
            print(f"{i = 1}: {args[i]}")
if __name__ = "__main__":
    main()
