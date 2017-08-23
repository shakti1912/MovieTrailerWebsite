import media
import json
import AccessAPI as access
import fresh_tomatoes


def make_movie_object(data):
    movies_list = []
    for movie in data['results']:
        type(movie)
        movie_object = movie['title']
        movie_object = media.Movie(movie['title'], movie['storyline'], movie['poster_image_url'], movie['trailer_youtube_url'])
        movies_list.append(movie_object)
    return movies_list


def main_caller():
    # calling methods to get movies info and save them in movies_file.json file.
    access.download_all_movies_file()
    api_key = "Put the movie database(TMdb) API KEY here."    # get api key from https://www.themoviedb.org/documentation/api
    conf = access.get_configuration(api_key)
    list = access.get_movies_ids('downloadedMovies.json')
    access.get_movies(api_key, list, conf)



# Program starts from here. First it downloads a gzip file the extract that file to create downloadedMovies.json file.
# from that json file, all the movies with popularity greater than 25 are selected and written in  movies_file.json.
# this json is used to create movie objects and stored them in a list and then fresh_tomatoes.py's
# open_movies_page function is called to open webbrowser and display movies and their trailers.

main_caller()    # this creates movies_file.json file
movies_data = open('movies_file.json', 'r')
jsonData = json.loads(movies_data.read())
list_of_movies = make_movie_object(jsonData)
print list_of_movies[0].title

# this creates movies webpage
fresh_tomatoes.open_movies_page(list_of_movies)
