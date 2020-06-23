#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Intensifiers(object):
    object.tokens.Token.set_extension("is_INTENSADV1", getter = lambda token: token.text.lower() in ('absolutely', 'absurdly', 'resoundingly', 'amazingly', 'awfully', 'extremely', 'completely', 'highly', 'incredibly', 'perfectly', 'quite', 'really', 'strikingly', 'surprisingly', 'terribly', 'totally', 'unbelievably', 'hugely', 'unnaturally', 'unusually', 'utterly', 'very', 'tremendously', 'spectacularly') and token.pos_ == 'ADV', force = True)
    
    object.tokens.Token.set_extension("is_INTENSADJ1", getter = lambda token: token.text.lower() in ('absolute', 'extreme', 'incredible', 'perfect', 'phenomenal', 'spectacular', 'huge', 'major', 'tremendous', 'complete', 'considerable', 'real', 'terrible', 'total', 'unbelievable', 'utter', 'great', 'resounding') and token.pos_ == 'ADJ', force = True)

   