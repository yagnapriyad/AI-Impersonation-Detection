#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Takes filtered user tweet files from 'preprocessed_data_path', generates
embeddings, and writes output processed_data_path.

Jan, 2020
@author: Yagna
"""

from get_config import (get_config, create_dir_if_not_there)
from tweetvalidator.data_processing import embed_tweets_from_directories

config = get_config()
create_dir_if_not_there(config['processed_data_path'])

embed_tweets_from_directories(config['preprocessed_data_path'], 
                              config['processed_data_path'])
                              
