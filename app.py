from post import Post
from database import Database

Database.inserting()

post = Post(blog_id='123',title='hello worl', content='this is a new blog that i have been writing for months', author='izhar')

post.save_to_mongo()
