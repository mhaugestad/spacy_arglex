#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Assessment(object):
    
    def __init__(self, nlp, object):
        
        self.object = object
        self.matcher = object.matcher.Matcher(nlp.vocab)
        self.matcher.add("Assessment", None,
            
            # (our|my) (opinion|understanding) (is|was) that
            [{'DEP':'poss'},
            {"LOWER": {'IN':['understanding', 'opinion']}}, 
            {'LEMMA': 'be'},
            {'LOWER': 'that'}],

            # it (is|was) (our|my) (opinion|understanding) (that)?                     
            [{'LOWER':'it'},
            {'LEMMA': 'be'},
            {'DEP': 'poss'},
            {'LOWER' :{'IN':['opinion', 'understanding']}}],

            #in (our|my) opinion
            [{'LOWER': 'in'},
             {'DEP': 'poss'},
             {'LEMMA': 'opinion'}],

            #(our|my) take on
            [{'DEP': 'poss'},
             {'LOWER': 'take'},
             {'LOWER': 'on'}],

            #it (seems|seemed) to (us|me) (that)?
            [{'LOWER': 'it'},
             {'LEMMA': 'seem'},
             {'LOWER': 'to'},
             {'POS': 'PRON'}],

            #it (seems|seemed) (that)?
            [{'LOWER': 'it'},
             {'LEMMA': 'seem'}],

            #it would seem to (us|me)?
            [{'LOWER': 'it'},
             {'LOWER': 'would'},
             {'LOWER': 'seem'},
             {'LOWER': 'to'}],

            #it would appear to (us|me)?
            [{'LOWER': 'it'},
             {'LOWER': 'would'},
             {'LOWER': 'appear'},
             {'LOWER': 'to'}],

            #it appear to (us|me)?
            [{'LOWER': 'it'},
             {'LEMMA': 'appear'},
             {'LOWER': 'to'}],

            #(the|my|our) ([\w]+[ ])?point is (that)?
            [{'DEP': {'IN':['poss', 'det']}},
             {'IS_ALPHA': True, 'OP':'?'},
             {'LOWER': 'point'},
             {'LEMMA': 'be'}],

            #it (looks|looked) to (us|me) (as if|like)
            [{'LOWER': 'it'},
             {'LEMMA': 'look'},
             {'LOWER': 'to'},
             {'POS':'PRON'},
             {'LOWER': 'like'}],

            #it (looks|looked) (as if|like|that way)
            [{'LOWER': 'it'},
             {'LEMMA': 'look'},
             {'LOWER': 'as'},
             {'LOWER':'if'}],
            
            [{'LOWER': 'it'},
             {'LEMMA': 'look'},
             {'LOWER': 'like'}],
            
            [{'LOWER': 'it'},
             {'LEMMA': 'look'},
             {'LOWER': 'that'},
             {'LOWER': 'way'}],

            #(we|i) (have|get|got) the impression (that)?
            [{'POS': 'PRON'},
             {'LEMMA': {'IN':['have', 'get']}},
             {'LOWER': 'the'},
             {'LOWER':'impression'}],

            #(our|my) impression (was|is) (that)?
            [{'DEP': 'poss'},
             {'LOWER':'impression'},
             {'LEMMA': 'be'}],

            #in (our|my) book
            [{'LOWER': 'in'},
             {'DEP':'poss'},
             {'LEMMA': 'book'}],

            #to (our|my) mind
            [{'LOWER': 'to'},
             {'DEP':'poss'},
             {'LEMMA': 'mind'}],
                         
            #to (our|my) way of thinking
            [{'LOWER': 'to'},
             {'DEP':'poss'},
             {'LOWER': 'way'},
             {'LOWER': 'of'},
             {'LOWER': 'thinking'}],
                         
            #as far as (I am|I was|we are|we were) concerned
            [{'LOWER': 'as'},
             {'LOWER': 'far'},
             {'LOWER': 'as'},
             {'POS': 'PRON'},
             {'LEMMA': 'be'},
             {'LOWER': 'concerned'}],

            #if you ask (me|us)
            [{'LOWER': 'if'},
             {'LOWER': 'you'},
             {'LOWER': 'ask'},
             {'POS': 'PRON'}],
                         
            #(our|my) feeling (is|was|would be)
            [{'DEP': 'poss'},
             {'LOWER': 'feeling'},
             {'LEMMA': {'IN':['be', 'would']}}],
                        
            #from where (I\'m|I am) (standing|sitting)
            [{'LOWER': 'from'},
             {'LOWER': 'where'},
             {'POS': 'PRON'},
             {'LEMMA': 'be'},
             {'LOWER': {'IN':['standing', 'sitting']}}],
                         
            #(we|I) (don\'t)? think (that)?
            [{'POS': 'PRON'},
             {'LEMMA': 'do'},
             {'LOWER': 'not'},
             {'LEMMA': 'think'},
             {'LOWER': 'that'}],
                         
            #all (we\'re|I\'m) saying is
            [{'LOWER': 'all'},
             {'POS': 'PRON'},
             {'LEMMA': 'be'},
             {'LEMMA': 'say'},
             {'LEMMA': 'be'}],
                         
            #what (I\'m|we\'re) saying is
            [{'LOWER': 'what'},
             {'POS': 'PRON'},
             {'LEMMA': 'be'},
             {'LEMMA': 'say'},
             {'LEMMA': 'be'}],

            #(we\'re|I\'m) (not)? saying that
            [{'POS': 'PRON'},
             {'LEMMA': 'be'},
             {'LOWER': 'not', 'OP':'?'},
             {'LEMMA': 'say'},
             {'LOWER': 'that'}],
            
            #what (we\'re|i\'m) trying to say is
            [{'LOWER': 'what'},
             {'POS': 'PRON'},
             {'LEMMA': 'be'},
             {'LEMMA': 'try'},
             {'LOWER': 'to'},
             {'LEMMA': 'say'}],
            
            #what (we|i) mean is (that)?
            [{'LOWER': 'what'},
             {'POS': 'PRON'},
             {'LOWER': 'mean'},
             {'LEMMA': 'be'}],            
        )
    
    def __call__(self, doc):
        matches = self.matcher(doc)
        
        for match_id, start, end in matches:
            sents = self.object.tokens.Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = self.object.tokens.Span(doc, sent_start, sent_end, label = "ASSESSMENT")
            doc._.opinion.append(opinion,)
        return doc
