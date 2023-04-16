import argparse


class Arguments:
    filename: str
    outputFilepath: str


parser = argparse.ArgumentParser(
    prog="python ./src/main.py",
    description="Automatically generate flashcards in a word document",
)
parser.add_argument("-f", "--file", dest="filename", help="the file to load data from")
parser.add_argument(
    "-o", "--output", dest="outputFilepath", help="output filename", default="out.docx"
)


def get_args() -> Arguments:
    args: Arguments = parser.parse_args()
    if args.filename is None:
        args.filename = input("Enter the data files name > ")
    if args.outputFilepath == "out.docx":
        inp = input("Enter output filename (leave blank for 'out.docx') > ")
        if not inp == "":
            args.filename = inp
    return args
