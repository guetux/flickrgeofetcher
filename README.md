
Flickr GEO Fetcher
==================

Need a lot of geo-tagged images from all around the world? This stupid little python script gives you the amount you need by fetching them from flickr.

First, install flickrapi:

    pip install flickrapi

Then, adapt `fgf.py` to your needs:

    # Flickr credentials
    api_key = u'YOUR_API_KEY'
    api_secret = u'YOUR_API_SECRET'

    # Config values
    directory = 'images'
    number_of_photos_to_download = 1000
    photos_per_page = 100
    
Finally, run that bastard:

    ./fgf.py

Now sit back and relax while pix are flying in. This may take a looot of time ;-)