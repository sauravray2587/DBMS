from flask import Flask, render_template, redirect, url_for, request
import feed 
import stories
from datetime import datetime
# Route for handling the login page logic
app = Flask(__name__)

import login_signup as _database
cur_user = -1

@app.route('/login', methods=['GET', 'POST'])
def login():
	global cur_user
	error = None
	if request.method == 'POST':
		# If login request
		if (request.form['submit-button'] == 'login'):
			print(request.form['username'], request.form['password'] )
			if _database.check_login(request.form['username'], request.form['password']) != True:
				error = 'Invalid Credentials. Please try again.'			
			else:
				cur_user = request.form['username']
				print(cur_user)
				return redirect(url_for('home', username = request.form['username']) )
		else:
			print(2)				
			_database.sign_up(request.form['username'], request.form['name'], request.form['password'], request.form['age'], request.form['email'])
			cur_user = request.form['username']
			return redirect(url_for('home', username = request.form['username']))
	return render_template('index.html', error=error)


@app.route('/home/<username>', methods=['GET', 'POST'])
def home(username):
	# return 'User %s' % username
	# Put Different Tabs for the different features
	print("Requesting Feed")
	feed_content = get_feed1(username, cur_user)

	if request.method == 'POST':
		if request.form['button']=="search_user":
			if True:
				print(request.form['search_text'])
				# Replace here with something else
				# Where to display the user?
				# search_for_user
				return redirect(url_for('profile', username = request.form['search_text']))
		elif request.form['button']=="My Profile":
			return redirect(url_for('profile', username = cur_user))
		elif request.form['button']=="tag_search":
			# tags = request.form['categories[]']
			# print(tags)
			# print("Hello")
			tag = request.form['tags']
			feed_content = get_feed_given_tags(tag)

			return render_template('feed.html', username = cur_user,  all_feeds = feed_content, all_tags = get_tags(), all_user = get_all_user(), all_comm = get_all_comm())
			# return "Tags are : %s" %request.form['tags']
		else:
			# .... insert a function to bookmark here
			feed_id = request.form['button']
			print(feed_id)
			return render_template('feed.html', username = cur_user,  all_feeds = feed_content, all_user = get_all_user(), all_comm = get_all_comm())


	return render_template('feed.html', username = cur_user,  all_feeds = feed_content, all_tags = get_tags(),all_user = get_all_user(), all_comm = get_all_comm())

@app.route('/profile/<username>', methods = ['GET', 'POST'])
def profile(username):
	print("username : ", username)
	feed_content = get_feed_user1(username)
	if (username == cur_user):
		display_follow = False
	else:
		display_follow = True

	is_following = True
	if request.method == 'POST':
		if request.form['button'] == 'bookmark':
			# .... insert a function to bookmark a post
			is_following = True
			# .... insert a function here to check is user1 follows user2
			return render_template('profile.html', all_feeds = feed_content, follow_status = is_following, display_follow = display_follow)
		else:
			if request.form['button'] == 'unfollow':
				# .... insert a function to unfollow a user
				is_following = False
			else:
				# .... insert a function to follow a user
				is_following = True
		return render_template('profile.html', all_feeds = feed_content, follow_status = is_following, display_follow = display_follow)
	else:
		return render_template('profile.html', all_feeds = feed_content, follow_status = is_following, display_follow = display_follow)



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
		comm = request.form['comm']
		# assign username here
		username = cur_user
		stories.user_post(username, content, 5, tags, comm)
		# post_to_database()
		return redirect(url_for('home', username = cur_user ))
	return render_template("post.html")

@app.route('/bookmark/<bookmark_id>', methods = ['GET', 'POST'])
def bookmark(bookmark_id):
	# .... a function here
	print("bookmarked, ", bookmark_id)
	return redirect(url_for('home', username = cur_user ))

def get_feed1(username, cur_user):
	database_active = True
	if database_active == True:
		feed_content = feed.get_feed(cur_user)
		print("feed len", len(feed_content))
		for x in feed_content:
			print("post post 1: ", x)
			x['post_time'] = x['post_time'].date()
			print("post post 2: ", x)
	else:
		temp = {}
		temp['username'] = 'random_user1'
		temp['date'] = '20/03/2019'
		temp['tags'] = ['ab', 'cd']
		temp['content'] = ['Hello Friends']
		temp['id'] = 2
		feed_content = [temp]
	return feed_content

def get_feed_user1(username):
	database_active = True
	if database_active == True:
		feed_content = stories.search_username(user, cur_user)
		print("feed len", len(feed_content))
		for x in feed_content:
			# print("post post 1: ", x)
			x['post_time'] = x['post_time'].date()
			print("post post 2: ", x)
	else:
		temp = {}
		temp['username'] = 'random_user1'
		temp['date'] = '20/03/2019'
		temp['tags'] = ['ab', 'cd']
		temp['content'] = ['Hello Friends, hahaha']
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

# def get_all_user():
# 	users = ['saurav', 'prashik', 'piyush', 'ritik']
# 	return users

# def get_all_comm():
# 	users = ['saurav', 'prashik', 'piyush', 'ritik']
# 	return users