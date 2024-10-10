import requests
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import streamlit as st
import re
from io import BytesIO
from transformers import BertTokenizer
from transformers import BertTokenizer, BertForTokenClassification, pipeline
from transformers import BertModel
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertModel
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
API_ENDPOINT = 'https://sheetdb.io/api/v1/24opc9hx6djz6'
strings = ''

def room_creation():
    response = requests.post(API_ENDPOINT)
    return response

def model():
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/1Ojzc65O7XcVWXPAAKcskGuB5a9oMhM8my10JbHWGHCQ/gviz/tq?tqx=out:csv&sheet=Sheet1')
    sentences = df['about']
    model = SentenceTransformer('all-mpnet-base-v2')
    sentence_embeddings = model.encode(sentences)
    similarity_scores = model.similarity(sentence_embeddings, sentence_embeddings)
    person = df['name']
    d = dict(zip(person, similarity_scores))
    df = pd.DataFrame(d, index = person)
    arr = []
    for i in range(len((sentences))):
        t = df.sort_values(person[i],ascending=False)
        arr.append([t.index[0],t.index[1] + ': ' + str(t[person[i]][1]*100),t.index[2] + ': ' + str(t[person[i]][2]*100),t.index[3] + ': ' + str(100*t[person[i]][3])])
    df_from_array = pd.DataFrame(arr)
    return df_from_array,person


def func(linkedin_profile_url):
    if(linkedin_profile_url == ''):
        return []
    elif(linkedin_profile_url != ''):
        ipt_final = 'Working!'
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        linkedin_profile_url = linkedin_profile_url
        api_key = 'mSLO0XONI_EP0KQ-hJtDvw'
        headers = {'Authorization': 'Bearer ' + api_key}
        response = requests.get(api_endpoint, params={'url': linkedin_profile_url, 'skills': 'include'}, headers=headers)
        profile_data = response.json()
        if(len(profile_data) <= 3):
            return []
        else:
            experiences = len(profile_data['experiences'])
            final_experiences = ''
            for i in range(experiences):
                final_experiences += f"{profile_data['experiences'][i]['company']} {profile_data['experiences'][i]['title']}  {profile_data['experiences'][i]['description']}\n"
            with open("data.json", "w") as outfile:
                json.dump(profile_data, outfile)
            summary = profile_data['summary']
            
            API_ENDPOINT = 'https://sheetdb.io/api/v1/24opc9hx6djz6'

            # Step 1: Ensure the necessary NLTK resources are available
            nltk.download('punkt')  # Tokenizer models
            nltk.download('punkt_tab')
            nltk.download('stopwords')  # Stopwords for filtering
            nltk.download('averaged_perceptron_tagger')
            nltk.download('averaged_perceptron_tagger_eng')  # POS tagger

            profile_text = final_experiences
            strings = profile_text
            # Step 3: Tokenization (splitting the text into words)
            try:
                tokens = word_tokenize(profile_text)
            except Exception as e:
                print(f"Error during tokenization: {e}")

            # Step 4: Remove stopwords (common unimportant words)
            try:
                stop_words = set(stopwords.words('english'))
                filtered_tokens = [word for word in tokens if word.lower() not in stop_words and word.isalpha()]
            except Exception as e:
                print(f"Error during stopwords filtering: {e}")

            # Step 5: POS tagging to identify the part of speech of each word
            try:
                pos_tags = pos_tag(filtered_tokens)
            except Exception as e:
                print(f"Error during POS tagging: {e}")

            # Step 6: Extracting important words (nouns and adjectives)
            try:
                important_words = [word for word, pos in pos_tags if pos.startswith('N') or pos.startswith('J')]
            except Exception as e:
                print(f"Error during extraction of important words: {e}")

            data = {
                "data": {
                    'name': profile_data['full_name'],
                    'linkedin url': linkedin_profile_url,
                    'keywords': important_words,
                    'about': summary,
                }
            }

            response = requests.post(API_ENDPOINT, json=data)

            return important_words