class Artist:

    # TODO: Define constructor with parameters to initialize instance attributes
    #       (name, birth_year, death_year)
    def __init__(self, artist_name='unknown', year_birthed=-1, year_dead=-1):
        self.name = artist_name
        self.birth_year = year_birthed
        self.death_year = year_dead

    # TODO: Define print_info() method
    def print_info(self):
        print(self)


class Artwork:
    def __init__(self, art_title='unknown', art_year=-1, art_artist=-1):
        self.title = art_title
        self.year_created = art_year
        self.artist = art_artist

    # TODO: Define constructor with parameters to initialize instance attributes
    #       (title, year_created, artist)

    # TODO: Define print_info() method
    def print_info(self):
        print(self)


if __name__ == "__main__":
    user_artist_name = input('Input the artist name: ')
    user_birth_year = int(input('Input the birth year of the artist: '))
    user_death_year = int(input('Input the death year of the artist: '))
    user_title = input('Input the title of the artwork: ')
    user_year_created = int(input('Input the year the piece was painted: '))

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)

    user_artist.print_info()
    new_artwork.print_info()
