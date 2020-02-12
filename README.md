# AI-Impersonation-Detection
The  goal  of  this  research  is  to  check if an account has been compromised on Twitter by validating their tweets using Natural Language Processing techniques.

Social engineering is an major threat that everyone is facing whether is hacking an account or identity theft. Fraudulent posts on social media are embarrassing to individuals and expensive to brands. Some accounts are hacked on purpose by an acquaintance  of  the  owner  with  the  goal  of  damaging  the reputation of the legitimate owner. Even though there is no money involeved it damages the credibility and releability of the user. This repository demonstrates use of natural language processing techniques with embedding via Universal Sentence Encoder, to classify new Twitter posts as in or out-of-character for a particular user. This can be applied in a simple binary discriminator to screen incoming content.

#### Presentation Slides

Further details regarding the motivation, methods and results of implementing this idea can be found in my presentation [here](https://tinyurl.com/v97rrbu) .

#### Setup
          
- Clone this repo with command git clone https://github.com/yagnapriyad/AI-Impersonation-Detection.git .

- Run the following to create a new conda/python environment


- conda create --name <environment_name> python=3.6.8


- conda activate <environment_name>


- conda install pip


- cd <project_path>/build


- pip install -r requirements.txt


If you're going to be using the Twitter API, edit <project_path>/build/insightTwitterCreds.bat and add your credentials. 

- Run:

  - source twitter_creds.txt


#### Running the project

1. Tweetvalidator

    - tweetvalidator.data_processing contains tools for downloading, filtering, and embedding Twitter data.
    - tweetvalidator.models contains the embedding-based models, which can be used for mean embedding and a variety of multi-   cluster variations, as well as a term-frequency model as a statistical baseline. Each of these models has a characterize method in which it's initialized and a similarity_score method for comparing a new tweet against the model's characterization.

2. Scripts

    - These starting place to running project and provide examples for how to use the functionality in tweetvalidator.

3. Configuration
  
    - Scripts get their configuration details from <project_path>/configs/config.json. 
  
##### Run these scripts (e.g. >python filter_raw_data.py) in this order to reproduce the project workflow.

    - retrieve_users_from_twitter.py downloads max_tweets_per_user tweets for the list of users in twitter_users. It writes to raw_data_path.
    - filter_raw_data.py reads tweets from raw_data_path, removes strings matching the regular expressions in regexp_tweet_filters, and writes tweets with at least min_tweet_characters to preprocessed_data_path.
    - embed_preprocessed_data.py reads tweets from preprocessed_data_path, generates an embedding using Universal Sentence Encoder, and writes the tweets with associated embeddings to processed_data_path.
    - train_user_specific_models reads data from processed_Data_path; splits it into training and test data and performs classification model, accuracy metrics are generated to eval_output_path.
    - generate_similarity_scores.py reads data from processed_data_path; splits it into user-characterization and test sets; initializes a variety of models, both embedding-based and term-frequency-based; and uses those models to generate cosine similarity scores for the test data. These results are written to eval_output_path.
    - analyze_similarity_scores.py reads similarity scores from eval_output_path and generates ROC/AUC graphs and data tables providing "sensitivity at false-positive-rate x" statements. Results are written to analysis_output_path.
    
#### Unit Testing

  - cd <project_path>/tests
  - pytest








