# Song Recommender Project Aaron Pereira
This is my submission for the GNOD project from Ironhack. Here I built a Song Recommender based on a K-Means Clustering model. 

To get an idea about the idea behind how this Song recommender works, please have a look at the Schematic diagram below.
But in a nutshell, a user enters the name of a song, if the song they chose is in the Hot 100, they will be recommended other Hot 100 songs. If the song is NOT in Hot 100, then they will be recommended similar NOT Hot songs based on certain song features extracted from Spotify. 

For the data to be used: 
   - first I made a dataset of the Billboard Hot 100 songs (containing just the song name and artist name). This was done by Web Scraping the Billboard Hot 100 website using Beautiful Soup on Python. 
   - Second I had a random dataset of 5000 songs which were NOT hot songs.
   - Third, for these songs I extracted multiple song features using Spotify's API through Spotipy on Python. This song feature data is used in the building of the K-Means Clustering model.    

**Attention**: to make the final function work you need to have a config file containing all your SpotifyAP credentials


## Contents
The folders present in this repo are:

- datasets : 
     - `hot100.csv` contains the billboard hot 100 songs,
     - `not_hot.csv` contains around 5000 not hot songs, 
     - `featsfinal.csv` contains spotify features of both nothot and hot100 songs combined, 
     - `feats_final_withclusters.csv` contains features and the clusters (This one is needed for the final function, but functioon knows filepath).

- functions:
     - `functions.py` which contains the song_recommender function. So import by entering:
            
            ```python
            import song_recommender from functions```

- jupyternotebooks: 
      
     Contains the following notebooks (here is the correct order of operation):
     - `lab_webscraping_single_page_aaron_pereira.ipynb` - webscrapping for music data from billboardhot 100.
     - `lab_not_hot_songs_aaron_pereira.ipynb`- webscraping from other sites
     - `lab_spotify_api.ipynb`- using spotify to get features of the songs in dataset
     - `lab_kmeans_clustering.ipynb` - This is for the kmeans clustering model

- libraries: 
      
     contains a text file of libraries that I used

- models: 
      
     contains all the cluster models in pickle format. The one used for the functions.py is kmeans_15.pickle

- scalers: 
     
     contains the standard scaler file which is used in functions.py, standard_scaler.pickle


- In the main branch of this repo, you will find already availble the main.ipynb and main.py, as well as a functions.py for easy running. 

## Presentation Link:
https://docs.google.com/presentation/d/1yXj_f92pGX6B9doz3tsxcNP0-D9TV5BQKafXwEwyyLI/edit?usp=sharing
