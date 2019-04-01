from flask import Flask, render_template, redirect, url_for, request

# Route for handling the login page logic
app = Flask(__name__)

import login_signup as _database
cur_user = -1

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	global cur_user
	error = None
	if request.method == 'POST':
		if (request.form['submit-button'] == 'login'):
			print(request.form['username'], request.form['password'] )
			if _database.check_login(request.form['username'], request.form['password']) != True:
				error = 'Invalid Credentials. Please try again.'			
			else:
				cur_user = request.form['username']
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
	feed_content = get_feed(username)

	if request.method == 'POST':
		if request.form['button']=="search_user":
			if True:
				print(request.form['search_text'])
				# Replace here with something else
				# Where to display the user?
				# search_for_user
				return redirect(url_for('profile', username = request.form['search_text']))
		elif request.form['button']=="My Profile":
			return redirect(url_for('myfeeds', username = cur_user))
		elif request.form['button']=="tag_search":
			# tags = request.form['categories[]']
			# print(tags)
			# print("Hello")
			tag = request.form['tags']
			feed_content = get_feed_given_tags(tag)

			return render_template('feed.html', username = cur_user,  all_feeds = feed_content, all_tags = get_tags())
			# return "Tags are : %s" %request.form['tags']
		elif request.form['button']=="bookmark":
			# .... insert a function to bookmark here
			return render_template('feed.html', username = cur_user,  all_feeds = feed_content)


	return render_template('feed.html', username = cur_user,  all_feeds = feed_content, all_tags = get_tags())

@app.route('/profile/<username>', methods = ['GET', 'POST'])
def profile(username):
	feed_content = get_feed(username)
	is_following = True
	if request.method == 'POST':
		if request.form['button'] == 'bookmark':
			# .... insert a function to bookmark a post
			is_following = True
			# .... insert a function here to check is user1 follows user2
			return render_template('profile.html', all_feeds = feed_content, follow_status = is_following)
		else:
			if request.form['button'] == 'unfollow':
				# .... insert a function to unfollow a user
				is_following = False
			else:
				# .... insert a function to follow a user
				is_following = True
		return render_template('profile.html', all_feeds = feed_content, follow_status = is_following)
	else:
		return render_template('profile.html', all_feeds = feed_content, follow_status = is_following)


@app.route('/myfeeds/<username>', methods = ['GET', 'POST'])
def myfeeds(username):
	feed_content = get_feed(username)
	return render_template('feed.html', username = cur_user,  all_feeds = feed_content)


# @app.route('/bookmark/<feed_id>', methods = ['GET', 'POST'])
# def bookmark(feed_id):
# 	print(cur_user)
# 	# add_to_bookmarks(feed_number, username)
# 	# return "Feed Number %s, bookmarked" 
# 	return redirect(url_for('home', username = cur_user))

@app.route('/post', methods = ['GET', 'POST'])
def post():
	# add_to_bookmarks(feed_number, username)
	if request.method == 'POST':
		content = request.form['content']
		
		tags = request.form['tags']
		tags = tags.replace(" ", "")
		tags = tags.split(',')
		
		preq = request.form['preq']
		preq = preq.replace(" ", "")
		preq = preq.split(',')
		# assign username here
		username = cur_user
		# post_to_database()
		return "Your Post Submitted"
	return render_template("post.html")

def get_feed(username):
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
	return feed_content

def get_tags():
	database_active = False
	if database_active == True:
		all_tags = get_all_tags()
	else:
		all_tags = ['artifical intelligence', 'operating systems']
	return all_tags