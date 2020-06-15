#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class spacy_arglex(object):
    
    def __init__(self, object):
        self.nlp = object.load("en_core_web_sm")
        
        # Set Document Extensions
        object.tokens.Doc.set_extension("opinion", default = [], force = True)
        
        # Set Span extensions
        object.tokens.Span.set_extension("assessment", default = None, force = True)
        
        # Set Token Extensions
        object.tokens.Token.set_extension("is_emo", getter = lambda token: token.lemma_
                            in ('like', 'adore', 'want', 'prefer', 'love', 'enjoy',
                               'adoration', 'want', 'preference', 'love', 'enjoyment',
                               'hate', 'dislike', 'disprefer', 'dispreference'), force = True)

        object.tokens.Token.set_extension("is_intensifier", getter = lambda token: token.lemma_
                            in ('absolutely', 'absurdly', 'resoundingly', 'amazingly', 
                                'awfully', 'extremely', 'completely', 'highly', 'incredibly', 
                                'perfectly', 'quite', 'really', 'strikingly', 'surprisingly', 
                                'terribly', 'totally', 'unbelievably', 'hugely', 'unnaturally', 
                                'unusually', 'utterly', 'very', 'tremendously', 'spectacularly',
                                'absolute', 'extreme', 'incredible', 'perfect', 'phenomenal', 
                                'spectacular', 'huge', 'major', 'tremendous', 'complete', 'considerable',
                                'real', 'terrible', 'total', 'unbelievable', 'utter', 'great', 'resounding'
                                ), force = True)

        object.tokens.Token.set_extension("is_spoken", getter = lambda token: token.lemma_
                            in ('uh,um', 'mm-hmm', 'uh-huh', 'huh'), force = True)
        
        opinion_tag = Assessment(self.nlp)
        self.nlp.add_pipe(op_tag, last = True)
