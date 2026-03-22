# Takes the file output of a Kasiski analysis from JKrypto and converts it
# into an Excel file
import pandas as pd
import re  # not strictly necessary, but makes code nicer

file_name = input("Input file from JKrypto: ")
with open(file_name, "r") as file:
    rows = file.readlines()[2:]  # first two lines are not data

cols = rows[0]
rows = rows[2:] #remove cols and blank line

data = map(lambda row: re.split(r"\W+", row.strip()), rows)
df = pd.DataFrame(data, columns=re.split(r"\W+", cols.strip()))
df.to_excel(input("Output file name: "))