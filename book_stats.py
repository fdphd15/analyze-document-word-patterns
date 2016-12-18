# A script for computing statistics on a collection of documents (books) stored
# in a hierarchical file structure.  Based on the lecture from Case Study #2 in
# the Using Python for Research course by HarvardX
from collections import Counter
import os
import matplotlib.pyplot as plt
import pandas as pd

def count_words(text):
    """
    Count the number of times each word occurs in text (str).  Return a 
    dictionary where keys are unique words and values are the word counts.  
    Input text is converted to lower-case, and all punctuation is skipped.
    """
    text = text.lower()
    punc_to_skip = [". ", ", ", "; ", ": ", " '", "' ", ' "', '" ' "? ", "! ", \
            " - ", " (", ") "]
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
    skipped.
    """
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts

def read_doc(doc_path):
    """
    Read a document and return it as a string.
    """
    with open(doc_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

def word_stats(word_counts):
    """Return number of unique words and word frequencies."""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

def word_distribution(word_counts):
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

def get_doc_stats(root_dir):
    """Get statistics on each document in hierarchical folder structure with
    top level=root_dir.  Return a Pandas DataFrame containing each document's
    language, author, title, total word count, number of unique words, and 
    word count distribution.
    Hidden folders and files are not included (i.e. those starting with .)
    The example below is designed for the book folder structure from the HW2
    of the Using Python for Research course.  Modify accordingly for other
    document folder structures!
    """
    stats = pd.DataFrame(columns = ("language", "author", "title", "length", \
            "unique"
    ))
    doc_num = 1
    languages = [val for val in os.listdir(root_dir) if val[0] != "."]
    for lang in languages:
        authors = [val for val in os.listdir(root_dir+"/"+lang) if val[0] != "."]
        for auth in authors:
            titles = [val for val in os.listdir(root_dir+"/"+lang+"/"+auth) if val[0] != "."]
            for titl in titles:
                inputfile = "/".join((root_dir, lang, auth, titl))
                print(inputfile) 
                count_words = count_words_fast(read_doc(inputfile))
                (num_unique, counts) = word_stats(count_words)
                word_dis = word_distribution(count_words)
                stats.loc[doc_num] = lang, auth.capitalize(), titl[:-4], \
                        sum(counts), num_unique
                doc_num += 1 
    return stats, word_dis

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

if __name__ == "__main__":
    # Run script for computing statistics on documents in folder hierarchy
    root_dir = "/Users/frederickpearce/Documents/PythonProjects/HarvardX/PythonForResearch/Language_Processing"
    doc_dir = "Books"
    figfname = "docstats_bylang.png"
    doc_stats, word_dis = get_doc_stats(root_dir+"/"+doc_dir)
    print(word_dis)
    # Outputs
    print(doc_stats.head())
    plot_docstats_bylanguage(doc_stats, root_dir+"/"+figfname)

