from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_source,get_articles
from models import Source,Articles

# Views
@main.route('/')
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

# @app.route('/source/<string:source_id>')
# def source(source_id):

#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     id = "abc-news"
#     return render_template('source.html',id = source_id)

@main.route('/source/<string:id>')
def source(id):

    '''
    View source page function that returns the source articles page and its data
    '''
    source = get_source(id)
    name = f'{source.name}'

    return render_template('source.html',name=name,source=source)

@main.route('/articles/<string:id>')
def articles(id):

    '''
    View source page function that returns the source articles page and its data
    '''
    articles = get_articles(id)
    name = f'{articles.name}'

    return render_template('articles.html',name=name,articles=articles)
