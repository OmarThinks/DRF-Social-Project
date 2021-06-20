from django.db import models
from django.conf import settings

class Post(models.Model):
	content = models.CharField(max_length=1000) 
	author = models.ForeignKey(settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE)

	def __str__(self):
		return (str(self.id) + " By "+ self.author.username 
			+ ") " + self.content) 
