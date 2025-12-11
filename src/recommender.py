import pandas as pd
import numpy as np
import ast #used for safely evaluating string representations of Python literals (lists, dicts)

DATA_PATH = '../data/'
N_RECOMMENDATIONS = 10

def load_and_merge_data(movies+file, credits_file):
    """loads and merges the movies and credits datasets"""
    try:
        movies = pd.read_csv(DATA_PATH + movies_file)
        credits = pd.read_csv(DATA_PATH + credits_file)

    except FileNotFoundError as e:
        print(f"Error loading data: {e}. Ensure data files are in the '{DATA_PATH}' directory.")
        return None

    #merge the two DataFrames on 'id' and 'movie_id'

    #rename movie_id to id for merge
    credits.columns = ['id', 'title', 'cast', 'crew']
    df = movies.merge(credits, on='id)

    #keep only relevant columns
    df = df[['id', 'title', 'genres', 'keywords', 'cast', 'crew', 'overview']]
    return df

#Helper function to safely extract the 'name' value from nested JSON-like strings
def extract_names(obj):
    """Converts a string of JSON list/dict to a list of names"""

    L = []
    #safely convert string representation of a list/dict to an actual list dict
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L


