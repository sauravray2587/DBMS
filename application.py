from flask import Flask, render_template, redirect, url_for, request

# Route for handling the login page logic
app = Flask(__name__)

import login_signup as _database
cur_user = -1

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if (request.form['submit-button'] == 'login'):
			print(1)
			if _database.check_login(request.form['username'], request.form['password']) == False:
				error = 'Invalid Credentials. Please try again.'			
			else:
				return redirect(url_for('home', username = request.form['username']))
		else:
			print(2)				
			_database.sign_up(request.form['username'], request.form['name'], request.form['password'], request.form['age'], request.form['email'])
			cur_user = request.form['username']
			return redirect(url_for('home', username = request.form['username']))
	return render_template('index.html', error=error)

@app.route('/home/<username>', methods = ['GET', 'POST'])
def home(username):
	# return 'User %s' % username
	# Put Different Tabs for the different features
	database_active = False
	if database_active == True:
		feed_content = find_feeds(username)
	else:
		temp = {}
		temp['username'] = 'random_user1'
		temp['date'] = '20/03/2019'
		temp['tags'] = ['ab', 'cd']
		temp['content'] = ['Hello Friends']
		temp['id'] = 1
		feed_content = [temp]

	if request.method == 'POST':
		if request.form['button']=="search_user":
			if True:
				print(request.form['search_text'])
				# Replace here with something else
				# Where to display the user?
				# search_for_user
				return redirect(url_for('profile', username = request.form['search_text']))
		elif request.form['button']=="user_post":
			return redirect(url_for('myfeeds', username = cur_user))
		elif request.form['button']=="tag_search":
			return "Tags are : %s" %request.form['tags']

	return render_template('feed.html', all_feeds = feed_content)

@app.route('/profile/<username>', methods = ['GET', 'POST'])
def profile(username):
	database_active = False
	if database_active == True:
		feed_content = get_my_feeds(username)
	else:
		temp = {}
		temp['username'] = 'random_user1'
		temp['date'] = '20/03/2019'
		temp['tags'] = ['ab', 'cd']
		temp['content'] = ['Hello Friends']
		temp['id'] = 1
		feed_content = [temp]
	if request.method == 'POST':
		return "%s is now following %s" %(cur_user, username)
		# follow_user(username, cur_user)
	return render_template('profile.html', all_feeds = feed_content)


@app.route('/myfeeds/<username>', methods = ['GET', 'POST'])
def myfeeds(username):
	database_active = False
	if database_active == True:
		feed_content = get_my_feeds(username)
	else:
		temp = {}
		temp['username'] = 'random_user1'
		temp['date'] = '20/03/2019'
		temp['tags'] = ['ab', 'cd']
		temp['content'] = ['Hello Friends']
		temp['id'] = 1
		feed_content = [temp]
	return render_template('feed.html', all_feeds = feed_content)


@app.route('/bookmark/<feed_content>/<feed_id>', methods = ['GET', 'POST'])
def bookmark(feed_content, feed_id):
	# add_to_bookmarks(feed_number, username)
	# return "Feed Number %s, bookmarked" 
	return render_template('feed.html', all_feeds = feed_content)

@app.route('/post', methods = ['GET', 'POST'])
def post():
	# add_to_bookmarks(feed_number, username)
	if request.method == 'POST':
		content = request.form['user_post']
		tags = request.form['tags']
		tags = tags.replace(" ", "")
		tags = tags.split(',')
		# assign username here
		username = 'saurav'
		# post_to_database()
		return "Your Post Submitted"
	return render_template("post.html")


def addBookmark(x):
    print("Hello")
    print(x)
    return False