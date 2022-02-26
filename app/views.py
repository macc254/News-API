from flask import render_template
from app import app
from .requests import get_sources,get_source


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting business news
    general_news = get_sources('general')
    health_news = get_sources('health')
    technology_news = get_sources('technology')
    business_news = get_sources('business')

    title = 'Welcome to news hour!'
    return render_template('index.html',title = title,general=general_news,health=health_news,technology=technology_news,business=business_news)

@app.route('/source/<string:source_id>')
def source(source_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    id = "234"
    return render_template('source.html',id = source_id)

@app.route('/source/<int:id>')
def source(id):

    '''
    View source page function that returns the source articles page and its data
    '''
    source = get_source(id)
    title = f'{source.title}'

    return render_template('source.html',title = title,source= source)