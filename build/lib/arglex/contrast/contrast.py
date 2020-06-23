#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Contrast(object):
    
    def __init__(self, nlp, object):
        self.object = object
        self.matcher = object.matcher.Matcher(nlp.vocab)
        self.matcher.add("Contrast", None,
            
            # really, actually
            [{'LOWER':{'IN':['really', 'actually']}}],

            #as opposed to
            [{'LOWER': 'as'},
             {'LOWER': 'oppsed'},
             {'LOWER': 'to'}],

            #instead of
            [{'LOWER': 'instead'},
             {'LOWER': 'of'}],
                         
            #rather than
            [{'LOWER': 'rather'},
             {'LOWER': 'than'}],

            #there (are|is) ([\w]+[ \,]*){1,4} and (then )?there (are|is)
            [{'LOWER': 'there'},
             {'LEMMA': 'be'},
             {'IS_ASCII':True, 'OP':'+'},
             {'LOWER': 'and'},
             {'LOWER': 'then', 'OP':'?'},
             {'LOWER': 'there'},
             {'LEMMA': 'be'}],

            #(is|that\'s|it\'s) a whole nother issue
            [{'LOWER': {'IN':['that', 'it']}},
             {'LEMMA': 'be'},
             {'LOWER': 'a'},
             {'LOWER': 'whole'},
             {'LOWER': 'nother'},
             {'LOWER': 'issue'}],

            #(is|are|that\'s|it\'s) (very|quite|completely|totally )?different
            [{'LEMMA': 'be'},
             {'LOWER': {'IN':['very', 'quite', 'completely', 'totally']}},
             {'LOWER': 'different'}],

            #whole new ballgame
            [{'LOWER': 'whole'},
             {'LOWER': 'new'},
             {'LOWER': 'ballgame'}],
                         
            #(is|that\'s|it\'s) a (separate|different) (issue|question)
            [{'LEMMA': 'be'},
             {'LOWER': 'a'},
             {'LOWER': {'IN': ['separate', 'different']}},
             {'LOWER': {'IN': ['issue', 'question']}}
              ]
          
        )
    
    def __call__(self, doc):
        matches = self.matcher(doc)
        
        for match_id, start, end in matches:
            sents = self.object.tokens.Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = self.object.tokens.Span(doc, sent_start, sent_end, label = "CONTRAST")
            doc._.opinion.append(opinion,)
        return doc
