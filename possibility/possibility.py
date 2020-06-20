#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Possibility(object):
    
    def __init__(self, nlp, object):
        
        self.matcher = object.matcher.Matcher(nlp.vocab)
        self.matcher.add("Possibility", None,
        
        #you can
        [{'LOWER': 'you'},
         {'LOWER': 'can'}],                
        
        #we can
        [{'LOWER': 'we'},
         {'LOWER': 'can'}],                  
        
        #you can\'t
        [{'LOWER': 'you'},
         {'LOWER': 'can'},
         {'LOWER': 'not'}],                   
        
        #you cannot
                         
        #we can\'t
        [{'LOWER': 'we'},
         {'LOWER': 'can'},
         {'LOWER': 'not'}],                  
        
        #we cannot
                         
        #you could
        [{'POS': 'PRON'},
         {'LOWER': 'could'}],                  
        
        #we could
                         
        #(@BE) able to
        [{'LEMMA': 'be'},
         {'LOWER': 'able'},
         {'LOWER': 'to'}],
                         
        #there\'s no way (that|for|of|to)?
        [{'LOWER': 'there'},
         {'LEMMA': 'be'},
         {'LOWER': 'no'},
         {'LOWER': 'way'},
         {'LOWER': {'IN':['that', 'for', 'of', 'to']}}],
                         
        #any way (that|for|of|to)?
        [{'LOWER': 'any'},
         {'LOWER': 'way'},
         {'LOWER': {'IN':['that', 'for', 'of', 'to']}}],
                         
        #no way
        [{'LOWER': 'no'},
         {'LOWER': 'way'}],                 
    )
    
    def __call__(self, doc):
        matches = self.matcher(doc)
        
        for match_id, start, end in matches:
            sents = Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = Span(doc, sent_start, sent_end, label = "POSSIBILITY")
            doc._.opinion.append(opinion,)
        return doc
