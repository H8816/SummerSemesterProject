from django.db import models
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    topics = models.CharField(max_length=100)
    topicsCounter = models.IntegerField()
    posts = models.CharField(max_length=500)
    postsCounter = models.IntegerField()

    #For further purposes
    ip = models.CharField(max_length=15)

    def __str__(self):
        return self.username

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class Thread(models.Model):
    start_user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagelink = models.CharField(max_length=200)
    topic = models.CharField(max_length=30)
    comment = models.CharField(max_length=500)
    datetime = models.DateTimeField(max_length=50)
    category = models.ForeignKey(Category, default="0")

    def __str__(self):
        return self.topic

class Postings(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    post_data = models.CharField(max_length=500)
    imagelink = models.CharField(max_length=50)



    def __str__(self):
        return self.post_data
