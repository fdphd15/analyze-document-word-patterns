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
features) and 3) Output results (histogram plots, images, reports). 

An example is included that analyzes book data in different languages.  This 
dataset was provided as part of the Language Processing case study assignment 
in the "Using Python for Research" course, and was originally sourced from the 
Gutenberg Project: https://www.gutenberg.org 

The code starts by loading the text contained within each document, marching 
automatically through the provided hierarchical folder structure. The example 
book data shown below has a root level named Books, a second level with 
document language (English, French, German, or Portugese), a third level with 
author name, and a fourth level with Book title.
Next, the text string within each document is analyzed to extract certain
features that describe it.  Here we deviate from the course and instead focus 
on how frequently words with different lengths occur within each document.  
The data is still preprocessed to separate out punctuation, prior to 
calculating the word length distribution.  
Finally, the output of the analysis is printed to the screen, and a couple of 
figures are produced that show the word length distributions across all 
documents in the form of an image (below) and as a line plot versus language.
Note that each language is uniquely identified by a characteristic word length 
distribution that can be used to classify unknown, test documents.

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

