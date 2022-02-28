# TheALLDictionary
CSE 416 final project at the State University of New York Korea (SUNY Korea)

## About Members and Roles

#### Young-jae (Bush) Moon
* Role: Product owner and Project manager
* Email: youngjae.moon@stonybrook.edu

#### Yoora Kim 
* Role: Lead programmer
* Email: yoora.kim@stonybrook.edu

#### Seo-young Ko 
* Role: Designer
* Email: seoyoung.ko@stonybrook.edu

#### Seung-jae Kang 
* Role: Designer
* Email: seungjae.kang@stonybrook.edu

## Advisor

#### Professor Alexander Kuhn
* Teaching Assistant Professor in Computer Science at SUNY Korea

## Problem

When people do not know an English word, they have to search its definition from a dictionary. Although they may be satisfied with the meanings and the example sentences given from the dictionary, they may also be dissatisfied when they cannot fully grasp the word after reading the dictionary’s explanations. In this case, they then have to search its meaning through other dictionaries, encyclopedias or search relevant photos or videos from Google or YouTube for full understandings.

## Solution 

“TheALLDictionary” is a web-based application that helps people to search the meanings of the term from Merriam-Webster’s Learner’s dictionary, Merriam-Webster dictionary, Oxford English Dictionary, Urban dictionary, WordNet, synonym.com Wiktionary, Wikipedia, Google News, Google Images, YouTube at once. Here Merriam-Webster’s Learner’s is the easiest dictionary in which the terms are explained in most simple and plain English. By contrast, the Merriam-Webster dictionary explains the terms at the intermediate level, and the Oxford English Dictionary explains them at more advanced levels. Thus, the Urban dictionary is especially useful for finding the definitions of slang words. Hence the user can find the explanations of the term at various levels from each dictionary. Thus, if a dictionary is not sufficient to understand the meaning of the word, then the user can refer to Wikipedia, Google News, Google Images and YouTube videos to understand more thoroughly.

The target audience of TheALLDictionary is someone who wants to search for the definition of an English word. Nonetheless, it is expected that students who learn English at school will use this application most frequently. Therefore, TheALLDictionary will include additional features that help people to memorise the vocabularies that they have searched for. These features include creating and shuffling note cards for testing their learnings, creating and taking sample exams, sharing note cards that the user has made to its friends.

## Tools and technologies

### Programming languages and Database Management System (DBMS) used

1. JavaScript (ECMAScript 2020)
2. MySQL (MySQL Community Edition 8.0.24)
3. Python (3.9.4)

### Frameworks used

1. Bootstrap front-end framework (v5.0.0-beta 3)
2. Flask framework (v1.1.2)

### Libraries used

1. WerkZeug (1.0.1)

Note that we decided not to use React and only use Bootstrap.

### Application Programming Interfaces (API) used

1. Custom Search JSON API (v1)
2. Merriam-Webster's Learner's Dictionary with Audio (v3)
3. Merriam-Webster's Collegiate® Dictionary with Audio (v3)
4. Oxford Dictionaries API (v2.5)

Note that we decided to not use INIAPI (v1) for implementing KG Inicis payment system because Merriam-Webster APIs are free to use only for non-commercial purposes. Thus, YouTube Data API was not needed to show search results from YouTube. We have instead used a different third-party package to gain the list of videos from YouTube search.

### External Storage used

1. Amazon Relational Database Service (RDS)
2. Amazon S3

### Third-party packages used

1. beautifulsoup4 (4.9.3)
2. Flask-Bootstrap (3.3.7.1)
3. Flask-MySQLdb (0.2.0)
4. flask-restx (0.3.0)
5. Flask-SocketIO (5.0.1)
6. google-api-python-client (2.2.0)
7. GoogleNews (1.5.7)
8. gunicorn (20.1.0)
9. MySQL Connector/Python (8.0.24)
10. PyDictionary (2.0.1)
11. requests (2.25.1)
12. udpy (2.0.0)
13. Wikipedia-API (0.5.4)
14. wiktionaryparser (0.0.97)
15. youtube-search-python (1.4.3)

Note that we decided not to use oxforddictionaries (0.1.101) as a Python wrapper for Oxford Dictionaries API, because it is a wrapper that only supports Oxford Dictionaries v1. Thus, we found out ways to implement without using this wrapper.

## Instructions for checking out the latest stable version

### Method 1:
1. Open the main page for our GitHub repository: https://github.com/yr2351/cse416
2. Click the following button: <img src = "https://user-images.githubusercontent.com/63883314/115416097-69ade280-a232-11eb-8401-8c41362ab4c2.png" width="44" height="14">
3. Click 'Download ZIP' option.
4. Unzip the folder.

