from django.db import models

# Create your models here.
STATUC_CHOICES = (
	('d', 'Draft'),
	('p', 'Published'),
	('w', 'Withdrawn'),
)


class Article(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	status = models.CharField(max_length=1, choices=STATUC_CHOICES)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return u"%s" % self.title

	