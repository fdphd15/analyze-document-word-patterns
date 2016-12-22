analyze_document_word_patterns.py
======
**analyze_document_word_patterns.py** is a script for analyzing patterns in the
structure of text documents with the goal of identifying characteristic 
text features (i.e. predictors) that can be used for document modeling (e.g. 
classification). It performs three basic tasks: 1) Load each document and any 
metadata that describes it, 2) Analyze each document by first preprocessing it,
and then extracting text features that describe its structure in meaningful 
ways, and 3) Write outputs as a report printed to screen, and as histograms, 
images, etc. written to file. 

This project was inspired by a case study on Language Processing, part of the
HarvardX course on "Using Python for Research" by JP Onnela and the PH526x 
team. The example data included in this repository (see ./Books) uses the same 
books data from the course, a set of famous literary works written in different 
languages, which were originally obtained from the Gutenberg Project: 
https://www.gutenberg.org.  

I hope this project grows into a full fledged text analytics toolbox, with 
interesting new document data sets for testing, and exciting new tools for 
analytics, visualizations, modeling, etc.

Analysis Example

The analysis example included here examines the distribution of word lengths 
across all book documents, and across different categorical variables, such as
the document language. The data is first preprocessed to remove capitalization,
separate out punctuation, etc., and then the word length distribution is 
calculated and visualized.  

Running the script with the example data produces the figure below, showing the 
word length distribution for each document in the data set in an image format. 
The x-axis of the image corresponds to the length of each word.  For example, 
"a document with only these words in quotes" would have a word length 
distribution of [1: 1, 2: 1, 3: 0, 4: 2, 5: 2, 6: 1, 7: 0, 8: 1], since the 
sentence contains one word with one letter, one word with two letters, zero 
words with three letters, two words with four letters, etc. 

Each horizontal row of pixels in the image shows how the distribution of word 
lengths varies for a given book, with the different colors denoting the # of
words of a given length, normalized by the maximum # of words across all 
word lengths. In the above example, this would lead to [1: 0.5, 2: 0.5, 3: 0, 
4: 1, 5: 1, 6: 0.5, 7: 0, 8: 0.5]. Thus, the most frequent word length in each 
document (row) is dark red (value of 1), while the least frequent word length 
in each document (value of zero) is dark blue .
 
The y-axis of the image identifies the individual books by their id number, 
which is sorted by language, such that the id number 1 shown in the figure 
corresponds to the first book (row) written in English, the id number 8 denotes
the first book (row) written in French, etc. 

Examining a single column shows how the normalized occurance of each word 
length varies across all the books.  For example, the leftmost vertical column 
of the image describes the relative frequency of words with only one letter. 
The proportion of words with only one letter is highest in Portugese (orange, 
50-70% of max. value) while it is lowest for German (dark blue, less than 10%
of max. value).

The most prominent characteristic of the word length distributions is their 
strong dependence on language. Each document written in the same language 
has a very similar word length distribution, a type of structural fingerprint
that identifies each language.  Thus, analytics, or features, derived from the
word length distribution would be good predictor(s) for classifying document 
language, at least for the languages we've analyzed thus far...

It would be interesting to see if different types of documents, such as emails 
or newspaper articles, show the same distinguishing word length distribution 
dependency versus document language.

![Example Figure](https://github.com/fdphd15/analyze-document-word-patterns/blob/master/word_length_alldocs_img.png)

## Usage
* Download a copy from github

```
$ git clone https://github.com/fdphd15/analyze-document-word-patterns.git
```

* Run the example

```
$ python3 ./analyze_doc_words.py
```

## Version 
* Version 0.1 - Created on 09/17/2016 by Frederick D. Pearce (FDP)
                This version used to seed github repository.
                Basic functionality for analyzing and visualizing word 
                length distributions across all documents and as a function
                of document language.
## License 

* Copyright 2016 Frederick D. Pearce
* Licensed under the Apache License, Version 2.0 (the "License")
* You may obtain a copy of the License from
[LICENSE](https://github.com/fdphd15/analyze-document-word-patterns/blob/master/LICENSE.md) or
[here](http://www.apache.org/licenses/LICENSE-2.0)
 
## Contact
#### Frederick D. Pearce
* e-mail: fdphd15@users.noreply.github.com

