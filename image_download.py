from urllib.request import urlretrieve
import backend.psql_handlers as psql

def downloadImages():
    all_media_info = psql.get_images()
    for item in all_media_info:
        urlretrieve(item[1], f'image_holder/{item[0]}')
