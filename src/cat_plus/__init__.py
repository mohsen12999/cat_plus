from argparse import ArgumentParser

def main() -> None:
    parser = ArgumentParser(
        description="cat-plus: An enhanced version of the cat command"
    )

    parser.add_argument(
        "file",
        nargs="?",
        help="File to read"
    )

    parser.add_argument(
        "-n", "--line-numbers",
        action="store_true",
        help="Show line numbers"
    )

    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, 'r') as f:
                content = f.readlines()
                for i, line in enumerate(content, 1):
                    if args.line_numbers:
                        print(f"{i:6d}  {line}", end='')
                    else:
                        print(line, end='')
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found")
    else:
        print("Please provide a file to read")