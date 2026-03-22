# this was an early version of bigram_distribution_analysis.py that was intended to work with
# trigrams instead of bigrams, but was dropped due to the impractically long time it took
# for pyplot to chart the data, as well as the illegibility of the results at the current
# image size

import itertools

import matplotlib.container
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

from IPython.core.pylabtools import figsize

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

en_trigrams = pd.read_csv("ciphertext_4/english_trigrams.txt", delimiter=" ", header=None, names=["trigram", "en_freq"], na_filter=False)
en_max = en_trigrams["en_freq"].max()
en_min = en_trigrams["en_freq"].min()

en_monograms = pd.read_csv("ciphertext_4/english_monograms.txt", delimiter=" ", header=None, names=["monogram", "en_freq"], na_filter=False)


with open("ciphertext_4/c4", "r") as file:
    c4 = "".join(file.readlines()).replace("\n", "").replace(" ", "")

c4_monograms = pd.DataFrame([*c4.upper()], columns=["monogram"])
c4_monograms = c4_monograms.value_counts().to_frame("c4_freq").reset_index().sort_values("c4_freq", ascending=False)
c4_trigrams = np.array(re.findall(r'(?=(...))', c4.upper()))
c4_trigrams = pd.DataFrame(c4_trigrams, columns=["trigram"])
c4_trigrams = c4_trigrams.value_counts().to_frame("c4_freq").reset_index().sort_values("c4_freq", ascending=False)
c4_max = c4_trigrams["c4_freq"].max()
c4_min = c4_trigrams["c4_freq"].min()

order = [a+b for a,b in itertools.product(alphabet, repeat=2)]
all_trigrams = pd.DataFrame(order, columns=["trigram"])
all_trigrams = pd.merge(all_trigrams, en_trigrams, how="outer", on=["trigram"])
# all_trigrams = pd.merge(all_trigrams, c4_trigrams, how="outer", on=["trigram"])


en_fig, en_plots = plt.subplots(7, 4, figsize=(60,50))
# c4_fig, c4_plots = plt.subplots(7, 4, figsize=(60,50))
for index, letter in enumerate(en_monograms["monogram"]):
    row = index // 4
    col = index % 4
    en_freqs = en_trigrams[en_trigrams["trigram"].str.contains(letter)]
    en_plots[row, col].bar(en_freqs["trigram"], en_freqs["en_freq"], color=en_freqs["trigram"].str.contains("E").replace([True, False], ["red", "blue"]))
    en_plots[row, col].set_title(letter)
    en_plots[row, col].set_ylim(0, en_max)
    print(index)

# for index, letter in enumerate(c4_monograms["monogram"]):
#     row = index // 4
#     col = index % 4
#     c4_freqs = c4_trigrams[c4_trigrams["trigram"].str.contains(letter)]
#     c4_plots[row, col].bar(c4_freqs["trigram"], c4_freqs["c4_freq"], color=c4_freqs["trigram"].str.contains("L").replace([True, False], ["red", "blue"]))
#     c4_plots[row, col].set_title(letter)
#     c4_plots[row, col].set_ylim(0, c4_max)
#     print(index)


en_fig.savefig("en_tri_freqs2.png")
# c4_fig.savefig("c4_tri_freqs.png")





# print(c4_trigrams.head(20))



#print(english_trigrams[english_trigrams["trigram"].str.contains("A")])