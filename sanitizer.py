import lyricsgenius
import pandas as pd

# import xlsx file of curse words from Wiki, convert to list

curse_words_df = list(pd.read_excel('all curse words.xlsx')['curse_words'])
curse_words_lower = []

for word in curse_words_df:
    new_word = word.replace('\xa0','')
    curse_words_lower.append(new_word)
    

# Create duplicate of list with capitalized words
curse_words_capital = []
for word in curse_words_lower:
    capitalized = word.capitalize()
    curse_words_capital.append(capitalized)
    
# concatenate lower case list and capitalized list
curse_words_list = curse_words_lower + curse_words_capital


def vet(song_name,artist_name):
    
    # use Genius API to retreive lyrics data
    genius = lyricsgenius.Genius("WqkTMJ4fumfrTuffmu_Ld4h40KVDccec7uoSEdx82EBnT-Qj5uVYXqYdvKc5rd9k")
    song = genius.search_song(song_name, artist_name)
    
    # remove unneccesary characters and split string into list
    lyrics = song.lyrics
    lyrics = lyrics.replace(".", "").replace(",", "").replace("!", "").replace("'", "").replace("\n", " ").replace("?", "")
    lyrics = lyrics.split()

    # list to store curse words in song    
    song_curse_words = []
    
    # iterate through each word in lyrics, check if it is in curse_words_list
    # if a word is a curse word, store in song_curse_words list
    res = []
    for word in lyrics:
        res.append(word)
        if word in curse_words_list :
            song_curse_words.append(word)

    
 

    res = ' '.join(map(str, res))
    if not song_curse_words:
        res = "This song is clean!" 
        return res
    song_curse_words = ' '.join(map(str, song_curse_words))
    song_curse_words = 'Bad words: ' + song_curse_words
    song_curse_words = song_curse_words  +  res 
    return song_curse_words
    # If song is clean...
    #if not song_curse_words:
        #print("\nClean Lyrics")
    
    # If song is explicit...
    #if song_curse_words:
        #print('\nExplicit lyrics detected!\n')
        #print(song_curse_words)  
        

