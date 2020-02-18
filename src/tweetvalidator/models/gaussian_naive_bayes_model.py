#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Provides GaussianNBModel which can be trained on tweet embeddings.

Jan, 2020
@author: Yagna
"""

import numpy as np
from sklearn.model_selection import cross_val_score
from .base_model import Model
from sklearn.naive_bayes import GaussianNB

class GaussianNBModel(Model):
    """ Trains a gaussian naive bayes model to the embedded tweets provided.
    """
    def __init__(self, verbose=False):       
        self.verbose = verbose
        self.characterization_complete = False
     
    def characterize(self, corpus, context_corpus):
        
        # Because dataframe holds nested arrays awkwardly
        corpus = np.asarray([x for x in corpus])

        # Let's get the same number of negatives as positive examples
        context_corpus = np.asarray([x for x in context_corpus])
        np.random.shuffle(context_corpus)
        context_corpus = context_corpus[:len(corpus)]


        X = np.concatenate([corpus, context_corpus])
        Y = np.concatenate([np.ones(len(corpus)),
                            np.zeros(len(context_corpus))])

        self.clf = GaussianNB()
        self.clf.fit(X, Y)

        self.characterization_complete = True
           
    def infer(self, embedded_tweets=None):
        """ Makes a prediction based on the trained model.  Expects tweets to
            arrive embedded.
        """
        
        predictions =  self.clf.predict(np.asarray(
                                                [x for x in embedded_tweets]))       
        
        return predictions
        
