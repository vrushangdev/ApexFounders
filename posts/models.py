from django.db import models


# Create your models here.
class Post( models.Model ):
    title = models.CharField( max_length=100 )
    content = models.TextField()
    thumbnail = models.TextField()
    publish_date = models.DateTimeField( auto_now_add=True )

    def __str__(self):
        return self.title


class Comment( models.Model ):
    post = models.ForeignKey( Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField( auto_now_add=True )
    content = models.TextField()

    def __str__(self):
        return self.user.username


class PostView( models.Model ):
    post = models.ForeignKey( Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField( auto_now_add=True )

    def __str__(self):
        return self.user.username
