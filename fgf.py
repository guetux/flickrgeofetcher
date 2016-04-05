#!/usr/bin/env python
# encoding: utf-8

import os
import flickrapi
import urllib2
import credentials

# Config values
directory = 'images'
number_of_photos_to_download = 1000
photos_per_page = 100


def fetch_images():
    flickr = flickrapi.FlickrAPI(credentials.api_key, credentials.api_secret, format='parsed-json')
    downloaded = 0
    page = 1

    while (downloaded < number_of_photos_to_download):
        page_size = min(number_of_photos_to_download - downloaded, photos_per_page)
        search_results = flickr.photos.search(has_geo=True, per_page=page_size, page=page, extras='original_format')

        for photo in search_results['photos']['photo']:
            if 'originalsecret' in photo and photo.get('originalformat', '') == 'jpg':
                try:
                    url = 'https://farm{farm}.staticflickr.com/{server}/{id}_{originalsecret}_o.jpg'.format(**photo)
                    download(url)
                    print("[OK] %s" % url)
                except:
                    print("[FAIL] %s" % url)
                finally:
                    downloaded += 1

        page += 1


def download(url):
    file_name = os.path.basename(url)
    file_path = os.path.join(directory, file_name)
    request = urllib2.urlopen(url)

    with open(file_path, "wb") as file:
        file.write(request.read())


if __name__ == "__main__":

    if not os.path.exists(directory):
        os.makedirs(directory)

    fetch_images()