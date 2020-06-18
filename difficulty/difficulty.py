#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Difficulty(object):
    
    def __init__(self, object):
        
        self.matcher = Matcher(object.vocab)
        self.matcher.add("Difficulty", None,
            
        #(@BE) (@INTENSADV1)?easy
        [{'LEMMA':'be'},
         {'_': {'is_intense':True}},
         {'LOWER': 'easy'}]

        #(@BE) a (@INTENSADJ1)?breeze
        [{'LEMMA':'be'},
         {'LOWER': 'a'},
         {'_': {'is_intense':True}, 'OP': '?'},
         {'LOWER': 'breeze'}]

        #(@BE) a (@INTENSADJ1)?walk in the park
        [{'LEMMA':'be'},
         {'LOWER': 'a'},
         {'_': {'is_intense':True}, 'OP': '?'},
         {'LOWER': 'walk'},
         {'LOWER' : 'in'},
         {'LOWER': 'the'},
         {'LOWER' : 'park'}]

        #(@BE) a (@INTENSADJ1)?piece of cake
        [{'LEMMA':'be'},
         {'LOWER': 'a'},
         {'_': {'is_intense':True}, 'OP': '?'},
         {'LOWER': 'piece'},
         {'LOWER' : 'of'},
         {'LOWER': 'cake'}]

        #(@BE) a (@INTENSADJ1)?snap
        [{'LEMMA':'be'},
         {'LOWER': 'a'},
         {'_': {'is_intense':True}, 'OP': '?'},
         {'LOWER': 'snap'}]
                         
        #(@BE) a (@INTENSADJ1)?cinch
        [{'LEMMA':'be'},
         {'LOWER': 'a'},
         {'_': {'is_intense':True}, 'OP': '?'},
         {'LOWER': 'cinch'}]

        #(@BE) (@INTENSADJ1)?child's play
        [{'LEMMA':'be'},
         {'_': {'is_intense':True}, 'OP': '?'},
         {'LEMMA': 'child'},
         {'LOWER' : 'play'}]

        #(@BE) (@INTENSADV1)?difficult
        [{'LEMMA':'be'},
         {'_': {'is_intense':True}, 'OP': '?'},
         {'LOWER': 'difficult'}]

        #(@BE) a (@INTENSADJ1)?pain
        [{'LEMMA':'be'},
         {'LOWER': 'a'},
         {'_': {'is_intense':True}, 'OP': '?'},
         {'LOWER': 'pain'}]

        #(@BE) a (@INTENSADJ1)?pain in the (butt|neck|ass)
        [{'LEMMA':'be'},
         {'LOWER': 'a'},
         {'_': {'is_intense':True}, 'OP': '?'},
         {'LOWER': 'pain'},
         {'LOWER': 'in'},
         {'LOWER' : 'the'},
         {'LOWER': {'IN':['butt', 'neck', 'ass']}}]

        #(@BE) a (@INTENSADJ1)?(bitch|bastard) to
        [{'LEMMA':'be'},
         {'LOWER': 'a'},
         {'_': {'is_intense':True}, 'OP': '?'},
         {'LOWER': {'IN':['bitch', 'bastard']},
         {'LOWER' : 'to'}]
                        
        #(@BE) no picnic
        [{'LEMMA':'be'},
         {'LOWER': 'no'},
         {'LOWER' : 'picnic'}]

        #(@BE) (@INTENSADV1)?tricky
         [{'LEMMA':'be'},
         {'_': {'is_intense':True}, 'OP': '?'},
         {'LOWER' : 'tricky'}]

        #(@BE) (@INTENSADV1)?arduous
         [{'LEMMA':'be'},
         {'_': {'is_intense':True}, 'OP': '?'},
         {'LOWER' : 'arduous'}]
         
        #(@BE) a (@INTENSADJ1)?challenge
         [{'LEMMA':'be'},
         {'_': {'is_intense':True}, 'OP': '?'},
         {'LOWER' : 'challenge'}]

        #(@BE) (@INTENSADV1)?challenging
        [{'LEMMA':'be'},
         {'_': {'is_intense':True}, 'OP': '?'},
         {'LOWER' : 'challenging'}]

        #(@HAVE) a (@INTENSADV1)?(hard|difficult) time
         [{'LEMMA':'have'},
          {'LOWER': 'a'},
          {'_': {'is_intense':True}, 'OP': '?'},
          {'LOWER' : {'IN':['hard', 'dificult']},
          {'LOWER' : 'time'}]
          
        )
    
    def __call__(self, doc):
        matches = self.matcher(doc)
        
        for match_id, start, end in matches:
            sents = Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = Span(doc, sent_start, sent_end, label = "DIFFICULTY")
            doc._.opinion.append(opinion,)
        return doc
