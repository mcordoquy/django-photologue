""" Newforms Admin configuration for Photologue

"""
from django.contrib.admin import ModelAdmin, site
from adminsortable.admin import SortableAdmin
from django import forms
from models import *
from django.db.models import get_model
from uuslug import uuslug


class GalleryAdmin(SortableAdmin):
    list_display = ('title', 'owner', 'date_added', 'photo_count', 'is_public')
    list_filter = ['date_added', 'is_public']
    exclude = ['title_slug']

    date_hierarchy = 'date_added'
    filter_horizontal = ('photos',)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        if not obj.title_slug:
            obj.title_slug = uuslug(obj.title, instance=obj, slug_field='title_slug', filter_dict={'owner': request.user,})
        obj.save()

def crop_from_top(modeladmin, request, queryset):
    queryset.update(crop_from='top')
crop_from_top.short_description = "Crop photos from top"

def crop_from_bottom(modeladmin, request, queryset):
    queryset.update(crop_from='bottom')
crop_from_bottom.short_description = "Crop photos from bottom"

class PhotoAdmin(SortableAdmin):
    list_display = ('id', 'title', 'caption', 'date_taken', 'date_added', 'is_public', 'view_count', 'admin_thumbnail')
    list_editable = ('title', 'caption', 'is_public')
    list_filter = ['date_added', 'is_public', 'tags', 'galleries']
    search_fields = ['title', 'title_slug', 'caption', 'tags']
    prepopulated_fields = {'title_slug': ('title',)}
    actions = [crop_from_top, crop_from_bottom]
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(PhotoAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'caption':
            formfield.widget = forms.Textarea(attrs={'cols': 60, 'rows': 2})
        return formfield

class PhotoEffectAdmin(ModelAdmin):
    list_display = ('name', 'description', 'color', 'brightness', 'contrast', 'sharpness', 'filters', 'admin_sample')
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Adjustments', {
            'fields': ('color', 'brightness', 'contrast', 'sharpness')
        }),
        ('Filters', {
            'fields': ('filters',)
        }),
        ('Reflection', {
            'fields': ('reflection_size', 'reflection_strength', 'background_color')
        }),
        ('Transpose', {
            'fields': ('transpose_method',)
        }),
    )

class PhotoSizeAdmin(ModelAdmin):
    list_display = ('name', 'width', 'height', 'crop', 'pre_cache', 'effect', 'increment_count')
    fieldsets = (
        (None, {
            'fields': ('name', 'width', 'height', 'quality')
        }),
        ('Options', {
            'fields': ('upscale', 'crop', 'pre_cache', 'increment_count')
        }),
        ('Enhancements', {
            'fields': ('effect', 'watermark',)
        }),
    )


class WatermarkAdmin(ModelAdmin):
    list_display = ('name', 'opacity', 'style')


class GalleryUploadAdmin(ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False # To remove the 'Save and continue editing' button

class ImageOverrideInline(generic.GenericTabularInline):
    model = ImageOverride


site.register(Gallery, GalleryAdmin)
site.register(GalleryUpload)
site.register(Photo, PhotoAdmin)
#site.register(PhotoEffect, PhotoEffectAdmin)
site.register(PhotoSize, PhotoSizeAdmin)
#site.register(Watermark, WatermarkAdmin)
