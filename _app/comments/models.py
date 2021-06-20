from django.db import models
from django.conf import settings
from posts.models import Post

class Comment(models.Model):
	post = models.ForeignKey(Post,
		on_delete=models.CASCADE)
	content = models.CharField(max_length=1000) 
	author = models.ForeignKey(settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE)

	def __str__(self):
		return (str(self.id) + " By "+ self.author.username 
			+ " on post"+ str(self.post_id) +") " + self.content) 
