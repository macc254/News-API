from app import app
import urllib.request,json
from .models import source

Source = source.Source
# Getting api key
apiKey = app.config['NEWS_API_KEY']


# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['results']:
            source_results_list = get_source_response['results']
            source_results = process_results(source_results_list)


    return source_results

def process_results(source_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('original_name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')

       
        # there was an if append: here for a path,, add it if you find a path 
    if category:
        source_object = Source(id,name,description,url,category)
        source_results.append(source_object)

    return source_results

def get_source(id):
    get_source_details_url = base_url.format(id,apiKey)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)

        source_object = None
        if source_details_response:
            id = source_details_response.get('id')
            name = source_details_response.get('original_name')
            description = source_details_response.get('description')
            url= source_details_response.get('url')
            category = source_details_response.get('category')

            source_object = Source(id,name,description,url,category)
           

    return source_object