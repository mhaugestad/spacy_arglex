#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Doubt(object):
    
    def __init__(self, object):
        
        self.matcher = Matcher(object.vocab)
        self.matcher.add("Assessment", None,
                        
            #(i am|i\'m) not (sure|convinced)
            [{'POS':'PRON'},
            {"LEMMA": 'be'}, 
            {'LOWER': 'not'},
            {'LOWER': {'IN':['sure', 'convinced']}}],
            
            #i (don\'t|can\'t|do not|cannot) see how
            [{'POS':'PRON'},
            {"LEMMA": {'IN':['do', 'can']}}, 
            {'LOWER': 'not'},
            {'LOWER': 'see'},
            {'LOWER' : 'how'}],

            #it (is not|isn\'t) (clear|evident|obvious) (that)?
            [{'LOWER':'it'},
            {"LEMMA": 'be'}, 
            {'LOWER': 'not'},
            {'LOWER': {'IN':['clear', 'evident', 'obvious']}},
            {'LOWER' : 'that', 'OP':'?'}],
                         
            #(we|i) doubt (that)?
            [{'POS':'PRON'},
            {"LOWER": 'doubt'}, 
            {'LOWER' : 'that', 'OP':'?'}],
                         
            #(we|i) (am|are) doubtful
            [{'POS':'PRON'},
             {'LEMMA': 'be'},
             {"LOWER": 'doubtful'}]
        )
    
    def __call__(self, doc):
        matches = self.matcher(doc)
        
        for match_id, start, end in matches:
            sents = Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = Span(doc, sent_start, sent_end, label = "DOUBT")
            doc._.opinion.append(opinion,)
        return doc
