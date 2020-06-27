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

doc = nlp('It was my understanding that there would be burgers. According to the WHO burgers are good for you!')

for opinion in doc._.opinion:
  print((opinion, opinion.label_))

(It was my understanding that there would be burgers., 'ASSESSMENT')
(According to the WHO burgers are good for you!, 'AUTHORITY')

```
The module also includes the test patterns provided by the authors which can be accessed through a simple function call. The patterns come in a json file where each key represents the type of opinion expressed, and value a text snippet with a sentence that exemplifies the type of pattern we are supposed to pick up.

```
from arglex import load_test_patterns
test_patterns = load_test_patterns()

for doc in nlp.pipe(test_patterns['contrast']): 
  for opinion in doc._.opinion: 
    print((opinion, opinion.label_))

(uh as opposed to what you'd really want to know if you were gonna use this thing, 'CONTRAST')
(um i think they should be recorded instead of written, 'CONTRAST')
(um i think they should be recorded instead of written, 'NECESSITY')
(so rather than say the most interesting thing something interesting, 'CONTRAST')
(there's a median filtering and then there's a piece-wise linear fit based on some criteria, 'CONTRAST')
(i mean the language model for switchboard is totally different, 'CONTRAST')
(It's a whole new ballgame., 'CONTRAST')

```
Current behaviour of the module is to return a sentence twice if it matches two separate opinion types.

The module also allows for you to pull out individual opinion type patterns and add to your nlp pipeline. Note that some of these patterns requires customised token extensions, therefore you may want to run the set_token_extension first.

```
import spacy
from arglex import set_token_extension
from arglex import Authority

set_token_extension(spacy)

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe(Authority(nlp, spacy), name = 'Authority', last = True)
nlp.pipeline

[('tagger', <spacy.pipeline.pipes.Tagger at 0x115b1de48>),
 ('parser', <spacy.pipeline.pipes.DependencyParser at 0x115b648e8>),
 ('ner', <spacy.pipeline.pipes.EntityRecognizer at 0x115b64948>),
 ('Authority', <arglex.authority.authority.Authority at 0x11920fda0>)]
```

