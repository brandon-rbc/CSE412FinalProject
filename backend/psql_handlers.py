import operator
from datetime import date
import random

import psycopg2

# Connection to psql database and all query handling

connection = psycopg2.connect(user="acgfo",
                              password="",
                              host="127.0.0.1",
                              port="5432",
                              database="acgfo")

cursor = connection.cursor()

#connects to local database
def main():
    try:
        connection = psycopg2.connect(user="acgfo",
                                      password="",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="acgfo")

        cursor = connection.cursor()
    except(Exception, psycopg2.Error) as error:
        print(f"Failure connecting to psql: {error}")
    else:
        print('Successful connection to psql!')

#performs sql query to get images from database
def get_images():
    cursor.execute(r'SELECT "mediaObject".mediaID, "mediaObject".poster_url FROM "mediaObject";')
    result = cursor.fetchone()
    img_list = []
    while result:
        # print(record)
        img_list.append(result)
        result = cursor.fetchone()
    return img_list

#performs sql query to get number of favorites of inputted user
def getNumFavs(id):
    cursor.execute(f'SELECT COUNT(*) FROM "favoritedBy" '
                   f'WHERE "favoritedBy".userID = {id};')
    result = cursor.fetchone()
    return result[0]

#performs sql query to find mediaObjects based on sort method, search method, and search query
def getSearchMedia(sort_method, search_method, search_query):
    media_list = []
    search_query = search_query.upper()
    if search_method == 'Title':
        cursor.execute(f"SELECT \"mediaObject\".name, \"mediaObject\".poster_url, \"mediaObject\".mediaID, \"mediaObject\".rating FROM \"mediaObject\", \"show\" "
                       f"WHERE upper(\"mediaObject\".name) LIKE '%{search_query}%' "
                       f"AND \"mediaObject\".mediaID = \"show\".mediaID; ")
        result = cursor.fetchone()
        while result:
            temp = (result[0], result[1], result[2], result[3], 'show')
            media_list.append(temp)
            result = cursor.fetchone()
        cursor.execute(f"SELECT \"mediaObject\".name, \"mediaObject\".poster_url, \"mediaObject\".mediaID, \"mediaObject\".rating FROM \"mediaObject\", \"movie\" "
            f"WHERE upper(\"mediaObject\".name) LIKE '%{search_query}%' "
            f"AND \"mediaObject\".mediaID = \"movie\".mediaID; ")
        result = cursor.fetchone()
        while result:
            temp = (result[0], result[1], result[2], result[3], 'movie')
            media_list.append(temp)
            result = cursor.fetchone()
    elif search_method == 'Director':
        cursor.execute(f"SELECT \"director\".directorID FROM \"director\""
                       f"WHERE upper(\"director\".name) LIKE '%{search_query}%';")
        result = cursor.fetchone()
        ids = []
        while result:
            ids.append(result[0])
            result = cursor.fetchone()
        for id in ids:
            cursor.execute(f"SELECT \"mediaObject\".name, \"mediaObject\".poster_url, \"mediaObject\".mediaID, \"mediaObject\".rating  FROM \"mediaObject\",\"director\" ,\"directs\", \"show\" "
                           f"WHERE \"directs\".directorID = {id} "
                           f"AND \"directs\".directorID = \"director\".directorID "
                           f"AND \"directs\".mediaID = \"mediaObject\".mediaID "
                           f"AND \"mediaObject\".mediaID = \"show\".mediaID;")
            result = cursor.fetchone()
            while result:
                temp = (result[0], result[1], result[2], result[3], 'show')
                media_list.append(temp)
                result = cursor.fetchone()
            cursor.execute(
                f"SELECT \"mediaObject\".name, \"mediaObject\".poster_url, \"mediaObject\".mediaID, \"mediaObject\".rating  FROM \"mediaObject\",\"director\" ,\"directs\", \"movie\" "
                f"WHERE \"directs\".directorID = {id} "
                f"AND \"directs\".directorID = \"director\".directorID "
                f"AND \"directs\".mediaID = \"mediaObject\".mediaID "
                f"AND \"mediaObject\".mediaID = \"movie\".mediaID;")
            result = cursor.fetchone()
            while result:
                temp = (result[0], result[1], result[2], result[3], 'movie')
                media_list.append(temp)
                result = cursor.fetchone()
    elif search_method == 'Genre':
        cursor.execute(f'SELECT "mediaObject".name, "mediaObject".poster_url, "mediaObject".genres, "mediaObject".mediaID, "mediaObject".rating FROM \"mediaObject\", \"show\" '
                       f'WHERE \"mediaObject\".mediaID = \"show\".mediaID;')
        result = cursor.fetchone()
        while result:
            genreFound = False
            for genre in result[2]:
                genre = genre.upper()
                if genre.find(search_query) != -1:
                    genreFound = True
            if genreFound:
                temp = (result[0], result[1], result[3], result[4], 'show')
                media_list.append(temp)
            result = cursor.fetchone()
        cursor.execute(
            f'SELECT "mediaObject".name, "mediaObject".poster_url, "mediaObject".genres, "mediaObject".mediaID, "mediaObject".rating  FROM \"mediaObject\", \"movie\" '
            f'WHERE \"mediaObject\".mediaID = \"movie\".mediaID;')
        result = cursor.fetchone()
        while result:
            genreFound = False
            for genre in result[2]:
                if genre.find(search_query) != -1:
                    genreFound = True
            if genreFound:
                temp = (result[0], result[1], result[3], result[4], 'movie')
                media_list.append(temp)
            result = cursor.fetchone()

    if sort_method == 'Rating':
        media_list = sorted(media_list, key=operator.itemgetter(3))
        media_list.reverse()
    else:
        media_list = sorted(media_list, key=operator.itemgetter(0))
    return media_list

