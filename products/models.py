from django.db import models


class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.FloatField()
	stock = models.IntegerField()
	image_url = models.CharField(max_length=2083)
 



class Offer(models.Model):
	code = models.CharField(max_length=10)
	description = models.CharField(max_length=255)
	discount = models.FloatField()

	
class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
