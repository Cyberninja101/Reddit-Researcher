# Reddit Researcher

## Project Description
The Reddit Researcher is a webapplication based in Flask, that allows users to view and download posts, comments, and images from Reddit. Utilizing the Reddit API, Reddit Researcher is a one stop solution for getting data for researchers, essentially a webscraper with UI. This application features a sleek webpage design that allows users to search for specific information on Reddit, and filter and search for it. Some filters include specific subreddits, users, type of data (post, comments, images, etc) and the total amount of data. This also uses NLP to analyze the sentiment of each post, which provides another feature for this dataset. Finally, the data is displayed on the webpage, and users have the option to download it in a CSV format. 

## How to use the Website?
The Reddit Research website has a very simple user interface. Run the main.py python file to start the website. Start by typing in the subreddit you want to research. For example, you can type in "wallstreetbets" to search up the wallstreetbets subreddit. I recommend you search on Google to get the exact spelling of the subreddit. You can also choose one of the four categories to filter your posts. Next, press enter. You might need to wait a few seconds for the results to load. When it does, you will be redirected to the results page with a table featuring the data for all of the posts. You can also download this data in a CSV format by clicking download data. The table also features scrolling overflow.

**IMPORTANT**: In a couple of weeks, Reddit is making their API cost money. As a result, my website won't work, and many subreddits such as r/chess and r/ftc are now set on private to protest against these changes. So if you search up a private subreddit, it will say "Forbidden". I assure you, my code is not broken. Right now, the r/askreddit subreddit is working, so you can try that as an example.

![User Interface](New_UI.png)
![Results Page](results.png)

## The Different Files
### main.py
The main python file running the flask webpage. 

### reddit.py
The python file running webscraping algorithms.

### nlp.py
The python file running sentiment analysis algorithms.

### home.html
The html file for the home page.

### result.html
The html file for the result page.

### home.css
The css file for the homepage design.

### home.js
The javascript file for the home page, controlling the button functionalities.


## Project Outcomes
### Abstraction
* Utilizes OOP and class structure to create webpage using Flask. 
* Uses functions and methods for the Reddit API.

### Algorithms
* Use advanced loops and conditionals to organize data from web scraping.

### Writing
* Use PEP 8 format to write clear and concise code.
* Use doctsrings and comments to make code more readable.

### Data Analysis
* Work with Reddit API to scrape data based on User parameters
* Organize and clean data to display to users


## Project Outline
Outline the overall structure of your code.  What is the file structure?  What classes will be created?  What functions?  What is the basic process your code uses to run?

Not 100% sure what the exact structure of my code will be. I will have a python file for obtaining data from Reddit API, a python file for the website's backend with flask, and multiple HTML and CSS files for the websites. I will need a few classes for the data and website parts, but I am not sure what exact classes and functions I will need. 

## Project Timeline
Use this timeline to map out your daily goals.  To start these goals should be the major steps in your project.  They might be a little sketchy at first, but as you work through the project, you should update your goals to be more and more specific.  Your goal for the next class should be the most specific goal.

Use "Not Started", "On track", "Behind", or "Ahead" to keep track of the status of each goal.

### Thursday May 25 - **DUE DATE**
**GOAL** --> Project Complete and Presented to Class (maybe host website??)
*STATUS* --> On track

### Tuesday May 23
**GOAL** --> Finished Designed website
*STATUS* --> On track 

### Friday May 19
**GOAL** --> Make it look prettier and cleaner UI
*STATUS* --> On track

### Wednesday May 17
**GOAL** --> Fully Functional website
*STATUS* --> On track

### Monday May 15
**GOAL** --> Website 50% complete
*STATUS* --> On track

### Thursday May 11
**GOAL** --> Basic structure of website
*STATUS* --> On track

### Tuesday May 9
**GOAL** --> Basic outline of website
*STATUS* --> On track

### Friday May 5
**GOAL** --> Finish Reddit API Data Stuff. By this point, I should be able to obtain csv results of specific info from reddit.
*STATUS* --> On track

### Wednesday May 3
**GOAL** --> Code for Webscraping 50% complete
*STATUS* --> Ahead

### Monday May 1
**GOAL** --> Research Reddit API
*STATUS* --> Ahead
