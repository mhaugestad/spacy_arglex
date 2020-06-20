#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Structure(object):

    def __init__(self, nlp, object):
        self.matcher = object.matcher.PhraseMatcher(nlp.vocab, attr="LOWER")
        terms = ['first', 'secondly', 'first place', 'in the first place', 'first of all']
        patterns = [nlp.make_doc(text) for text in terms]
        self.matcher.add("Structure", None, *patterns)

    def __call__(self, doc):
        matches = self.matcher(doc)
        for match_id, start, end in matches:
            sents = Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = Span(doc, sent_start, sent_end, label = "STRUCTURE")
            doc._.opinion.append(opinion,)
        return doc
