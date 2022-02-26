#!/usr/bin/env python3
import unittest
from models import articles
Articles = articles.Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sourceclass
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_Article = Articles("abc-news",'ABC NEWS',"Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","https://abcnews.go.com","general")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))


if __name__ == '__main__':
    unittest.main()