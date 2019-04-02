from flask import Flask, render_template, redirect, url_for, request
import feed 
import stories
from datetime import datetime
from get_all import *
from following import *
import bookmark as bm
from search_queries import *
from upvote import *
from prerequisite import *
from community import *
from config import *
# Route for handling the login page logic
app = Flask(__name__)

import login_signup as _database
cur_user = -1
last_user = -1

@app.route('/', methods=['GET', 'POST'])
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
				last_user = cur_user
				print(cur_user)
				return redirect(url_for('home', username = request.form['username']) )
		else:
			print(2)				
			_database.sign_up(request.form['username'], request.form['name'], request.form['password'], request.form['age'], request.form['email'])
			cur_user = request.form['username']
			last_user = cur_user
			return redirect(url_for('home', username = request.form['username']))
	return render_template('index.html', error=error)


@app.route('/home/<username>', methods=['GET', 'POST'])
def home(username):
	# return 'User %s' % username
	# Put Different Tabs for the different features
	print("Requesting Feed")
	feed_content = get_feed1(username, cur_user)

	if request.method == 'POST':
		if request.form['button']=="Search User":
			if True:
				print(request.form["users"])
				# Replace here with something else
				# Where to display the user?
				# search_for_user
				# last_user = request.form["users"]
				return redirect(url_for('profile', username = request.form["users"], type = 0))
		elif request.form['button']=="Show Bookmarks":
			if True:
				return redirect(url_for('bookmark', username = cur_user))

		elif request.form['button']=="Bookmark":
			if True:
				post_bookmark = request.form['button11']
				bm.bookmark(cur_user, post_bookmark)
				# sleep(2)
				# feed_content = get_feed1(username, cur_user)
				# print(feed_content)
				# all_tags = get_all_tags()
				# all_user = get_all_user()
				# all_comm = get_all_comm()
				return redirect(url_for('home', username = username))
				
		elif request.form['button']=="Upvote":
			if True:
				post_upvote = request.form['button22']
				upvote(post_upvote, cur_user)
				# feed_content = get_feed1(username, cur_user)
				# print("Printing after upvote")
				# print(feed_content)
				# all_tags = get_all_tags()
				# all_user = get_all_user()
				# all_comm = get_all_comm()
				user1 = username
				return redirect(url_for('home', username = username))
				# return render_template('feed.html', username = cur_user,  all_feeds = feed_content, all_tags = all_tags, all_user = all_user, all_comm = all_comm)
				
		elif request.form['button']=="PreRequisite":
			if True:
				post_prereq = request.form["button33"]
				feed_content = get_prerequisites(cur_user, post_prereq )
				all_tags = get_all_tags()
				all_user = get_all_user()
				all_comm = get_all_comm()
				return render_template('feed.html', username = cur_user,  all_feeds = feed_content, all_tags = all_tags, all_user = all_user, all_comm = all_comm)
				
		elif request.form['button']=="Search Community":
			if True:
				print(request.form["comm"])
				# Replace here with something else
				# Where to display the user?
				# search_for_user
				# last_user = request.form["comm"]
				return redirect(url_for('profile', username = request.form["comm"], type = 0))
		elif request.form['button']=="My Profile":
			return redirect(url_for('profile', username = cur_user, type = 0))
		elif request.form['button']=="Search Tag":
			# tags = request.form['categories[]']
			# print(tags)
			# print("Hello")
			tags = request.form["tags"]
			feed_content = search_tags(tags, cur_user)
			all_tags = get_all_tags()
			all_user = get_all_user()
			all_comm = get_all_comm()
			return render_template('feed.html', username = cur_user,  all_feeds = feed_content, all_tags = all_tags, all_user = all_user, all_comm = all_comm)
			
			# return "Tags are : %s" %request.form['tags']
		else:
			# .... insert a function to bookmark here
			feed_id = request.form['button']
			print(feed_id)
			all_tags = get_all_tags()
			all_user = get_all_user()
			all_comm = get_all_comm()
			return render_template('feed.html', username = cur_user,  all_feeds = feed_content, all_user = all_user, all_comm = all_comm)

	all_tags = get_all_tags()
	all_user = get_all_user()
	all_comm = get_all_comm()
	return render_template('feed.html', username = cur_user,  all_feeds = feed_content, all_tags =all_tags ,all_user = all_user, all_comm = all_comm)

