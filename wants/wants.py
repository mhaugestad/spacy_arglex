#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Wants(object):
    
    def __init__(self, nlp, object):
        
        self.matcher = object.matcher.Matcher(nlp.vocab)
        self.matcher.add("Wants", None,
                    
            #(you|we|i) (don\'t )?(want|wanna)
            [{'POS':'PRON'},
             {'LOWER': 'do'},
             {'LOWER': 'not'},
             {'LEMMA': 'want'}],
            #(you|we|i) might (not )?(want|wanna)
            [{'POS':'PRON'},
             {'LOWER': 'might'},
             {'LOWER': 'not'},
             {'LEMMA': {'IN':['want', 'wanna']}}],
                         
        )
    
    def __call__(self, doc):
        matches = self.matcher(doc)
        
        for match_id, start, end in matches:
            sents = Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = Span(doc, sent_start, sent_end, label = "WANTS")
            doc._.opinion.append(opinion,)
        return doc
