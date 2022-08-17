# Write the solution for "Longest Word".
import re

f = open("../inputs/longest.txt", "r")
long_text = f.read()
f.close()

long_len = 0
longest = ""
for word in words:
    if len(word) > long_len:
        long_len = len(word)
        longest = word

  out_file = open("longest_out.txt", "w")
  out_file.write(long_text)
  out_file.close()
