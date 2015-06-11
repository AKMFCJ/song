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
	pub_date = models.DateField()
	status = models.CharField(max_length=1, choices=STATUC_CHOICES)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return u"%s" % self.title

	

class FlatPage(models.Model):
	url = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	content = models.TextField()

	def __str__(self):
		return self.title

	def __unicode__(self):
		return u"%s" % self.title