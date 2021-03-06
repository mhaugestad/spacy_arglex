#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Priority(object):
    
    def __init__(self, nlp, object):
        self.object = object
        self.matcher = object.matcher.Matcher(nlp.vocab)
        self.matcher.add("Priority", None,

        #important
        [{'LOWER': 'important'}],
                         
        #crucial
        [{'LOWER': 'crucial'}],
                         
        #key
        [{'LOWER': 'key'}],                 

        #essential
        [{'LOWER': 'essential'}],
                         
        #critical
        [{'LOWER': 'critical'}],
                         
        #fundamental
        [{'LOWER': 'fundamental'}],
                         
        #key
        [{'LOWER': 'key'}],                 
        
        #major
        [{'LOWER': 'major'}],                 
        
        #vital
        [{'LOWER': 'vital'}],
                         
        #first and foremost
        [{'LOWER': 'first'},
         {'LOWER': 'and'},
         {'LOWER': 'foremost'}],                 
        
        #(now )?remember (that)?
        [{'LOWER': 'now', 'OP':'?'},
         {'LOWER': 'remember'}],  
                         
        #keep in mind (that)?
        [{'LOWER': 'keep'},
         {'LOWER': 'in'},
         {'LOWER': 'mind'}], 
                         
        #don\'t forget (that)?
        [{'LOWER': 'do'},
         {'LOWER': 'not'},
         {'LOWER': 'forget'}], 
                         
        #let\'s not forget
        [{'LOWER': 'let'},
         {'LOWER': 'us'},
         {'LOWER': 'not'},
         {'LOWER': 'forget'}], 
                         
        #let\'s keep in mind
        [{'LOWER': 'let'},
         {'LOWER': 'us'},
         {'LOWER': 'keep'},
         {'LOWER': 'in'},
         {'LOWER': 'mind'}], 
                                          
        #let\'s remember
        [{'LOWER': 'let'},
         {'LOWER': 'us'},
         {'LOWER': 'remember'}], 
              
    )
    
    def __call__(self, doc):
        matches = self.matcher(doc)
        
        for match_id, start, end in matches:
            sents = self.object.tokens.Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = self.object.tokens.Span(doc, sent_start, sent_end, label = "PRIORITY")
            doc._.opinion.append(opinion,)
        return doc
