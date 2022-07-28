import time
import sys, time
import praw

__author__ = 'davide perozzi'
__version__ = '0.1'

"""Upvotes (or downvotes) all comments and submissions by redditor target.
Change commented lines to specify user and upvote/downvote.
python upvote-bot.py target
"""

class RedditBot(object):

	def __init__(self, target):
		self.reddit = praw.Reddit(
			client_id="TQRb6-g0ZvS5ybruCBkl6g",
			client_secret="CfhpdUMsqVzzQmzeRLT_fQB1kD9nFQ",
			user_agent="testscript by u/AdventurousWolf81434",
			password="auj-qvr.VYB6nze3mau",
			username="AdventurousWolf81434"
			)
		self.count = 0
		self.redditor = self.reddit.redditor(target)

	def run(self):
		for comment in self.redditor.comments.new(limit=None):
			try:
				comment.upvote() # Change this to comment.downvote() if you want to downvote instead
				print("Upvoted comment: %s" %comment.id)
				self.count += 1
			except:
				Exception('Cannot upvote!')
			time.sleep(2) # Following reddit's rules

		for submitted in self.redditor.submissions.new(limit=None):
			try:
				submitted.upvote() # Change this to submission.downvote() if you want to downvote instead
				print("Upvoted submission: %s" %submitted.id)
				self.count += 1
			except:
				Exception('Cannot upvote!')
			time.sleep(2) # Following reddit's rules

def main(target):
	bot = RedditBot(target) # Specify username and password
	try:
		bot.run()
	except:
		raise
	finally:
		print('Done!  Upvoted %d submissions/comments!' %bot.count)

	return 0

if __name__ == '__main__':
	target = sys.argv[-1]
	main(target)


