# Generated by Django 4.1.4 on 2023-01-26 03:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appblog', '0002_alter_blog_cuerpo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
