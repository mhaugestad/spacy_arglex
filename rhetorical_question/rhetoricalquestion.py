#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class RhetoricalQuestion(object):
    
    def __init__(self, object):
        
        self.matcher = Matcher(object.vocab)
        self.matcher.add("RhetoricalQuestion", None,

                         
        #do (we|you) (actually|really|still) (need|want)
        [{'LEMMA': 'do'},
         {'POS': 'PRON'},
         {'LOWER': {'IN':['actually', 'really', 'still']}},
         {'LOWER': {'IN':['need', 'want']}}],
        
        #why not
        [{'LOWER':'why'},
         {'LOWER': 'not'}],
        
        #why don\'t (we|you)
        [{'LOWER':'why'},
         {'LOWER': "don't"},
         {'POS': 'PRON'}],
        
        #what if
        [{'LOWER':'what'},
         {'LOWER': "if"}],
        
        #(and )?who (wouldn\'t|doesn\'t) (@EMO1V)
        [{'LOWER':'and', 'OP':'?'},
         {'LOWER': "who"},
         {'LEMMA': {'IN':['would', 'do']}},
         {'LOWER': 'not'},
         {'_':{'is_EMO1V':True}}],
              
    )
    
    def __call__(self, doc):
        matches = self.matcher(doc)
        
        for match_id, start, end in matches:
            sents = Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = Span(doc, sent_start, sent_end, label = "RHETORICALQUESTION")
            doc._.opinion.append(opinion,)
        return doc
