class Song:  
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        self.name = name
        self.artist = artist
        self.genre = genre

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        else:
            pass

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        else:
            pass

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count.keys():
            count = (cls.genre_count[genre] + 1)
            cls.genre_count.update({genre: count})
        else:
            cls.genre_count.update({genre: 1})

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count.keys():
            count = (cls.artist_count[artist] + 1)
            cls.artist_count.update({artist: count})
        else:
            cls.artist_count.update({artist: 1})
        

if __name__ == "__main__":
    print(Song.count)
    bad_romance = Song("Bad Romance", "Lady Gaga", "Pop")
    print(Song.count)
    print(Song.genre_count)
