import sys
from django.contrib.auth.models import User
from blog.models import Post
# from .blog.models import Post

# Creating objects and inserting.
user = User.objects.get(username='admin')
post = Post(title='Another post',
                slug='another-post',
                body='Post body.',
                author=user)

post.save()

user = User.objects.get(username='admin')

# Inserting objects to database directly.
Post.objects.create(title='One more post', slug='one-more-post', body='Post body.', author=user)

# Updating objects.
post.title = 'New title'
post.save()

# Retrieving objects.
all_posts = Post.objects.all()

# Using the filter() method.
Post.objects.filter(publish__year=2018)
Post.objects.filter(publish__year=2017, author__username='admin')
Post.objects.filter(publish__year=2017) \
            .filter(author__username='admin')

# Using exclude()
Post.objects.filter(publish__year=2017) \
            .exclude(title__startswith='Why')

# Using order_by()
Post.objects.order_by('title')
Post.objects.order_by('-title')

# Deleting objects
post = Post.objects.get(id=1)
post.delete()
# Note that deleting objects will also delete
# any dependent relationships for ForeignKey objects defined
# with on_delete set to CASCADE.

# Using custom Manager:
Post.published.filter(title__startswith='Who')

# Sending email
from django.core.mail import send_mail
send_mail('Django mail', 'This e-mail was sent with Django.', 'your_account@gmail.com', ['your_account@gmail.com'], fail_silently=False)
