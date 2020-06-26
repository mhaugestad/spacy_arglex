# spacy_arglex
Project to detect arguments and opinions in corpus based on patterns described by Somasundaran et al. http://mpqa.cs.pitt.edu/lexicons/arg_lexicon/.

The module is built on top of spacy and tag sentences that expresses some argument with its corresponding label.

# Installation
The model requires you to have Spacy and their core language model for english already installed;

```
# pip install spacy
# python -m spacy download en_core_web_sm
git clone https://github.com/mhaugestad/spacy_arglex.git
cd spacy_arglex
python setup.py install
```
# Example
```
from spacy_arglex import arglex
import spacy

nlp = arglex(spacy)

```
