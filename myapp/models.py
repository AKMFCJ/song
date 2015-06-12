from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html

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
    url = models.CharField(_('URL'), max_length=100, db_index=True)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)
    enable_comments = models.BooleanField(_('enable comments'), default=False)
    template_name = models.CharField(_('template name'), max_length=70, blank=True,
        help_text=_("Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'."))
    registration_required = models.BooleanField(_('registration required'),
        help_text=_("If this is checked, only logged-in users will be able to view the page."),
        default=True)
    sites = models.ManyToManyField(Site)

    class Meta:
        db_table = 'django_flatpage'
        verbose_name = _('flat page')
        verbose_name_plural = _('flat pages')
        ordering = ('url',)

    def __str__(self):
        return "%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        # Handle script prefix manually because we bypass reverse()
        return iri_to_uri(get_script_prefix().rstrip('/') + self.url)


class Person(models.Model):

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	birthday = models.DateField()
	age = models.IntegerField()
	color_code = models.CharField(max_length=6)

	def decade_born_in(self):
		return self.birthday.strftime('%Y')[:3] + "0's"

	decade_born_in.short_description = 'Birth decade'

	def colored_name(self):
		return format_html('<span style="color: #{};">{}{}</span>', self.color_code, self.first_name, self.last_name)

	colored_name.allow_tags = True

	def born_in_fifities(self):
		return self.birthday.strftime('%Y')[:3] == '195'
	born_in_fifities.boolean = True


	def __str__(self):
		return self.first_name

