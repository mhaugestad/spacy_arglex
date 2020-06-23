#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Necessity(object):
    
    def __init__(self, nlp, object):
        self.object = object
        self.matcher = object.matcher.Matcher(nlp.vocab)
        self.matcher.add("Necessity", None,
                    
        #a must
        [{'LOWER': 'a', 'OP': '?'},
         {'LOWER': 'must'}],
                         
        #must
                         
        #essential
        [{'LOWER': 'essential'}],
        
        #indispensable
        [{'LOWER': 'essential'}],
        
        #necessary
        [{'LOWER': 'necessary'}],
                         
        #(@BE) a necessity
        [{'LEMMA': 'be'},
         {'LOWER': 'a'},
         {'LOWER': 'necessity'}],
        
        #needed
        [{'LOWER': 'needed'}],
                         
        #required
        [{'LOWER': 'required'}],
        
        #requirement
        [{'LOWER': 'requirement'}],
        
        #can\'t do without
        [{'LOWER': 'can'},
         {'LOWER': 'not'},
         {'LOWER': 'do'},
         {'LOWER': 'without'}],
                         
        #got to
        [{'LOWER': 'got'},
         {'LOWER': 'to'}],
                         
        #gotta 
        [{'LOWER': 'gotta'}],                 
                         
        #had better
        [{'LEMMA': 'have'},
         {'LOWER': 'better'}],
                         
        #hafta
        [{'LOWER': 'hafta'}],
        
        #have to
        [{'LEMMA': 'have'},
         {'LOWER': 'to'}],
                         
        #has to
        
        #need to
        [{'LEMMA': 'need'},
         {'LOWER': 'to'}],
                         
        #needs to
        
        #ought to
        [{'LEMMA': 'ought'},
         {'LOWER': 'to'}],
                         
        #oughta
        [{'LOWER': 'oughta'}],
                         
        #should
        [{'LOWER': 'should'}],
        
        #(@PRONSUBJ) better
        [{'POS': 'PRON'},
         {'LOWER': 'better'}],
        
        #(necesssitates|necessitated|necessitating|necessitate)
        [{'LOWER': {'IN':['necessitates', 'necessitated', 'necessitating', 'necessitate']}}],
    )
    
    def __call__(self, doc):
        matches = self.matcher(doc)
        
        for match_id, start, end in matches:
            sents = self.object.tokens.Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = self.object.tokens.Span(doc, sent_start, sent_end, label = "NECESSITY")
            doc._.opinion.append(opinion,)
        return doc
