# Write the solution for "Split the files".
import os
import re

def split_file(file):
    file_bytes = os.stat('./inputs/split/' + file + ".txt")
    if file_bytes.st_size > 500:
        file_open = open('./inputs/split/' + file + ".txt", "r")
        text = file_open.read()

        word_pattern = "\w+"
        regex = re.compile(word_pattern)
        found = regex.findall(text)

        first_string = found[:round(len(found) / 2)]
        second_string = found[round(len(found) / 2):]

        with open(file + "-1.txt", "w") as f:
            f.write(' '.join(first_string))

        with open(file + "-2.txt", "w") as f2:
            f2.write(' '.join(second_string))

def main():
    split_file("github")
    split_file("meta")
