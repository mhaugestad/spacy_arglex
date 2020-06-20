#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Wordclasses(object):
    object.tokens.Token.set_extension("is_EMO1V", getter = lambda token: token.lemma_ in ('like', 'adore', 'want', 'prefer', 'love', 'enjoy') and token.pos_ == 'VERB', force = True)
    
    object.tokens.Token.set_extension("is_EMO1N", getter = lambda token: token.lemma_ in ('like', 'adoration', 'want', 'preference', 'love', 'enjoyment') and token.pos_ == 'NOUN', force = True)

    object.tokens.Token.set_extension("is_EMO2V", getter = lambda token: token.lemma_ in ('hate', 'dislike', 'disprefer') and token.pos_ == 'VERB', force = True)
    
    object.tokens.Token.set_extension("is_EMO2N", getter = lambda token: token.lemma_ in ('hate', 'dislike', 'dispreference') and token.pos_ == 'VERB', force = True)