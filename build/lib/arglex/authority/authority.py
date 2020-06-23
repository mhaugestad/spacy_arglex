#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Authority(object):

    def __init__(self, nlp, object):
        self.matcher = object.matcher.PhraseMatcher(nlp.vocab, attr="LOWER")
        self.object = object
        terms = ["according to"]
        patterns = [nlp.make_doc(text) for text in terms]
        self.matcher.add("Authority", None, *patterns)

    def __call__(self, doc):
        matches = self.matcher(doc)
        for match_id, start, end in matches:
            sents = self.object.tokens.Span(doc, start, end).sent
            sent_start, sent_end = sents.start, sents.end
            opinion = self.object.tokens.Span(doc, sent_start, sent_end, label = "AUTHORITY")
            doc._.opinion.append(opinion,)
        return doc
