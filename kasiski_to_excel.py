# Takes the file output of a Kasiski analysis from JKrypto and converts it
# into an Excel file
import pandas as pd
import re  # not strictly necessary, but makes code nicer

if False:
    from sympy.ntheory import factorint
else:
    factorint = None

file_name = input("Input file from JKrypto: ")
with open(file_name, "r") as file:
    rows = file.readlines()[2:]  # first two lines are not data

data = map(lambda row: re.split(r": |\| ", row.strip()), rows)
df = pd.DataFrame(data, columns=["string", "occurrences", "relative offset"])
#df["relative offset"] = pd.to_numeric(df["relative offset"])
#df.sort_values("relative offset", inplace=True, ascending=False)
df.sort_values("string", inplace=True, ascending=True)
if factorint is not None:
    df["prime factorisation"] = df["relative offset"].apply(lambda num: str(factorint(num, visual=True)).replace("**", "^").replace("*", "·"))
df.to_excel(input("Output file name: "))