analyze_document_word_patterns.py
======
**analyze_document_word_patterns.py** is a script for analyzing patterns in the 
words contained within a collection of text documents (e.g. books) located in a 
hierarchical folder structure.  Current implementation focuses on identifying
the relationship between the distribution of word lengths and the language the 
document was written in. This project is an extension of a case study and 
homework problem on Language Processing given as part of the HarvardX course 
entitled "Using Python for Research" taught by JP Onnela and the PH526x team.

This repository includes an example that uses the data provided in the course: 
a set of famous books in several different languages (English, French, German, 
and Portugese) that were obtained from The Gutenberg Project.  The example 
code provided, analyze_doc_words.py, computes the word length distribution 
across all the documents, and visualizes the results through histograms and 
images. Each language has a unique word length distribution signature that can 
be used to classify the language of unknown, test documents.

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