### Method 2:
1.  Copy the web URL to your clipboard.
2.  Open 'Git Bash' from your local computer. You must have installed Git from the following page to do this: https://git-scm.com/downloads
3.  Move to the preferred directory.
4.  Next, type the following:
```
git clone
```
5. Then, all the codes and documents in the repository can be accessed.

Note: For Method 2, if you have already cloned the repository before, then you can skip the first two steps. And type this instead for step 4:
```
git type
```

## How to build this software

Note that the instructions are intended to work on Windows 10 because all the codes have been written in Windows 10 environment.

### 1. Please make sure you have downloaded MySQL (v8.0.24).

* Here is the URL for downloading the MySQL installer for Windows: https://dev.mysql.com/downloads/installer/
* Here is the URL that shows the instructions to install MySQL on macOS: https://dev.mysql.com/doc/mysql-osx-excerpt/5.7/en/osx-installation.html 

### 2. Install the following python packages using pip in the terminal:

```
pip install beautifulsoup4
pip install flask
pip install flask-bootstrap
pip install Flask-MySQLdb
pip install flask-restx
pip install flask-socketio
pip install google-api-python-client
pip install GoogleNews
pip3 install gunicorn
pip install mysql-connector-python
pip install PyDictionary
pip install requests
pip install udpy
pip install Werkzeug
pip install wikipedia-api
pip install wiktionaryparser
pip3 install youtube-search-python
```

### 3. Deployment method

#### We will use Heroku to deploy the Flask. Note that:
 1. Git must be installed since Heroku uses Git. Please install Git from this website unless you have already installed: https://git-scm.com/downloads
 2. Python must be installed to use Flask. Please install Python 3.9.4 from this website unless you have already installed: https://www.python.org/downloads/

#### To install Heroku,
 1. Open the Heroku website. Here is the link for the Heroku website: https://www.heroku.com/
 2. Sign up a Heroku account.
 3. Install Heroku command-line interface (CLI) in your Terminal.
 ```
 brew tap heroku/brew && brew install heroku
 ```
 
 #### To use Heroku for deploying our application,
 1. Make sure you have already installed Flask and Gunicorn. Check "How to build software" section to refer the installation processes for each of them.
 2. Create requirements.txt and make sure requirements.txt contains gunicorn.
 ```
 pip3 freeze
 pip3 freeze > requirements.txt
 ```
3. Create Profile 
 
    Format: process type: command
 
4. Go to Heroku website again and create an application. 
 
    App name: thealldictionary
    
5. Login to your Heroku account in the terminal.
 ```
 heroku login
 ```
6. Clone the repository using Git.  
 ```
 heroku git:clone -a thealldictionary
 ```
7. Make the following changes to Heroku using Git.
 ```
 cd thealldictionary
 git add .
 git commit -am "First Commit"
 git push heroku master
```
8. If the following steps run successfully, the website URL will be printed in the console. 
```
https://thealldictionary.herokuapp.com/
```

## How to test this software

* To test the software, you shall initially download the latest stable version of this software. Please refer "Instructions for checking out the latest stable version" to do this.

### Instructions for testing signup.py
1. Connect with MySQL server and enter queries (account, useraccount, adminaccount)
2. Run the signup.py
3. Open http://127.0.0.1:5000/signup
4. Enter the information required to join in the signup form
5. If the sign-up is successful, the following message will be printed in the Python console:
```
You have successfully registered !
```
6. If the userID is already exist, the following message will be printed in the Python console:
```
Account already exists !
```
7. Check the entered data from MySQL console

### Instructions for testing signin.py
1. Connect with MySQL server and enter queries (account, useraccount, adminaccount)
2. Follow the step from testing signup.py above unless you can manually insert the data on db.
3. Run the signin.py
4. Open http://127.0.0.1:5000/signin
5. Enter ID, password and click submit
6. If the user typed in correct ID and password, page will be redirected to search page
7. Else will remain on the same page

### Instructions for testing app.py
( I merged signin.py and signup.py and I include search function. so I will explain only testing search in this part. )
1. Change the name of the web_view folder into static.
2. Run the app.py
3. Open http://127.0.0.1:5000
4. Enter the word in the search box, and click the magnifying glass button on the right.
5. The defition of word will be shown the page. (It hasn't been organized yet)
6. The user can search other words by using search box on the top.

## Bug tracking

* All users can view and report a bug in "GitHub Issues" of our repository. 
* Here is the URL for viewing and reporting a list of bugs: https://github.com/yr2351/cse416/issues
