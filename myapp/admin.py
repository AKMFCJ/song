from django.contrib import admin
from myapp.models import Article, FlatPage, Person


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
    fieldsets = (
        (None, {
            'fields': ('url', 'title', 'content', 'sites')
        }),
        ('Advanced options',{
            'classes': ('collapse',),
            'fields': ('enable_comments', 'registration_required', 'template_name')
        }),
    )

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('upper_case_name', 'name', 'decade_born_in', 'colored_name','born_in_fifities', )

    def upper_case_name(self, obj):
        return ("%s %s" % (obj.first_name, obj.last_name)).upper()
    upper_case_name.short_description = 'Name'