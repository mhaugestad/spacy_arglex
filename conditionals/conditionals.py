#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Conditionals(object):
    
    def __init__(self, object):
        
        self.matcher = Matcher(object.vocab)
        self.matcher.add("Conditionals", None,
            
            # if (we|you) want to ([\w]+[ \,]+){1,7}(we|you) (need to|must|have to)
            [{'LOWER':'if'},
            {"LOWER": {'IN':['we', 'you']}}, 
            {'LOWER': 'want'},
            {'LOWER': 'to'},
            {'IS_ALPHA': True, 'OP':'+'},
            {'LOWER', {'IN':['we', 'you']}},
            {'LOWER': {'IN':['need', 'must', 'have'}],

            #(we|you) ([\w ,]+) (must|have to|need to) ([\w]+[ \,]+){1,7}if  (you|we) want to                    
            [{'LOWER':{'IN':['we', 'you']}},
            {'IS_ALPHA': True, 'OP':'+'},
            {'LOWER': {'IN':['need', 'must', 'have'}},
            {'LOWER': 'to', 'OP':'?'},
            {'IS_ALPHA': True, 'OP':'+'},
            {'LOWER': 'if'},
            {'LOWER':{'IN':['we', 'you']}}
            {'LOWER' : 'want'},
            {'LOWER': 'to'}],

            # it would be ([\w]+[ \,]+){0,2}nice if
            [{'LOWER': 'it'},
             {'LOWER': 'would'},
             {'LEMMA': 'be'}],

            # wouldn\'t it be ([\w]+[ \,]+){0,2}nice if
            [{'DEP': 'poss'},
             {'LOWER': 'take'},
             {'LOWER': 'on'}],

            # if ([\w]+[ \,]+){3,8} that would be ([\w]+[ \,]+){0,2}nice
            [{'LOWER': 'it'},
             {'LEMMA': 'seem'},
             {'LOWER': 'to'},
             {'POS': 'PRON'},
             {'LOWER': 'that', 'OP':'?'}],

            # (cannot|will not|won\'t|can\'t) ([\w]+[ \,]+){1,7}(if|unless)
            [{'LOWER': 'it'},
             {'LEMMA': 'seem'},
             {'LOWER': 'that', 'OP':'?'}],

            # (if|unless) ([\w]+[ \,]+){3,10}(cannot|will not|won\'t|can\'t)
            [{'LOWER': 'it'},
             {'LOWER': 'would'},
             {'LOWER': 'seem'},
             {'LOWER': 'to'},
             {'POS': 'PRON', 'OP':'?'}],

            # (need|needs|must|has to|have to) ([\w]+[ \,]+){3,10}(in order )to
            [{'LOWER': 'it'},
             {'LOWER': 'would'},
             {'LOWER': 'appear'},
             {'LOWER': 'to'},
             {'POS': 'PRON', 'OP':'?'}],

            # (in order )?to ([\w]+[ \,]+){3,10}(need|needs|must|has to|have to)
            [{'LOWER': 'it'},
             {'LEMMA': 'appear'},
             {'LOWER': 'to'},
             {'POS': 'PRON', 'OP':'?'}],

            # as long as (we|you) ([\w]+[ \,]+){3,10}(will|can|able|should|[a-zA-Z]+\'ll)
            [{'DEP': {'IN':['poss', 'det']}},
             {'IS_ALPHA': True, 'OP':'?'},
             {'LOWER': 'point'},
             {'LEMMA': 'be'},
             {'LOWER': 'that', 'OP':'?'}],

            # ([a-zA-Z]\'ll|will|can|able|should) ([\w]+[ \,]+){3,10}as long as (we|you) 
            [{'LOWER': 'it'},
             {'LEMMA': 'look'},
             {'LOWER': 'to'},
             {'POS':'PRON'},
             {'LOWER': 'like'}],

            #(you|he|we) better ([\w]+[ \,]+){3,10}or
            [{'POS': 'PRON'},
             {'LEMMA': {'IN':['have', 'get']}},
             {'LOWER': 'the'},
             {'LOWER':'impression'},
             {'LOWER': 'that', 'OP':'?'}],

            # otherwise
            [{'DEP': 'poss'},
             {'LOWER':'impression'},
             {'LEMMA': 'be'},
             {'LOWER': 'that'}]
        )
    
    def __call__(self, doc):
        matches = self.matcher(doc)
        
        for match_id, start, end in matches:
            sents = Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = Span(doc, sent_start, sent_end, label = "COND")
            doc._.opinion.append(opinion,)
        return doc
