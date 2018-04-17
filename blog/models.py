from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @property
    def likes(self):
        return self.like_set.all().count()

    def liked(self, user_id):
        '''Check to see if the current user has already liked the post'''
        return any(l.author.id == user_id for l in self.like_set.all())

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment = models.TextField()
    posted_date = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.comment


class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    liked_date = models.DateTimeField(
        default=timezone.now
    )
