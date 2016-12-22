analyze_document_word_patterns.py
======
**analyze_document_word_patterns.py** is a script for analyzing patterns in the
structure of text documents with the goal of identifying characteristic 
text features (i.e. predictors) that can be used for document modeling (e.g. 
classification). It performs three basic tasks:

1) Load each document and any metadata that describes it, 
2) Analyze each document by first preprocessing it, and then extracting text 
features that describe its structure in meaningful ways, and 
3) Write outputs as a report printed to screen, and as histograms, images, etc. 
written to file. 

I hope this project grows into a full fledged text analytics toolbox, with 
interesting new document data sets for testing, and exciting new tools for 
analytics, visualizations, modeling, etc.

This project was inspired by a case study and homework problem on Language 
Processing that I worked on while a student in the HarvardX course on "Using
Python for Research" by JP Onnela and the PH526x team. The example data 
included in this repository (see Books dir) uses the same books data as the 
course, a set of famous literary works written in different languages, which 
were originally obtained from the Gutenberg Project: https://www.gutenberg.org.  

The analysis performed here examines the distribution of word lengths across 
all the documents, and also as a function of different categorical variables, 
such as the document language. The data is first preprocessed to separate out 
punctuation, etc., and then the word length distribution is calculated.  

Running the script using the example data produces several outputs, one of which
is the example figure shown below.  This figure provides a detailed view of the 
(normalized) word length distribution for every document in the data set, 
visualized in the form of an image. The x-axis identifies the length of each 
word (for example, "word" has four letters so a length of four, etc.), so each 
horizontal row of the image shows the distribution of word lengths for a given 
book.  The y-axis identifies each book in the data set by their id number, 
which have been sorted by language.  For example, the id number 1 corresponds
to the first book written in English, the id number 8 denotes the first book 
written in French, etc.

The most prominent characteristic of the word length distributions is their 
strong dependence on language, each language tightly clusters around its own 
unique word length distribution (i.e. a structural fingerprint).  Thus, 
analytics, or features, extracted from the word length distribution would 
be excellent predictor(s) for classifying document language, at least for the 
languages we've analyzed thus far...

It would be interesting to see if different types of documents, such as emails 
or newspaper articles, show the same word length distribution dependency versus 
document language.

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

