class Artist:


# TODO: Define constructor with parameters to initialize instance attributes
#       (name, birth_year, death_year)
    def __init__(self):
        self.name = 'unknown'
        self.birth_year = -1
        self.death_year = -1


# TODO: Define print_info() method
    def print_info(self):
        print()


class Artwork:


# TODO: Define constructor with parameters to initialize instance attributes
#       (title, year_created, artist)

# TODO: Define print_info() method


if __name__ == "__main__":
    user_artist_name = input()
    user_birth_year = int(input())
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)

    new_artwork.print_info()