### News-Api
Repo link: https://github.com/macc254/News-API.git
## Project description

- This is a web app that lists news articles from various sources that they get to choose.

## BDD
- A user should be able to see various news sources on the source route of the application
- A user should be able to select a news source and see all news articles from the selected news source in the application
- A user see the image, description and the time a news article was created.
- A user should click on an article and read the full article on the source website.


### Set-up instructions

- Install Python3 installed in your machine together with venv and pip.
- Set up the virtual environment and activate it

$ python3.8 -m venv virtual
$ source virtual/bin/activate


- Install all the necessary modules

$ git clone https://github.com/macc254/News-API.git
- Navigate into the cloned project.

$ cd news-api

Create a start.sh file
- $ touch start.sh

On your start.sh file , add your API key from [News API](https://newsapi.org) and the command for executing manage.py (python3 manage.py server), which will start the server.

In your start.sh file, also export NEWS_API_KEY='<YOUR_API_KEY>' to your local machine

Give the file execution permissions.
- $ chmod a+x start.sh

command to run your application
- $ ./start.sh

## Technologies Used

- Python (Flask)
- Jinja2
- HTML
- CSS
- Bootstrap

## LICENCE
Copyright 2022 Mercy Bore.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.