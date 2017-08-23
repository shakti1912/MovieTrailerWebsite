import urllib
import json
"""This module will access 'The Movie Database' and get
movies data such as title, storyline, image url, trailer url. This file will also generate a json file called movies_file.json with
movies data. """


def download_all_movies_file():
    import urllib
    import gzip

    url = "http://files.tmdb.org/p/exports/movie_ids_04_28_2017.json.gz"
    urllib.urlretrieve(url, 'file.json.gz')

    f_out = open('downloadedMovies.json', 'w')
    f_in = gzip.open('file.json.gz', 'rb')
    f_out.write(f_in.read())


def get_configuration(api_key):
    request_url = "https://api.themoviedb.org/3/configuration?api_key=" + api_key
    connection = urllib.urlopen(request_url)
    configs = connection.read()
    configurations = json.loads(configs)
    return configurations


def get_movies_ids(file_name): # get all the movie ids whose popularity is greater than 25
    list = []
    fileHandler = open(file_name, 'r')
    lines = fileHandler.readlines()
    for line in lines:
        jsonObj = json.loads(line)
        if jsonObj['popularity'] > 25:
            list.append(jsonObj['id'])
    return list


def get_movies(api_key, movie_ids, configs):
    movies_file = open('movies_file.json', 'w')
    dict = {'results': []}
    for id in movie_ids:
        request_url ="https://api.themoviedb.org/3/movie/"+str(id)+"?api_key="+api_key + "&append_to_response=videos"
        connection = urllib.urlopen(request_url)
        movie_data = connection.read()
        data = json.loads(movie_data)
        title = data['original_title']
        storyline = data['overview']
        image_url = get_image_url(data['poster_path'], configs)
        key = data['videos']['results'][0]['key']
        trailer_url = get_trailer_url(key)
        movie_info = {'title': title,
                      'storyline': storyline,
                      'poster_image_url': image_url,
                      'trailer_youtube_url': trailer_url
                      }
        dict['results'].append(movie_info)
    json.dump(dict, movies_file)


def get_image_url(image_key, configs):
    url = configs['images']['base_url']+"w500"+image_key
    return url


def get_trailer_url(key):
    url = "https://www.youtube.com/watch?v="+key
    return url



