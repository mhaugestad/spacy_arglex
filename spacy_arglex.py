#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from assessment.assessment import Assessment
from authority.authority import Authority
from causation.causation import Causation
from conditionals.conditionals import Conditionals
from contrast.contrast import Contrast
from difficulty.difficulty import Difficulty
from doubt.doubt import Doubt
from emphasis.emphasis import Emphasis
from generalization.generalization import Generalization
from inconsistency.inconsistency import Inconsistency
from intensifiers.intensifiers import Intensifiers
from inyourshoes.inyourshoes import Inyourshoes
from necessity.necessity import Necessity
from possibility.possibility import Possibility
from priority.priority import Priority
from rhetoricalquestion.rhetoricalquestion import RhetoricalQuestion
from spoken.spoken import Spoken
from structure.structure import Structure
from wants.wants import Wants
from wordclasses.wordclasses import Wordclasses

def arglex(object):
    nlp = object.load('en_core_web_sm')
    
    # Set Document Extensions
    object.tokens.Doc.set_extension("opinion", default = [], force = True)

    # Set Span Extensions
    object.tokens.Span.set_extension("assessment", default = None, force = True)
    object.tokens.Span.set_extension("authority", default = None, force = True)
    object.tokens.Span.set_extension("causation", default = None, force = True)
    object.tokens.Span.set_extension("conditionals", default = None, force = True)
    object.tokens.Span.set_extension("contrast", default = None, force = True)
    object.tokens.Span.set_extension("difficulty", default = None, force = True)
    object.tokens.Span.set_extension("doubt", default = None, force = True)
    object.tokens.Span.set_extension("emphasis", default = None, force = True)
    object.tokens.Span.set_extension("generalization", default = None, force = True)
    object.tokens.Span.set_extension("inconsistency", default = None, force = True)
    object.tokens.Span.set_extension("inyourshoes", default = None, force = True)
    object.tokens.Span.set_extension("necessity", default = None, force = True)
    object.tokens.Span.set_extension("possibility", default = None, force = True)
    object.tokens.Span.set_extension("priority", default = None, force = True)
    object.tokens.Span.set_extension("rhetoricalquestion", default = None, force = True)
    object.tokens.Span.set_extension("structure", default = None, force = True)
    object.tokens.Span.set_extension("wants", default = None, force = True)

    # Set Token Extensions
    Spoken(object)
    Wordclasses(object)
    Intensifiers(object)
    
    # Add to pipeline 
    nlp.add_pipe(Assessment(nlp, object), name = 'Assessment', last = True)
    nlp.add_pipe(Authority(nlp, object), name = 'Authority', last = True)
    nlp.add_pipe(Causation(nlp, object), name = 'Causation', last = True)
    nlp.add_pipe(Conditionals(nlp, object), name = 'Conditionals', last = True)
    nlp.add_pipe(Contrast(nlp, object), name = 'Contrast', last = True)
    nlp.add_pipe(Difficulty(nlp, object), name = 'Difficulty', last = True)
    nlp.add_pipe(Doubt(nlp, object), name = 'Doubt', last = True)
    nlp.add_pipe(Emphasis(nlp, object), name = 'Emphasis', last = True)
    nlp.add_pipe(Generalization(nlp, object), name = 'Generalization', last = True)
    nlp.add_pipe(Inconsistency(nlp, object), name = 'Inconsistency', last = True)
    nlp.add_pipe(Inyourshoes(nlp, object), name = 'Inyourshoes', last = True)
    nlp.add_pipe(Necessity(nlp, object), name = 'Necessity', last = True)
    nlp.add_pipe(Possibility(nlp, object), name = 'Possibility', last = True)
    nlp.add_pipe(Priority(nlp, object), name = 'Priority', last = True)
    nlp.add_pipe(RhetoricalQuestion(nlp, object), name = 'RhetoricalQuestion', last = True)
    nlp.add_pipe(Structure(nlp, object), name = 'Structure', last = True)
    nlp.add_pipe(Wants(nlp, object), name = 'Wants', last = True)
    return nlp

def load(file):
    with open(file + '.txt', 'rb') as f:
        return f.read().split('\n')