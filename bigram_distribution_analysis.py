#
# This file is made to be used with the data sets from https://people.sc.fsu.edu/~jburkardt/datasets/ngrams/ngrams.html
# in conjunction with a ciphertext file containing alphabetical characters and spaces
#

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

# read in english bigrams and monograms

en_digrams = pd.read_csv("english_bigrams.txt", delimiter=" ", header=None, names=["digram", "en_freq"], na_filter=False)
en_max = en_digrams["en_freq"].max()

en_monograms = pd.read_csv("english_monograms.txt", delimiter=" ", header=None, names=["monogram", "en_freq"], na_filter=False)

# read in ciphertext to find bigrams and monograms for
with open("c4", "r") as file:
    c4 = "".join(file.readlines()).replace("\n", "").replace(" ", "")


# get bigrams and monograms
c4_monograms = pd.DataFrame([*c4.upper()], columns=["monogram"])
c4_monograms = c4_monograms.value_counts().to_frame("c4_freq").reset_index().sort_values("c4_freq", ascending=False)
c4_digrams = np.array(re.findall(r'(?=(..))', c4.upper()))
c4_digrams = pd.DataFrame(c4_digrams, columns=["digram"])
c4_digrams = c4_digrams.value_counts().to_frame("c4_freq").reset_index().sort_values("c4_freq", ascending=False)
c4_max = c4_digrams["c4_freq"].max()

# define colours for specific characters, all negative numbers get clamped to -1
cols = {
    -1: 'lightsteelblue', 0:'black', 1:'red', 2:'green', 4:'blue', 8:'yellow', 16:'cyan'
}

# create subplots for english and ciphertext, each figure is 7x4
en_fig, en_plots = plt.subplots(7, 4, figsize=(60,50))
c4_fig, c4_plots = plt.subplots(7, 4, figsize=(60,50))

# chart english data
for index, letter in enumerate(en_monograms["monogram"]):
    row = index // 4
    col = index % 4
    en_freqs = en_digrams[en_digrams["digram"].str.contains(letter)]
    en_plots[row, col].bar(en_freqs["digram"], en_freqs["en_freq"],
                           color=( # define the number associated with each letter, then map the numbers to the predefined colours
                                   en_freqs["digram"].str.contains(letter+letter).replace([True, False], [-512, 0])
                                   + en_freqs["digram"].str.contains("E").replace([True, False], [1, 0])
                                   + en_freqs["digram"].str.contains("T").replace([True, False], [2, 0])
                                   + en_freqs["digram"].str.contains("A").replace([True, False], [4, 0])
                                   + en_freqs["digram"].str.contains("N").replace([True, False], [8, 0])
                                ).clip(-1, 512).replace({n: cols[n] if n in cols else 'dimgray' for n in range(-1,32)})
                           )
    en_plots[row, col].set_title(letter)
    en_plots[row, col].set_ylim(0, en_max)


# chart ciphertext data
for index, letter in enumerate(c4_monograms["monogram"]):
    row = index // 4
    col = index % 4
    c4_freqs = c4_digrams[c4_digrams["digram"].str.contains(letter)]
    c4_plots[row, col].bar(c4_freqs["digram"], c4_freqs["c4_freq"],
                           color=( # define the number associated with each letter, then map the numbers to the predefined colours
                                   c4_freqs["digram"].str.contains(letter + letter).replace([True, False], [-512, 0])
                                   + c4_freqs["digram"].str.contains("L").replace([True, False], [1, 0])
                                   + c4_freqs["digram"].str.contains("A").replace([True, False], [2, 0])
                                   + c4_freqs["digram"].str.contains("O").replace([True, False], [4, 0])
                                   + c4_freqs["digram"].str.contains("X").replace([True, False], [8, 0])
                                ).clip(-1, 512).replace({n: cols[n] if n in cols else 'dimgray' for n in range(-1,32)})
                           )
    c4_plots[row, col].set_title(letter)
    c4_plots[row, col].set_ylim(0, c4_max)


en_fig.savefig("en_freqs.png")
c4_fig.savefig("c4_freqs.png")