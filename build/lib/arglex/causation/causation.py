#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Causation(object):

    def __init__(self, nlp, object):
        self.object = object
        self.matcher = object.matcher.PhraseMatcher(nlp.vocab, attr="LOWER")
        terms = ['so', 'therefore', 'because', 'hence', 'as a result',
                 'consequently']
        patterns = [nlp.make_doc(text) for text in terms]
        self.matcher.add("Causation", None, *patterns)

    def __call__(self, doc):
        matches = self.matcher(doc)
        for match_id, start, end in matches:
            sents = self.object.tokens.Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = self.object.tokens.Span(doc, sent_start, sent_end, label = "CAUSATION")
            doc._.opinion.append(opinion,)
        return doc
