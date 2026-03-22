# simple program to print top n-grams within a file

import re
import numpy as np
import pandas as pd

# insert file name here
with open("c4", "r") as file:
    text = "".join(file.readlines()).replace("\n", "").replace(" ", "")

# adjust the regex to filter ngrams as desired
quadgrams = np.array(re.findall(r'(?=(...))', text))

ngrams = pd.DataFrame(quadgrams, columns=["ngram"])
ngrams = ngrams.value_counts()
print(ngrams.head(50))
