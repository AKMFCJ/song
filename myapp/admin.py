from django.contrib import admin
from django import forms
from django.db import models

from myapp.models import Article, FlatPage, Person
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = ['make_published', 'export_selectd_objects']
    actions_on_top = False
    actions_on_bottom = True
    actions_selection_counter = True

    date_hierarchy = 'pub_date'
    
    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated

        self.message_user(request, "%s successfully maked as published." % message_bit)

    make_published.short_description = "Mark selected stories as published"

admin.site.register(Article, ArticleAdmin)


@admin.register(FlatPage)
class FlatPageAdmin(admin.ModelAdmin):
    fields = (('url', 'title'), 'content', 'article')


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        exclude = ['name']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    #exclude = ['age']
    #form = PersonForm
    formfield_overrides = {
        models.CharField: {'widget': models.TextField}
    }



from kombu.transport.django import models as kombu_models
admin.site.register(kombu_models.Message)





