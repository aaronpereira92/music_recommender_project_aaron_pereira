# music_recommender_project_aaron_pereira
This is my submission for the GNOD project from Ironhack. 

**Attention**: to make the final function work you need to have a config file containing all your SpotifyAP credentials

**Information about REPO:**

The folders present in his repo are:
_datasets : This folder contains all the datasets that I used from the beginning. 
hot100.csv contains the billboard hot 100 songs,
not_hot.csv contains around 5000 not hot songs, 
featsfinal.csv contains spotify features of both nothot and hot100 songs combined, 
feats_final_withclusters.csv contains features and the clusters (This one is needed for the final function, but functioon knows filepath).

_functions: contains one file functions.py, which contains the song_recommender function. So do 'import song_recommender from functions'

_jupyternotebooks: Contains the following notebooks (here is the correct order of operation):
lab_webscraping_single_page_aaron_pereira.ipynb - webscrapping for music data from billboardhot 100.
lab_not_hot_songs_aaron_pereira.ipynb- webscraping from other sites
lab_spotify_api.ipynb- using spotify to get features of the songs in dataset
lab_kmeans_clustering.ipynb - This is for the kmeans clustering model

_libraries: contains a text file of libraries that I used

_models: contains all the cluster models in pickle format. The one used for the functions.py is kmeans_15.pickle

_scalers: contains the standard scaler file which is used in functions.py, standard_scaler.pickle


In the main branch of this repo, you will find already availble the main.ipynb and main.py, as well as a functions.py for easy running. 

Link to my presentation is this:
https://docs.google.com/presentation/d/1yXj_f92pGX6B9doz3tsxcNP0-D9TV5BQKafXwEwyyLI/edit?usp=sharing