#creates new user based on inputted data and updates
def updateUserInfo(username, age, gender, sort_method):
    cursor.execute(f'SELECT "user".userID FROM "user" '  
                   f'WHERE "user".username = \'{username}\' '
                   f'AND "user".age = {age}'
                   f'AND "user".gender = \'{gender}\';')
    result = cursor.fetchone()

    if not result:
        userID = random.randrange(6, 1000)
        # print(id)
        cursor.execute(f'SELECT * FROM "user" '
                       f'WHERE "user".userID = {userID};')
        result = cursor.fetchone()
        while result:
            cursor.execute(f'SELECT * FROM "user" '
                           f'WHERE "user".userID = {userID};')
            result = cursor.fetchone()

        cursor.execute(f"INSERT INTO \"user\" VALUES ('{userID}', '{age}', '{username}', '{gender}');")
        print('new user created!')
    else:
        userID = result[0]

    cursor.execute(f'SELECT * FROM "favoritedBy" '  
                   f'WHERE "favoritedBy".userID = {userID};')
    result = cursor.fetchone()
    favoriteList = []
    return_list = []
    sorted_list = []
    while result:
        favoriteList.append(result)
        result = cursor.fetchone()
    for item in favoriteList:
        type_of_media = ''
        cursor.execute(f'SELECT "mediaObject".name FROM "mediaObject" '  
                   f'WHERE "mediaObject".mediaID = {item[1]};')
        result = cursor.fetchone()
        temp_name = result[0]

        cursor.execute(f'SELECT "show".mediaID FROM "show" '
                       f'WHERE "show".mediaID = {item[1]};')
        result = cursor.fetchone()
        rating = 0
        if result:
            cursor.execute(f'SELECT "mediaObject".rating FROM "mediaObject" '
                           f'WHERE "mediaObject".mediaID = {result[0]};')
            result = cursor.fetchone()
            rating = result[0]
            type_of_media = 'show'
        else:
            # print(item[1])
            cursor.execute(f'SELECT "mediaObject".rating FROM "mediaObject" '
                           f'WHERE "mediaObject".mediaID = {item[1]};')
            result = cursor.fetchone()
            rating = result[0]
            type_of_media = 'movie'
        temp = (item[0], item[1], temp_name, type_of_media, rating) # userID, mediaID, name, show/movie, rating
        return_list.append(temp)
        if sort_method == 'Rating':
            sorted_list = sorted(return_list, key=operator.itemgetter(4))
            sorted_list.reverse()
        else:
            sorted_list = sorted(return_list, key=operator.itemgetter(2))
    # print(sorted_list)

    return(userID, sorted_list)

