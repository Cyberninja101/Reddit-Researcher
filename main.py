from flask import Flask, redirect, url_for, render_template, request
import reddit
import os

app = Flask(__name__)

# Default category
sort_category = "hot"

@app.route("/")
def home():
    """
    This is the home/default page. This is where the user can 
    search up different subreddits, and sort the posts.  
    """
    return render_template("home.html")

@app.route('/result',methods = ['POST'])
def result():
    """
    This is the results page. The results show up after the user
    searches for a subreddit. The user can download the results
    in a CSV file.

    POST method: This page takes a POST request of the form the
                 home page, and scrapes Reddit using the API by
                 calling the get_submission function from reddit.py.
                 After getting the results, it returns the result
                 page and displays it in a table.
    """
    if request.method == 'POST':
        result = request.form # From home page
        print("my result is: " + str(result["subreddit"]))

        # take top 5 posts from subreddit
        df = reddit.get_submission([result["subreddit"]], sort_category, path = os.getcwd(), n=5, mode=1)

        # Redirects to new page with these results
        return render_template("result.html",result = df)

# Button press filtering
@app.route('/filter/<category>')
def filter(category):
    """
    This is not a web page. This route function saves the 
    category filter choice from the home page. It works by
    setting the category variable for the result page.
    """

    print(f"category is {category}")
    
    # set variable
    global sort_category
    sort_category = category

if __name__ == "__main__":
    app.run(debug=True) # Set debug = True for live changes in development

