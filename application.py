from flask import Flask, render_template, redirect, url_for, request

# Route for handling the login page logic
app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home', username = request.form['username']))
    return render_template('index.html', error=error)

@app.route('/home/<username>', methods = ['GET', 'POST'])
def home(username):
	# return 'User %s' % username
	temp = {}
	temp['username'] = 'saurav'
	temp['date'] = '20/11/2019'
	temp['tags'] = ['ab', 'cd']
	temp['content'] = ['Hello Friends']
	feed_content = []
	feed_content.append(temp)
	return render_template('feed.html', all_feeds = feed_content)