#performs sql query to add favorite to user
def addFavorite(userID, mediaID):
    cursor.execute(f"INSERT INTO \"favoritedBy\" VALUES ('{userID}', '{mediaID}', '{date.today()}');")

#performs sql query to remove favorite from user
def removeFavorite(userID, mediaID):
    cursor.execute(f"DELETE FROM \"favoritedBy\" WHERE \"favoritedBy\".userID = {userID} AND \"favoritedBy\".mediaID = {mediaID}")
    cursor.execute(
        f"SELECT * FROM \"favoritedBy\" WHERE \"favoritedBy\".userID = {userID} AND \"favoritedBy\".mediaID = {mediaID}")
    result = cursor.fetchone()
    while result:
        # print(result)
        result = cursor.fetchone()

#performs sql query to check if mediaID is in user favorites list
def checkInFavorites(userID, mediaID):
    cursor.execute(f"SELECT * FROM \"favoritedBy\" WHERE \"favoritedBy\".userID = {userID} AND \"favoritedBy\".mediaID = {mediaID}")
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False

#returns mediaID of inputted media name
def getMediaID(name):
    temp = name.replace("'", "''")
    cursor.execute(f'SELECT "mediaObject".mediaID FROM "mediaObject" '
                   f'WHERE "mediaObject".name = \'{temp}\';')
    result = cursor.fetchone()
    # print(result[0])
    return result[0]

#returns info of given show name
def getShowInfo(name):
    temp = name.replace("'", "''")
    cursor.execute(f'SELECT * FROM "mediaObject" '
                   f'WHERE "mediaObject".name = \'{temp}\';')
    result = cursor.fetchone()
    # print(result)
    id, title, synopsis, year, genres, rating = result[0], result[1], result[2], result[3], result[5], result[6]
    cursor.execute(f'SELECT "show".numEpisodes, "show".numSeasons FROM "show" '
                   f'WHERE "show".mediaID = \'{id}\';')
    result = cursor.fetchone()
    numSeasons, numEpisodes = result[1], result[0]



    cursor.execute(f"SELECT \"directs\".directorID FROM \"directs\" "
                   f"WHERE \"directs\".mediaID = {id};")
    result = cursor.fetchone()
    directorid = result[0]
    cursor.execute(f"SELECT \"director\".name FROM \"director\" "
                   f"WHERE \"director\".directorID = {directorid};")
    result = cursor.fetchone()
    director = result[0]
    return id, year, director, genres, numSeasons, numEpisodes, synopsis, rating

#returns info of given movie name
def getMovieInfo(name):
    temp = name.replace("'", "''")
    cursor.execute(f'SELECT * FROM "mediaObject" '
                   f'WHERE "mediaObject".name = \'{temp}\';')
    result = cursor.fetchone()
    # print(result)
    id, title, synopsis, year, genres, rating = result[0], result[1], result[2], result[3], result[5], result[6]
    cursor.execute(f'SELECT "movie".runtime FROM "movie" '
                   f'WHERE "movie".mediaID = \'{id}\';')
    result = cursor.fetchone()
    runtime = result[0]

    cursor.execute(f"SELECT \"directs\".directorID FROM \"directs\" "
                   f"WHERE \"directs\".mediaID = {id};")
    result = cursor.fetchone()
    directorid = result[0]
    cursor.execute(f"SELECT \"director\".name FROM \"director\" "
                   f"WHERE \"director\".directorID = {directorid};")
    result = cursor.fetchone()
    director = result[0]
    return id, year, director, genres, runtime, synopsis, rating