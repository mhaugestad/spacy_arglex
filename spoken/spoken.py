#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Spoken(object):
    object.tokens.Token.set_extension("is_spoken", getter = lambda token: token.text.lower() in ('uh','um', 'mm-hmm', 'uh-huh', 'huh'), force = True)
