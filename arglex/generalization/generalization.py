#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Generalization(object):
    
    def __init__(self, nlp, object):
        self.object = object
        self.matcher = object.matcher.Matcher(nlp.vocab)
        self.matcher.add("Generalization", None,
                    
        #(everybody|everything|anybody|anything|nobody|nothing) (else|at all)
        [{'LOWER': {'IN':['everybody', 'everything', 'anybody', 'anything', 'nobody', 'nothing']}},
         {'LOWER': {'IN':['else', 'at']}}],
                         
        #in the (world|universe)
        [{'LOWER': 'in'},
         {'LOWER': 'the'},
         {'LOWER': {'IN':['world', 'universe']}}],
        
        #of all times
        [{'LOWER': 'of'},
         {'LOWER': 'all'},
         {'LOWER': 'times'}],
                         
        #in recent memory
        [{'LOWER': 'in'},
         {'LOWER': 'recent'},
         {'LOWER': 'memory'}],
                         
        #in living history
        [{'LOWER': 'in'},
         {'LOWER': 'living'},
         {'LOWER': 'history'}]
        
            )
    
    def __call__(self, doc):
        matches = self.matcher(doc)
        
        for match_id, start, end in matches:
            sents = self.object.tokens.Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = self.object.tokens.Span(doc, sent_start, sent_end, label = "GENERALIZATION")
            doc._.opinion.append(opinion,)
        return doc
