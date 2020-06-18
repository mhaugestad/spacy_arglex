#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from assessment.assesment import Assessment
from authority.authority import Authority
from causation.causation import Causation
from conditionals.conditionals import Conditionals
from contrast.contrast import Contrast
from difficulty.difficulty import Difficulty
from doubt.doubt import Doubt
from emphasis.emphasis import Emphasis
from generalization.generalization import Generalization
from inconsistency.inconsistency import Inconsistency


def arglex(object):
    nlp = object.load('en_core_web_sm')
    
    # Set Document Extensions
    object.tokens.Doc.set_extension("opinion", default = [], force = True)

    # Set Span Extensions
    object.tokens.Span.set_extension("assessment", default = None, force = True)
    object.tokens.Span.set_extension("authority", default = None, force = True)
    object.tokens.Span.set_extension("causation", default = None, force = True)
    object.tokens.Span.set_extension("conditionals", default = None, force = True)


    # Set Token Extensions


    # Add to pipe
    nlp.add_pipe(Assessment(nlp), name = 'Assessment', last = True)
    nlp.add_pipe(Authority(nlp), name = 'Authority', last = True)
    nlp.add_pipe(Causation(nlp), name = 'Causation', last = True)
    nlp.add_pipe(Conditionals(nlp), name = 'Conditionals', last = True)
    nlp.add_pipe(Contrast(nlp), name = 'Contrast', last = True)
    nlp.add_pipe(Difficulty(nlp), name = 'Difficulty', last = True)
    
    return nlp
