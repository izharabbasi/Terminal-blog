from post import Post
from database import Database

Database.inserting()

# post = Post(blog_id='123',title='hello worl', content='this is a new blog that i have been writing for months', author='izhar')

# post.save_to_mongo()

posts = Post.from_mongo('b085efcf2c9340c09f98d936bde6da85')
print(posts)