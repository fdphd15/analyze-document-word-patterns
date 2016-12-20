analyze_document_word_patterns.py
======
**analyze_document_word_patterns.py** is a script for analyzing patterns in the
structure of text documents and developing characteristic features (predictors) 
that can be used for document modeling (e.g. document classification). 
This project was inspired by a case study and homework problem on Language 
Processing that I was assigned while a student in the HarvardX course on "Using
Python for Research" by JP Onnela and the PH526x team.

This script performs three basic tasks:
1) Load each document and its metadata, 2) Analyze each document (measure
features) and 3) Output results (histogram plots, images, reports). Step 1 
closely follows the course code, it loads each text document marching through 
the hierarchical folder structure.  
In Step 2, the analysis of the text string within each done here focuses on 
the occurance of words with different lengths.  The data is preprocessed in a 
similar way, for example to separate out punctuation, and then analyzed to 
calculate the value of various text features (predictors), such as the 
occurance of words with different lengths (i.e. word length distribution).
Several tools are included for visualizing the features extracted from each
documents' text. 
This code is part of a larger effort to build a core set of data science tools 
in Python.

The book data contained in this repository were obtained from the Language 
Processing case study portion of the "Using Python for Research" course website
They were originally sourced from the Gutenberg Project: 
https://www.gutenberg.org 

The example book data shown below has a root level labelled with the document type 
(Books), a second level with document language (English, French, German, or 
Portugese), a third level with author name, and a fourth with Book title.
The example code provided, analyze_doc_words.py, computes the word length 
distribution across all the documents, and visualizes the results through histograms and 
images. Each language has a unique word length distribution signature that can 
be used to classify the language of unknown, test documents.

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

