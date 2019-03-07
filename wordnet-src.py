# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:54:22 2019

@author: scatt
"""

from __future__ import unicode_literals
from nltk.corpus.reader.wordnet import NOUN
from nltk.corpus import wordnet
from nltk.compat import python_2_unicode_compatible

class WordNetLemmatizer(object):
    
    '''WordNet Lemmatizer

    Lemmatize using WordNet's built-in morphy function.
    Returns the input word unchanged if it cannot be found in WordNet.

        >>> from nltk.stem import WordNetLemmatizer
        >>> wnl = WordNetLemmatizer()
        >>> print(wnl.lemmatize('dogs'))
        dog
        >>> print(wnl.lemmatize('churches'))
        church
        >>> print(wnl.lemmatize('aardwolves'))
        aardwolf
        >>> print(wnl.lemmatize('abaci'))
        abacus
        >>> print(wnl.lemmatize('hardrock'))
        hardrock
    '''

    def __init__(self):
        pass

    def lemmatize(self, word, pos=NOUN):
        lemmas = wordnet._morphy(word, pos)
        return min(lemmas, key=len) if lemmas else word


    def __repr__(self):
        return '<WordNetLemmatizer>'



# unload wordnet
    def teardown_module(module=None):
        from nltk.corpus import wordnet

        wordnet._unload()