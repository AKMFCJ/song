#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect


def export_selected_objects(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    ct = ContentType.objects.get_for_model(queryset.model)

    return HttpResponseRedirct("/export/?ct=%sids=%s" % (ct.pk, ",".join(selected)))


admin.site.add_action(export_selectd_objects)