@app.route('/profile/<username>/<int:type>', methods = ['GET', 'POST'])
def profile(username, type):

	if username==cur_user:
		display_follow = False
	else:
		display_follow = True

	print("username : ", username)
	is_following = check_follow(cur_user, username)
	# type = 1 represents bookmarked posts
	if type==1:
		feed_content = bm.get_bookmarked(username)
	else:
		feed_content = get_feed_user1(username)


	if request.method == 'POST':
		if request.form['button'] == 'unfollow':
			# .... insert a function to unfollow a user
			unfollow(cur_user, username)
			is_following = False
			return render_template('profile.html', all_feeds = feed_content, follow_status = is_following, display_follow = display_follow, username = username)
		elif request.form['button'] == 'follow':
			follow(cur_user, username)
			# .... insert a function to follow a user
			is_following = True
			return render_template('profile.html', all_feeds = feed_content, follow_status = is_following, display_follow = display_follow, username = username)
		elif request.form['button']=="Bookmark":
			if True:
				post_bookmark = request.form['button11']
				bookmark(cur_user, post_bookmark)
				# sleep(2)
				# feed_content = get_feed1(username, cur_user)
				# print(feed_content)
				# all_tags = get_all_tags()
				# all_user = get_all_user()
				# all_comm = get_all_comm()
				return redirect(url_for('profile', username = username, type = 0))
				
		elif request.form['button']=="Upvote":
			if True:
				post_upvote = request.form['button22']
				upvote(post_upvote, cur_user)
				# feed_content = get_feed1(username, cur_user)
				# print("Printing after upvote")
				# print(feed_content)
				# all_tags = get_all_tags()
				# all_user = get_all_user()
				# all_comm = get_all_comm()
				# user1 = username
				return redirect(url_for('profile', username = username, type = 0))
				# return render_template('feed.html', username = cur_user,  all_feeds = feed_content, all_tags = all_tags, all_user = all_user, all_comm = all_comm)
				
		elif request.form['button']=="PreRequisite":
			if True:
				post_prereq = request.form["button33"]
				feed_content = get_prerequisites(cur_user, post_prereq )
				all_tags = get_all_tags()
				all_user = get_all_user()
				all_comm = get_all_comm()
				return render_template('profile.html', username = cur_user,  all_feeds = feed_content, all_tags = all_tags, all_user = all_user, all_comm = all_comm)
				# return redirect(url_for('profile', username = username, type = 0))
	else:
		return render_template('profile.html', all_feeds = feed_content, follow_status = is_following, display_follow = display_follow, username = username)



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
		# preq = preq.replace(" ", "")
		# preq = preq.split(',')
		comm = request.form['comm']
		# assign username here
		username = cur_user
		new_post = stories.user_post(username, content, 5, tags, comm)
		create_prerequisite(new_post, preq)
		# post_to_database()
		return redirect(url_for('home', username = cur_user ))
	return render_template("post.html")

@app.route('/bookmark/<username>/', methods = ['GET', 'POST'])
def bookmark(username):
	# .... a function here
	# bookmark_feeds = get_bookmarked(username)
	print(username)
	return redirect(url_for('profile', username = cur_user, type = 1))

# @app.route('/upvote/<upvote_id>', methods = ['GET', 'POST'])
# def upvote(upvote_id):
# 	# .... a function here
# 	print("upvoted, ", upvote_id)
# 	# return "Hello"
# 	return redirect(url_for('home', username = cur_user ))

def get_feed1(username, cur_user):
	database_active = True
	if database_active == True:
		feed_content = feed.get_feed(cur_user)
		print("feed len", len(feed_content))
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
		feed_content = stories.search_username(username, cur_user)
		if len(feed_content)==0:
			print("user :", username)
			feed_content = community_posts(username, cur_user)
			print("feed : ", feed_content)
	else:
		temp = {}
		temp['username'] = 'random_user1'
		temp['date'] = '20/03/2019'
		temp['tags'] = ['ab', 'cd']
		temp['content'] = ['Hello Friends, hahaha']
		temp['id'] = 1
		feed_content = [temp]
	return feed_content
