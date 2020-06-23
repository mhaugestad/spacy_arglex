#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Inconsistency(object):
    
    def __init__(self, nlp, object):
        self.object = object
        self.matcher = object.matcher.Matcher(nlp.vocab)
        self.matcher.add("Inconsistency", None,
                    
        #except that
        [{'LOWER': 'except'},
         {'LOWER': 'that'}],
        
        # except for
        [{'LOWER': 'except'},
         {'LOWER': 'for'}],
                         
        # with the exception of
        [{'LOWER': 'with'},
         {'LOWER': 'the'},
         {'LOWER': 'exception'},
         {'LOWER' : 'of'}],
                         
        # however
        [{'LOWER': 'however'}],

        # nevertheless
        [{'LOWER': 'nevertheless'}],
                         
        # that said
        [{'LOWER': 'that'},
         {'LOWER': 'said'}],
                         
        # that having been said
        [{'LOWER': 'that'},
         {'LOWER': 'having'},
         {'LOWER': 'been'},
         {'LOWER': 'said'}],
                         
        # that being said
        [{'LOWER': 'that'},
         {'LOWER': 'being'},
         {'LOWER' : 'said'}],                 
        
        # despite
        [{'LOWER': 'despite'}],                 
        
        # in spite of
        [{'LOWER': 'in'},
         {'LOWER': 'spite'},
         {'LOWER': 'of'}],
                         
        # even so
        [{'LOWER': 'even'},
         {'LOWER': 'so'}],                 
        
        # at the same time
        [{'LOWER': 'at'},
        {'LOWER': 'the'},
        {'LOWER': 'same'},
        {'LOWER': 'time'}],
                         
        # still
        [{'LOWER': 'still'}],
                         
        # wait a minute
        [{'LOWER': 'wait'},
        {'LOWER': 'a'},
        {'LOWER': 'minute'}],                 
                         
        # hold on a second
        [{'LOWER': 'hold'},
         {'LOWER': 'on'},
         {'LOWER': 'a'},
         {'LOWER': 'second'}],                 
                         
        # hold on a sec
        [{'LOWER': 'hold'},
         {'LOWER': 'on'},
         {'LOWER': 'a'},
         {'LOWER': 'sec'}],                   
                         
        # it\'s just that
        [{'LOWER': 'it'},
         {'LOWER': 'is'},
         {'LOWER': 'just'},
         {'LOWER': 'that'}],                 
                         
        # all well and good
        [{'LOWER': 'all'},
         {'LOWER': 'well'},
         {'LOWER': 'and'},
         {'LOWER': 'good'}],              
                         
        # as far as it goes
        [{'LOWER': 'as'},
         {'LOWER': 'far'},
         {'LOWER': 'as'},
         {'LOWER': 'it'},
         {'LOWER': 'goes'}],                
                         
        # you might think (that)?
        [{'LOWER': 'you'},
         {'LOWER': 'might'},
         {'LOWER': 'think'}],                 
                         
        # you may think (that)?
        [{'LOWER': 'you'},
         {'LOWER': 'may'},
         {'LOWER': 'think'}]                  
                         
            )
    
    def __call__(self, doc):
        matches = self.matcher(doc)
        
        for match_id, start, end in matches:
            sents = self.object.tokens.Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = self.object.tokens.Span(doc, sent_start, sent_end, label = "INCONSISTENCY")
            doc._.opinion.append(opinion,)
        return doc
