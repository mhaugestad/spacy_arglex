#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Inyourshoes(object):
    
    def __init__(self, nlp, object):
        
        self.matcher = object.matcher.Matcher(nlp.vocab)
        self.matcher.add("Inyourshoes", None,
                    
        #what i would do
        [{'LOWER': 'what'},
         {'LOWER': 'i'},
         {'LOWER': 'would'},
         {'LOWER': 'do'}],
        
        # if i were you
        [{'LOWER': 'if'},
         {'LOWER': 'i'},
         {'LOWER': 'were'},
         {'LOWER': 'you'}],
        
        # i would not
        [{'LOWER': 'i'},
         {'LOWER': 'would'},
         {'LOWER': 'not'}]           
    )
    
    def __call__(self, doc):
        matches = self.matcher(doc)
        
        for match_id, start, end in matches:
            sents = Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = Span(doc, sent_start, sent_end, label = "INYOURSHOES")
            doc._.opinion.append(opinion,)
        return doc
