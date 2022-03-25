import sys
#sys.path.insert(1, 'C:/Users/ALP/ironhack_2022/Unit_06/Day_02/lab_apis/config.py')
from config import *
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import requests
import math
import pickle
##sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= client_id,
#                                                           client_secret= client_secret_id))

def song_recommender(z = 'Yes'):

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= client_id, client_secret= client_secret_id))
    while z == 'Yes': 


        '''
        *Important: you will have to import the login credentials and initialize SpotiPy with user credentials seperately 
        Assuming that we have all the libraries imported, this function prompts the user for the song name, 
        after which it provide a list of 10 possible songs. Then the user has to pick the number of the song that they
        want. And based on this it will return the features of that song.
        '''
        #A. Input asking for song name
        print('Enter song name:')
        x = input() 

        results = sp.search(q=x,limit=10)
        i=0
        print("")
        print("Please enter the correct track number from these choices:")
        print(" ")

        for item in results['tracks']['items']:#for loop that displays song name, the artist and url 
            print(i,".'{}' by '{}' and the url is: {}".format(item['name'],item['artists'][0]['name'], item['external_urls']['spotify']))
            i+=1
        print(" ")    
        print('Enter song number:')
        print(" ") 
        a = input()#input which asks for the number of the song(ordered number)
        a= int(a)

        #B. Getting song_features of that song
        my_dict = sp.audio_features(results["tracks"]["items"][a]["uri"])[0]#based on chosen integer audio features extracted
        my_dict_new = { key: [my_dict[key]] for key in list(my_dict.keys()) }
        song_features = pd.DataFrame(my_dict_new)#This makes a dataframe with songfeatures of chosen song

        #C. Now time to do the clustering
        #First drop unnecssary columns
        song_features_new = song_features.drop(['type','id', 'uri', 'track_href', 'analysis_url','time_signature'], axis = 1)
        #Second load your scaler and model
        def load(filename = "filename.pickle"): 
            try: 
                with open(filename, "rb") as file: 
                    return pickle.load(file) 
            except FileNotFoundError: 
                print("File not found!")
        scaler2 = load("_scalers/standard_scaler.pickle")
        cluster_model= load("_models/kmeans_15.pickle")
        #Third scale features
        song_features_sc = scaler2.transform(song_features_new)
        song_features_sc_df = pd.DataFrame(song_features_sc, columns = song_features_new.columns)

        #fourth perform cluster prediction on scale features
        cluster = cluster_model.predict(song_features_sc_df)
        cluster_df = pd.DataFrame(cluster, columns=['cluster'])#Here we have a df with the cluster
        #fifth concatenate cluster details onto the songfeatures
        cluster_df = pd.concat([song_features, cluster_df], axis = 1)# Here the cluster is added to the original df, which has the artist name and song name

        #D. Check if song is in Hot100 or not
        featsfinal = pd.read_csv('_datasets/feats_final_withclusters.csv')#IMPORTANT: You need featsfinal.csv in order to know hot100 ids
        hot100_ids_list =[]#empty list for hot100 song ids
        for x in featsfinal['id'][featsfinal['Hot']==True]:#Here we append to empty list of hot100 songs ids
            hot100_ids_list.append(x)
        i = cluster_df['cluster'][0]#here we assign he cluster of user song to variable
        if cluster_df['id'][0] in hot100_ids_list:
            recommendations = featsfinal[(featsfinal['Hot']== True) & (featsfinal['cluster'] == i)].head(10)#returns recommandation df
        else: #if NOT hot100
            recommendations = featsfinal[(featsfinal['Hot']== False) & (featsfinal['cluster'] == i)].head(10)

        print(" ") 
        print("Here are your recommended tracks:")
        print(" ")
        for x in recommendations['uri']:
            track = x
            track = sp.track(track)
            print("'{}' by '{}' and the url is: {}".format(track['name'],track['artists'][0]['name'], track['external_urls']['spotify']))
        print(" ")
        print("Do you want another recommendation? Yes or No")
        z = input()
