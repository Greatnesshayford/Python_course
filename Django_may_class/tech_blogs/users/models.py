from django.db import models

# Create your models here.
class Category (models.Model):
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category


# account model - keeping all the users account
class Account (models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    join_at = models.DateTimeField(auto_now_add= True)
    category = models.ManyToManyField(Category, related_name="account")    

    def __str__(self):
        return self.name
    

# article model - for all the post
class Post (models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="post")
    title = models.CharField(max_length=100)
    content = models.TextField()
    likes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add= True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="post_category")

    def __str__(self):
        return self.title
    

# comments model - for other comment
class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
    post_comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add= True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="comment_author")

    def __str__(self):
        return self.post_comment
    