#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Emphasis(object):
    
    def __init__(self, nlp, object):
        self.object = object
        self.matcher = object.matcher.Matcher(nlp.vocab)
        self.matcher.add("Emphasis", None,
                    
            #clearly
            [{'LOWER':'clearly'}],
                         
            #obviously
            [{'LOWER':'obviously'}],
            
            #patently
            [{'LOWER':'patently'}],
            
            #when you (really )?think about it
            [{'LOWER':'when'},
             {'LOWER': 'you'},
             {'LOWER': 'really', 'OP':'?'},
             {'LOWER': 'think'},
             {'LOWER': 'about'},
             {'LOWER': 'it'}],
            
            #(it is|it\'s) ((really|pretty) )?(obvious|evident|clear) (that)?
            [{'LOWER':'it'},
             {'LEMMA': 'be'},
             {'LOWER': {'IN':['really', 'pretty']}, 'OP':'?'},
             {'LOWER': {'IN':['obvious', 'evident', 'clear']}}],
            
            #definitely
             [{'LOWER':'definitely'}],
            
            #i have to say
            [{'POS':'PRON'},
             {'LEMMA': 'have'},
             {'LOWER': 'to'},
             {'LOWER': 'say'}],
                         
            #i\'ve got to say
            [{'POS':'PRON'},
             {'LEMMA': 'have'},
             {'LOWER': 'got'},
             {'LOWER': 'to'},
             {'LOWER': 'say'}],
                         
            #i\'ve gotta say
            [{'POS':'PRON'},
             {'LEMMA': 'have'},
             {'LOWER': 'gotta'},
             {'LOWER': 'say'}],
                         
            #i should say
            [{'POS':'PRON'},
             {'LOWER': 'should'},
             {'LOWER': 'say'}],
                         
            #surely
            [{'LOWER':'surely'}],
            
            #for sure
            [{'LOWER':'for'},
             {'LOWER': 'sure'}],       
                         
            #(@BE) ((sure)|(certain)|(confident)) (that)?
            [{'LEMMA':'be'},
             {'LOWER': 'sure'}],   
                         
            #of course
            [{'LOWER':'of'},
             {'LOWER': 'course'}],
                         
            #no doubt about it
            [{'LOWER':'no'},
             {'LOWER': 'doubt'},
             {'LOWER': 'about'},
             {'LOWER': 'it'}],
            
            #doubtless
            [{'LOWER':'doubtless'}],
                         
            #without a doubt
            [{'LOWER':'without'},
             {'LOWER': 'a'},
             {'LOWER': 'doubt'}],
                         
                         
            #I have no doubt (that)?
            [{'POS':'PRON'},
             {'LEMMA': 'have'},
             {'LOWER' : 'no'},
             {'LOWER': 'doubt'}],
            
            #I bet (that)?
            [{'POS':'PRON'},
             {'LEMMA': 'bet'}],
                         
            #(@BE) bound to
            [{'LEMMA':'be'},
             {'LOWER': 'bound'},
             {'LOWER': 'to'}],
                         
            #no two ways about it
            [{'LOWER':'no'},
             {'LOWER': 'two'},
             {'LOWER': 'ways'},
             {'LOWER': 'about'},
             {'LOWER': 'it'}],
                         
            #there ((is)|(are)) no two ways about it
            [{'LOWER':'there'},
             {'LEMMA': 'be'},
             {'LOWER':'no'},
             {'LOWER': 'two'},
             {'LOWER': 'ways'},
             {'LOWER': 'about'},
             {'LOWER': 'it'}], 
                         
            #((the)|(one)) ((thing)|(issue)|(question)|(problem)) (@MODAL )?(@BE) (that)?
            [{'LOWER':{'IN':['one', 'the']}},
             {'LOWER': {'IN': ['thing', 'issue', 'question', 'problem']}},
             {'LEMMA': {'IN': ['will', 'shall', 'can', 'could', 'would', 'may', 'might', 'be', 'must', 'dare']}, 'OP':'?'},
             {'LEMMA': 'be'}], 
                         
            #my feeling is (that)?
            [{'DEP': 'poss'},
             {'LOWER': 'feeling'},
             {'LEMMA': 'be'}], 
                         
            #that\'s why
            [{'LOWER':'that'},
             {'LOWER': 'is'},
             {'LOWER': 'why'}],
                         
            #that is why
                         
            #the idea (here )?is (that)?
            [{'LOWER':'the'},
             {'LOWER': 'idea'},
             {'LOWER': 'here'},
             {'LEMMA': 'be'}],
                         
            #((my)|(the)) whole ((point)|(question)) is 
            [#{'IN':[{'DEP':'poss'}, {'LOWER': 'the'}]},
             {'LOWER': 'whole'},
             {'LOWER': {'IN':['point', 'question']}},
             {'LEMMA': 'be'}],    
            
            #what you have to do is 
            [{'LOWER':'what'},
             {'POS': 'PRON'},
             {'LEMMA': 'have'},
             {'LOWER': 'to'},
             {'LOWER': 'do'},
             {'LEMMA': 'be'}],
                         
            #the reason is (that)?  
            [{'LOWER':'the'},
             {'LOWER': 'reason'},
             {'LEMMA': 'be'}],
                         
            #here\'s what
            [{'LOWER':'here'},
             {'LOWER': 'is'},
             {'LEMMA': 'what'}],
                         
            #here is what
                         
            #exactly
            [{'LOWER':'exactly'}],
                         
            #precisely
            [{'LOWER':'precisely'}],
                         
            #(@GONNA)
                         
            #(@GONNANEG)
                         
            #(@GONNANEGCL)
                         
            #(@GONNACL)
                         
            #what will happen is
            [{'LOWER':'what'},
             {'LOWER': 'will'},
             {'LOWER': 'happen'},
             {'LOWER': 'is'}],
                         
            #what\'ll happen is
                         
            #what\'s ((gonna)|(going to)) happen is
            [{'LOWER':'what'},
             {'LOWER': 'is'},
             {'LOWER': {'IN':['gonna', 'going']}},
             {'LOWER': 'to', 'OP': '?'},
             {'LOWER': 'happen'},
             {'LOWER': 'is'}],
                                         
            #what is ((gonna)|(going to)) happen is
                         
            #i want to (highlight|emphasize|underscore)
            [{'POS':'PRON'},
             {'LEMMA': 'want'},
             {'LOWER': 'to'},
             {'LOWER': {'IN':['highlight', 'emphasize', 'underscore']}}]
        )
    
    def __call__(self, doc):
        matches = self.matcher(doc)
        
        for match_id, start, end in matches:
            sents = self.object.tokens.Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = self.object.tokens.Span(doc, sent_start, sent_end, label = "EMPHASIS")
            doc._.opinion.append(opinion,)
        return doc
