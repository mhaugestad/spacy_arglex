#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Conditionals(object):
    
    def __init__(self, nlp, object):
        self.object = object
        self.matcher = object.matcher.Matcher(nlp.vocab)
        self.matcher.add("Conditionals", None,
            
            # if (we|you) want to ([\w]+[ \,]+){1,7}(we|you) (need to|must|have to)
            [{'LOWER':'if'},
            {"POS": 'PRON'}, 
            {'LEMMA': 'want'},
            {'LOWER': 'to'},
            {'IS_ALPHA': True, 'OP':'+'},
            {'POS': 'PRON'},
            {'LEMMA': {'IN':['need', 'must', 'have']}}],

            #(we|you) ([\w ,]+) (must|have to|need to) ([\w]+[ \,]+){1,7}if  (you|we) want to                    
            [{'LOWER':{'IN':['we', 'you']}},
            {'IS_ALPHA': True, 'OP':'+'},
            {'LOWER': {'IN':['need', 'must', 'have']}},
            {'LOWER': 'to', 'OP':'?'},
            {'IS_ALPHA': True, 'OP':'+'},
            {'LOWER': 'if'},
            {'LOWER':{'IN':['we', 'you']}},
            {'LOWER' : 'want'},
            {'LOWER': 'to'}],

            # it would be ([\w]+[ \,]+){0,2}nice if
            [{'LOWER': 'it'},
             {'LOWER': 'would'},
             {'LEMMA': 'be'},
             {'IS_ALPHA': True, 'OP':'?'},
             {'IS_ALPHA': True, 'OP': '?'},
             {'LOWER': 'nice'},
             {'LOWER': 'if'}],

            # wouldn\'t it be ([\w]+[ \,]+){0,2}nice if
            [{'LOWER': 'would'},
             {'LOWER': 'it'},
             {'LOWER': 'not'},
             {'LEMMA': 'be'},
             {'IS_ALPHA': True, 'OP':'?'},
             {'IS_ALPHA': True, 'OP': '?'},
             {'LOWER': 'nice'},
             {'LOWER': 'if'}],

            # if ([\w]+[ \,]+){3,8} that would be ([\w]+[ \,]+){0,2}nice
            [{'LOWER': 'if'},
             {'IS_ALPHA': True, 'OP':'+'},
             {'LOWER': 'that'},
             {'LOWER': 'would'},
             {'LOWER': 'be'},
             {'IS_ALPHA': True, 'OP':'?'},
             {'IS_ALPHA': True, 'OP':'?'},
             {'LOWER': 'nice'}],

            # (cannot|will not|won\'t|can\'t) ([\w]+[ \,]+){1,7}(if|unless)
            [{'LOWER': {'IN':['can', 'will']}},
             {'LOWER': 'not'},
             {'IS_ALPHA': True, 'OP':'+'},
             {'LOWER': {'IN':['if', 'unless']}}],

            # (if|unless) ([\w]+[ \,]+){3,10}(cannot|will not|won\'t|can\'t)
            [{'LOWER': {'IN':['if', 'unless']}},
             {'IS_ALPHA': True, 'OP':'+'},
             {'LOWER': {'IN':['can', 'will']}},
             {'LOWER': 'not'}],

            # (need|needs|must|has to|have to) ([\w]+[ \,]+){3,10}(in order )to
            [{'LEMMA': {'IN':['need', 'must', 'have']}},
             {'LOWER': 'to', 'OP':'?'},
             {'IS_ALPHA': True, 'OP':'+'},
             {'LOWER': 'in'},
             {'LOWER': 'order'},
             {'LOWER': 'to'}],

            # (in order )?to ([\w]+[ \,]+){3,10}(need|needs|must|has to|have to)
            [{'LOWER': 'in'},
             {'LOWER': 'order'},
             {'LOWER': 'to'},
             {'IS_ALPHA': True, 'OP':'+'},
             {'LEMMA': {'IN':['need', 'must','have']}},
             {'LOWER': 'to'}],

            # as long as (we|you) ([\w]+[ \,]+){3,10}(will|can|able|should|[a-zA-Z]+\'ll)
            [{'LOWER': 'as'},
             {'LOWER': 'long'},
             {'LOWER': 'as'},
             {'DEP': 'poss'},
             {'IS_ALPHA': True, 'OP':'+'},
             {'LEMMA': {'IN':['will', 'can', 'able', 'should']}}],

            # ([a-zA-Z]\'ll|will|can|able|should) ([\w]+[ \,]+){3,10}as long as (we|you) 
            [{'LEMMA': {'IN':['will', 'can', 'able', 'should']}},
             {'IS_ALPHA': True, 'OP':'+'},
             {'LOWER': 'as'},
             {'LOWER': 'long'},
             {'LOWER': 'as'},
             {'DEP': 'poss'}],

            #(you|he|we) better ([\w]+[ \,]+){3,10}or
            [{'POS': 'PRON'},
             {'LOWER': 'better'},
             {'IS_ALPHA': True, 'OP':'+'},
             {'LOWER':'or'}],

            # otherwise
            [{'LOWER': 'otherwise'}]
        )
    
    def __call__(self, doc):
        matches = self.matcher(doc)
        
        for match_id, start, end in matches:
            sents = self.object.tokens.Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = self.object.tokens.Span(doc, sent_start, sent_end, label = "CONDITIONALS")
            doc._.opinion.append(opinion,)
        return doc
