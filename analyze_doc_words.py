#!/usr/bin/python3
# Code name: analyze_doc_words.py 
# Brief Description: A script for computing statistics on a collection of 
# documents (books) stored in a hierarchical file structure.  Based on the 
# lecture from Case Study #2 in the Using Python for Research course by 
# HarvardX and the associated HW#2 by DataCamp.  This code has several 
# significant updates from the course version, including:
# 1) an expanded list of punctuations to skip, plus a bit better implementation
#    for skipping punctuation (explicitly looks for punc + a space to left
#    and/or right, depending on the nature of the punctuation
# NOTE: 
# Created on: December 16, 2016
# Written by: Frederick D. Pearce
# Code version: 0.1 on 12/17/2016 - Original version used to setup github repo

# Copyright 2016 Frederick D. Pearce

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0

## I) Import modules, all available via pip install
from collections import Counter, defaultdict
import os
import matplotlib.pyplot as plt
import pandas as pd

## II) Define functions
def read_doc(doc_path):
    """
    Read a document and return its text as a string. Replace newline, "\n", 
    and returns, "\r", escape character with a space.
    """
    with open(doc_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", " ").replace("\r", " ")
    return text

def count_words(text):
    """
    Count the number of times each word occurs in text (str).  Return a 
    dictionary where keys are unique words and values are the word counts.  
    Input text is converted to lower-case, and all punctuations listed in
    punc_to_skip are replaced by an empty space.
    """
    text = text.lower()
    # these punc to skip are old, but not currently used...
    punc_to_skip = [". ", ", ", "; ", ": ", " '", "' ", ' "', '" ' "?", "! ", \
            "-", " (", ") "]
    for ch in punc_to_skip:
        text = text.replace(ch, " ")
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def count_words_fast(text):
    """
    Fast way to count the number of times each word occurs in text (str).  
    Return a dictionary where keys are unique words and values are the word 
    counts. Input text is converted to lower-case, and all punctuation is 
    skipped. A word consisting of an empty string is NOT included in the 
    returned word_counts dict, and a message is printed to the screen reporting
    the # of empty strings that were found. A word consisting of a single blank
    space is included in the returned word_counts dict and a message is printed
    to the screen reporting a warning with the # of single blanks that were
    found.
    """
    text = text.lower()
    #skips = [".", ",", ";", ":", "'", '"']
    punc_to_skip = [".", "?", "-", "_", "*", "=", "+", ", ", "; ", ": ", \
            " '", "' ", ' "', '" ', "! ", " (", ") "
    ]
    for ch in punc_to_skip:
        text = text.replace(ch, " ")
    word_counts = Counter(text.split(" "))
    if "" in word_counts:
        print("\n Removing EMPTY string with {} counts from word_counts!" \
                .format(word_counts[''])
        )
        del word_counts['']
    if " " in word_counts:
        print("\n A BLANK string was found with {} counts!".format(
            word_counts[' '])
        )
    return word_counts

def calc_doc_word_lengths(word_counts, wordlen_minmax):
    """Take in a word count dictionary and return a dictionary where the keys
    are the length of each word and the values are the total occurance of 
    words with that length in the document.
    """
    # Initialize word length distribution dict with keys defined by range
    # of wordlen_minmax, and each value set to int of zero
    wl_min, wl_max = wordlen_minmax
    wl_dist = dict.fromkeys(range(wl_min, wl_max+1), 0)
    for k, v in word_counts.items():
        word_len = len(k)
        if word_len in wl_dist:
            wl_dist[word_len] += v
        elif word_len > wl_max:
            wl_dist[wl_max] += v
        elif word_len < wl_min:
            wl_dist[wl_min] += v
        else:
            print("\nError: word length of {} NOT recorded in wl_dist dict!\n" \
                    .format(word_len)
            )
    return wl_dist

def calc_doc_word_stats(word_counts):
    """Return number of unique words and word frequencies."""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

def calc_word_distribution(word_counts):
    """Take the input word_counts dictionary and outputs a dictionary with
    the same keys as those in word_counts (the number of times a group of 
    words appears in the text), and values corresponding to the fraction of 
    words that occur with more frequency than that key.
    Taken from DataCamp exercise 2 that goes along with Case Study 2.
    """
    wc_mf = {}
    wcv_list = list(word_counts.values())
    sum_words = sum(wcv_list)
    for k, v in word_counts.items():
        wc_mf[k] = sum(i > v for i in wcv_list) / sum_words
    return wc_mf

def get_doc_stats(wordlen_minmax, root_dir):
    """Get statistics on each document in hierarchical folder structure with
    top level=root_dir.  Return a Pandas DataFrame containing each document's
    language, author, title, total word count, number of unique words, and 
    word count distribution.
    Hidden folders and files are not included (i.e. those starting with .)
    The example below is designed for the book folder structure from the HW2
    of the Using Python for Research course.  Modify accordingly for other
    document folder structures!
    """
    doc_stats = pd.DataFrame(columns = ("language", "author", "title", "length", \
            "unique"
    ))
    doc_wordlens = pd.DataFrame()
    doc_names = {}
    doc_num = 1
    languages = [val for val in os.listdir(root_dir) if val[0] != "."]
    for lang in languages:
        authors = [val for val in os.listdir(root_dir+"/"+lang) if val[0] != "."]
        for auth in authors:
            titles = [val for val in os.listdir(root_dir+"/"+lang+"/"+auth) \
                    if val[0] != "."
            ]
            for titl in titles:
                #  For each language, author and title
                # 1) Define a string with the name of the input file
                # 2) Build a dictionary containing unique words (keys) and 
                # their counts, count_words
                # 3) Build a dictionary containing word lengths (keys) and 
                # their counts, word_lens
                # 4) Build a dictionary containing the names of each document
                # with keys corresponding to each column name in doc_wordlens 
                # (Doc1, Doc2, etc.) and values containing a string with each 
                # document's language, author, and title separated by underscores
                inputfile = "/".join((root_dir, lang, auth, titl))
                print("\n"+inputfile) 
                count_words = count_words_fast(read_doc(inputfile))
                (num_unique, counts) = calc_doc_word_stats(count_words)
                doc_stats.loc[doc_num] = lang, auth.capitalize(), titl[:-4], \
                        sum(counts), num_unique
                word_lens = calc_doc_word_lengths(count_words, wordlen_minmax)
                doc_wordlens["Doc"+str(doc_num)] = pd.Series( \
                        list(word_lens.values()), index=word_lens.keys()
                )
                doc_names["Doc"+str(doc_num)] = "_".join( \
                        (lang, auth.capitalize(), titl[:-4])
                )
                doc_num += 1 
    return (doc_stats, doc_wordlens, doc_names)

def get_doc_names_short(doc_names, dnlens=(3, 5, 5)):
    """Return shortened document names."""
    dn_short = {}
    for k,v in doc_names.items():
        lang, auth, titl = v.split("_")
        dn_short[k] = ", ".join((lang[:min(dnlens[0], len(lang))], \
                auth[:min(dnlens[1], len(auth))], \
                titl[:min(dnlens[2], len(titl))]
        ))
    return dn_short

def get_lang_start_ind(doc_wordlens, doc_names):
    """Takes in a Pandas DataFrame containing the word length histograms
    for ALL documents, doc_wordlens, and a dictionary that maps each column 
    name (keys) to a string that describes each document (values).  Returns
    a list of each unique language in the document description, doc_langs, 
    and the corresponding starting row index for each language, doc_lrsinds.
    """
    doc_langs = []
    doc_lrsinds = []
    for ci, cn in enumerate(doc_wordlens.columns):
        lang = doc_names[cn].split("_")[0]
        if lang not in doc_langs:
            doc_lrsinds.append(ci)
            doc_langs.append(lang)
    return (doc_langs, doc_lrsinds)

def plot_docstats_bylanguage(doc_stats, figfname, figsize=(10, 10)):
    """
    Plot document statistics using figure size of figsize.  Save resulting
    figure to file named figfname. 
    """
    languages = pd.unique(doc_stats["language"])
    langcol = ["blue", "green", "orange", "red"]
    langmark = ["o", "s", "p", "d"]
    linestyle = "None"
    plt.figure(figsize = figsize)
    for ind, lang in enumerate(languages):
        subset = doc_stats[doc_stats.language==lang]
        plt.loglog(subset.length, subset.unique, label=lang, \
                linestyle=linestyle, marker=langmark[ind], color=langcol[ind]
        )
    plt.legend()
    plt.xlabel("Book Length")
    plt.ylabel("Number of unique words")
    plt.savefig(figfname)

def plot_doc_word_len_hist(doc_wordlens, doc_names, docs2plot, figfname, \
        figsize=(10, 10)):
    """Plot histogram of word lengths for a single document.
    """
    dn_short = get_doc_names_short(doc_names)
    #print(dn_short)
    plt.figure(figsize=figsize)
    for d2p in docs2plot:
        plt.bar(doc_wordlens.index, doc_wordlens[d2p].values, \
                label=dn_short[d2p]
        )
    plt.title("Word Length Histogram")
    plt.xlabel("Word Length")
    plt.ylabel("# of Occurances")
    plt.legend(loc="upper right")
    plt.savefig(figfname)

def plot_doc_wlen_langstack_hist(doc_wordlens, doc_names, figfname, \
        figsize=(10, 10)):
    """Plot average word length histograms across all documents in the
    same language.
    """
    langcol = ["blue", "green", "orange", "red"]
    langmark = ["o", "s", "p", "d"]
    doc_langs, doc_lrsinds = get_lang_start_ind(doc_wordlens, doc_names)
    #print(dn_short)
    doc_lrsinds.append(doc_wordlens.shape[1])
    plt.figure(figsize=figsize)
    # Plot the average word count lengths across all columns of doc_wordlens
    doc_wl_mean = doc_wordlens.mean(axis=1)
    plt.plot(doc_wordlens.index, doc_wl_mean/doc_wl_mean.max(), "k-", \
            label="All Lang.", linewidth=4
    )
    
    for ind, lrsi in enumerate(doc_lrsinds[:-1]):
        doc_wl_mean_bylang = doc_wordlens[ \
                list(range(lrsi-1, doc_lrsinds[ind+1]))].mean(axis=1)
        plt.plot(doc_wordlens.index, \
                doc_wl_mean_bylang/doc_wl_mean_bylang.max(), \
                label=doc_langs[ind], color=langcol[ind], \
                marker=langmark[ind], markersize=10, linewidth=2
        )
        #plt.plot(doc_wordlens.index[[0, -1]], [ind]*2, 'k-', linewidth=1)
    plt.axis([min(doc_wordlens.index)-0.1, max(doc_wordlens.index)+0.1, -0.01, 1.01])
    plt.title("Mean Word Length Histograms by Language")
    plt.xlabel("Word Length")
    plt.ylabel("mean(Count)/max(mean(Count))")
    plt.legend(loc="upper right")
    plt.savefig(figfname)

def get_alldocs_img_yticks(doc_wordlens, doc_names):
    y_ticks = []
    y_ticklabels = []
    for ci, cn in enumerate(doc_wordlens.columns):
        lang = doc_names[cn].split("_")[0]
        if lang not in y_ticklabels:
            y_ticks.append(ci+1)
            y_ticks.append(0)
            y_ticklabels.append(str(ci+1))
            y_ticklabels.append(lang)
    y_ticks.append(doc_wordlens.shape[1])
    y_ticks_new = []
    for ind in range(len(y_ticks)): 
        if y_ticks[ind] == 0:
            y_ticks_new.append( \
                    int((y_ticks[ind-1]+y_ticks[ind+1])/2)
            )
        else:
            y_ticks_new.append(y_ticks[ind])
    #y_ticklabels.append(str(doc_wordlens.shape[1]))
    return (y_ticks_new[:-1], y_ticklabels)

def plot_alldocs_word_len_img(doc_wordlens, doc_names, figfname, \
        figsize=(10, 10)):
    """Plot occurance of word lengths versus word length for ALL Documents as
    an image (i.e. using pcolor).  Normalize each document's word count 
    occurance by the maximum occurance, so that each row of image is scaled 
    between zero and one.
    """
    doc_wordlens_max = doc_wordlens.max()
    doc_wordlens_nrm = doc_wordlens / doc_wordlens_max
    np_wordlens = doc_wordlens_nrm.as_matrix().transpose()
    plt.figure(figsize=figsize)
    plt.pcolor(range(min(doc_wordlens.index), max(doc_wordlens.index)+2), \
            range(1, doc_wordlens.shape[1]+2), np_wordlens)
    plt.axis([1, max(doc_wordlens.index)+1, 1, doc_wordlens.shape[1]+1])
    plt.title("Word Length Histograms for ALL Documents")
    plt.xlabel("Word Length")
    # Make y axis ticks and ticklabels that associate each document with 
    # its language
    y_ticks, y_ticklabels = get_alldocs_img_yticks(doc_wordlens, doc_names)
    #print(y_ticks_new)
    #print(y_ticklabels)
    plt.yticks(y_ticks, y_ticklabels)
    #plt.ylabel("Doc# Range for each Language", position=(0.5, 0.5))
    clb = plt.colorbar()
    clb.ax.set_title("Cnt/max(Cnt)", position=(1, 1.01))
    plt.savefig(figfname)

##############################################################################
# III) If this file is run from command line, execute script below here
if __name__ == "__main__":
    ## Run script for computing statistics on documents in folder hierarchy
    ## Inputs
    # Input Parameters
    root_dir = "/Users/frederickpearce/Documents/PythonProjects/HarvardX/PythonForResearch/Language_Processing"
    doc_dir = "Books"
    # Analysis Parameters
    wordlen_minmax = (1, 16)
    # Output Parameters
    figfname1 = "docstats_bylang_hw2.png"
    docs2plot = ["Doc1", "Doc2"]
    figfname2 = "word_length_ave_bylang.png"
    figfname3 = "word_length_alldocs_img.png"
    
    ## Analysis
    (doc_stats, doc_wordlens, doc_names) = get_doc_stats( \
            wordlen_minmax, root_dir+"/"+doc_dir
    )
    
    ## Outputs
    print("\n\nAnalysis Output")
    print("\nGeneral Word Statistics for first five Documents\n")
    print(doc_stats.head())
    print("\nWord Length (WL) Distribution for first five WLs and ALL Documents\n")
    print(doc_wordlens.head())
    print("\nGenerating Figures\n")
    plot_docstats_bylanguage(doc_stats, root_dir+"/"+figfname1)
    #plot_doc_word_len_hist(doc_wordlens, doc_names, docs2plot, root_dir+"/"+figfname2)
    plot_alldocs_word_len_img(doc_wordlens, doc_names, root_dir+"/"+figfname3)
    plot_doc_wlen_langstack_hist(doc_wordlens, doc_names, root_dir+"/"+figfname2)
    print("\nAnalysis Complete!\n")

