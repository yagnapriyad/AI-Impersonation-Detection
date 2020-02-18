#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates accuracy, precision, recall and confusion matrix for each model.

Jan, 2020
@author: Yagna
"""

from get_config import (get_config, create_dir_if_not_there)
config = get_config()
create_dir_if_not_there(config['eval_output_path'])

from tweetvalidator.models import random_forest_model
from tweetvalidator.models.random_forest_model import RandomForestModel
from tweetvalidator.models.xgboost_model import XgBoostModel
from tweetvalidator.models.gaussian_naive_bayes_model import GaussianNBModel
from tweetvalidator import train_models

dir_args = {   'input_directory'  : config['processed_data_path'],
       'negative_input_directory' : config['processed_negative_data_path'],
               'output_directory' : config['eval_output_path']}

train_models(RandomForestModel(verbose=True),
            'embedding', **dir_args,
            file_prefix = 'random_forest_model')

train_models(XgBoostModel(verbose=True),
            'embedding', **dir_args,
            file_prefix = 'xgboost_model')

train_models(GaussianNBModel(verbose=True),
            'embedding', **dir_args,
            file_prefix = 'gaussian_naive_bayes_model')
