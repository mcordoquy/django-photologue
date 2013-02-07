# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GalleryUploadTranslation'
        db.create_table('photologue_galleryupload_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['photologue.GalleryUpload'])),
        ))
        db.send_create_signal('photologue', ['GalleryUploadTranslation'])

        # Adding unique constraint on 'GalleryUploadTranslation', fields ['language_code', 'master']
        db.create_unique('photologue_galleryupload_translation', ['language_code', 'master_id'])

        # Adding model 'PhotoTranslation'
        db.create_table('photologue_photo_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('title_slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['photologue.Photo'])),
        ))
        db.send_create_signal('photologue', ['PhotoTranslation'])

        # Adding unique constraint on 'PhotoTranslation', fields ['language_code', 'master']
        db.create_unique('photologue_photo_translation', ['language_code', 'master_id'])

        # Adding model 'GalleryTranslation'
        db.create_table('photologue_gallery_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title_slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['photologue.Gallery'])),
        ))
        db.send_create_signal('photologue', ['GalleryTranslation'])

        # Adding unique constraint on 'GalleryTranslation', fields ['language_code', 'master']
        db.create_unique('photologue_gallery_translation', ['language_code', 'master_id'])

        # Deleting field 'Photo.date_taken'
        db.delete_column('photologue_photo', 'date_taken')

        # Deleting field 'Photo.image'
        db.delete_column('photologue_photo', 'image')

        # Deleting field 'Photo.crop_from'
        db.delete_column('photologue_photo', 'crop_from')

        # Deleting field 'Photo.effect'
        db.delete_column('photologue_photo', 'effect_id')

        # Deleting field 'Photo.view_count'
        db.delete_column('photologue_photo', 'view_count')

        # Deleting field 'Photo.title_slug'
        db.delete_column('photologue_photo', 'title_slug')

        # Deleting field 'Photo.title'
        db.delete_column('photologue_photo', 'title')

        # Deleting field 'Photo.caption'
        db.delete_column('photologue_photo', 'caption')

        # Deleting field 'GalleryUpload.caption'
        db.delete_column('photologue_galleryupload', 'caption')

        # Deleting field 'GalleryUpload.description'
        db.delete_column('photologue_galleryupload', 'description')

        # Deleting field 'GalleryUpload.tags'
        db.delete_column('photologue_galleryupload', 'tags')

        # Deleting field 'GalleryUpload.title'
        db.delete_column('photologue_galleryupload', 'title')

        # Deleting field 'Gallery.description'
        db.delete_column('photologue_gallery', 'description')

        # Deleting field 'Gallery.title_slug'
        db.delete_column('photologue_gallery', 'title_slug')

        # Deleting field 'Gallery.title'
        db.delete_column('photologue_gallery', 'title')


    def backwards(self, orm):
        # Removing unique constraint on 'GalleryTranslation', fields ['language_code', 'master']
        db.delete_unique('photologue_gallery_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'PhotoTranslation', fields ['language_code', 'master']
        db.delete_unique('photologue_photo_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'GalleryUploadTranslation', fields ['language_code', 'master']
        db.delete_unique('photologue_galleryupload_translation', ['language_code', 'master_id'])

        # Deleting model 'GalleryUploadTranslation'
        db.delete_table('photologue_galleryupload_translation')

        # Deleting model 'PhotoTranslation'
        db.delete_table('photologue_photo_translation')

        # Deleting model 'GalleryTranslation'
        db.delete_table('photologue_gallery_translation')

        # Adding field 'Photo.date_taken'
        db.add_column('photologue_photo', 'date_taken',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Photo.image'
        raise RuntimeError("Cannot reverse this migration. 'Photo.image' and its values cannot be restored.")
        # Adding field 'Photo.crop_from'
        db.add_column('photologue_photo', 'crop_from',
                      self.gf('django.db.models.fields.CharField')(default='center', max_length=10, blank=True),
                      keep_default=False)

        # Adding field 'Photo.effect'
        db.add_column('photologue_photo', 'effect',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='photo_related', null=True, to=orm['photologue.PhotoEffect'], blank=True),
                      keep_default=False)

        # Adding field 'Photo.view_count'
        db.add_column('photologue_photo', 'view_count',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Photo.title_slug'
        raise RuntimeError("Cannot reverse this migration. 'Photo.title_slug' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Photo.title'
        raise RuntimeError("Cannot reverse this migration. 'Photo.title' and its values cannot be restored.")
        # Adding field 'Photo.caption'
        db.add_column('photologue_photo', 'caption',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'GalleryUpload.caption'
        db.add_column('photologue_galleryupload', 'caption',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'GalleryUpload.description'
        db.add_column('photologue_galleryupload', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'GalleryUpload.tags'
        db.add_column('photologue_galleryupload', 'tags',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'GalleryUpload.title'
        raise RuntimeError("Cannot reverse this migration. 'GalleryUpload.title' and its values cannot be restored.")
        # Adding field 'Gallery.description'
        db.add_column('photologue_gallery', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Gallery.title_slug'
        raise RuntimeError("Cannot reverse this migration. 'Gallery.title_slug' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Gallery.title'
        raise RuntimeError("Cannot reverse this migration. 'Gallery.title' and its values cannot be restored.")

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'photologue.gallery': {
            'Meta': {'ordering': "['order']", 'object_name': 'Gallery'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'galleries'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['photologue.Photo']"}),
            'viewers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'view_albums'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"})
        },
        'photologue.gallerytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'GalleryTranslation', 'db_table': "'photologue_gallery_translation'"},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['photologue.Gallery']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'photologue.galleryupload': {
            'Meta': {'object_name': 'GalleryUpload'},
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photologue.Gallery']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'zip_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'photologue.galleryuploadtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'GalleryUploadTranslation', 'db_table': "'photologue_galleryupload_translation'"},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['photologue.GalleryUpload']"}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        'photologue.imageoverride': {
            'Meta': {'object_name': 'ImageOverride'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'imageoverride_related'", 'null': 'True', 'to': "orm['photologue.PhotoEffect']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'photosize': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photologue.PhotoSize']"}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'photologue.photo': {
            'Meta': {'ordering': "['order']", 'object_name': 'Photo'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'})
        },
        'photologue.photoeffect': {
            'Meta': {'object_name': 'PhotoEffect'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.6'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'photologue.photosize': {
            'Meta': {'ordering': "['width', 'height']", 'object_name': 'PhotoSize'},
            'crop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_sizes'", 'null': 'True', 'to': "orm['photologue.PhotoEffect']"}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'increment_count': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'pre_cache': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quality': ('django.db.models.fields.PositiveIntegerField', [], {'default': '70'}),
            'upscale': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'watermark': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_sizes'", 'null': 'True', 'to': "orm['photologue.Watermark']"}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'photologue.phototranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'PhotoTranslation', 'db_table': "'photologue_photo_translation'"},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['photologue.Photo']"}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'photologue.watermark': {
            'Meta': {'object_name': 'Watermark'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'opacity': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'style': ('django.db.models.fields.CharField', [], {'default': "'scale'", 'max_length': '5'})
        },
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_items'", 'to': "orm['taggit.Tag']"})
        }
    }

    complete_apps = ['photologue']