analyze_document_word_patterns.py
======
**analyze_document_word_patterns.py** is a script for analyzing patterns in the
structure of text documents with the goal of identifying characteristic 
text features (i.e. predictors) that can be used for document modeling (e.g. 
classification). 
This project was inspired by a case study and homework problem on Language 
Processing that I worked on while a student in the HarvardX course on "Using
Python for Research" by JP Onnela and the PH526x team.

This script performs three basic tasks, parts of its code and layout  are 
similar to codes presented in the course (see individual function docstrings 
for additional details):
1) Load each document and its metadata, 
2) Analyze each document by first preprocessing it, and then extracting text 
features that describe its structure in meaningful ways, and 
3) Write output as report printed to screen, and as histograms, images, etc. 
written to file. 

The example data included in this repository is a set of books written in 
different languages by many different authors.  This is the same data that 
was included as part of the "Using Python for Research" course; however, 
we perform a different, complementary analysis, as described below. 
The data is located in the "./Books" directory of this repository. It was 
originally obtained from the Gutenberg Project: https://www.gutenberg.org
The folder structure is as follows: the first level is Books, the second level
is the document language (English, French, German, or Portugese), the third 
level is author name, and the fourth level is book title.

The analysis performed here examines the distribution of word lengths across 
all the documents, and also as a function of different categorical variables, 
such as the document language. The data is first preprocessed to separate out 
punctuation, etc., and then the word length distribution is calculated.  

Running the script with the example data produces several outputs, one of which
is the example figure shown below.  This figure provides a detailed view of the 
word length distributions across all documents (normalized by its max.) in the 
form of an image. Each horizontal row of the image corresponds to the word 
length distribution of a particular document (book) written in a particular 
language, etc. The most prominent relationship is that each language appears to
have its own, characteristic word length distribution, meaning this text
feature would be a key predictor for document language classification, at least 
for the languages we've analyzed thus far...

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

