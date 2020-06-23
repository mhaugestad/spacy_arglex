#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Doubt(object):
    
    def __init__(self, nlp, object):
        self.object = object
        self.matcher = object.matcher.Matcher(nlp.vocab)
        self.matcher.add("Doubt", None,
                        
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
            {'LOWER': {'IN':['clear', 'evident', 'obvious']}}],
                         
            #(we|i) doubt (that)?
            [{'POS':'PRON'},
            {"LOWER": 'doubt'}],
                         
            #(we|i) (am|are) doubtful
            [{'POS':'PRON'},
             {'LEMMA': 'be'},
             {"LOWER": 'doubtful'}]
        )
    
    def __call__(self, doc):
        matches = self.matcher(doc)
        
        for match_id, start, end in matches:
            sents = self.object.tokens.Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = self.object.tokens.Span(doc, sent_start, sent_end, label = "DOUBT")
            doc._.opinion.append(opinion,)
        return doc
