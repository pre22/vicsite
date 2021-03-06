# Generated by Django 4.0.3 on 2022-03-28 14:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='msg',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='carousel_about',
            name='heading_one',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='carousel_about',
            name='heading_two',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='carousel_home',
            name='heading_one',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='carousel_home',
            name='heading_two',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='our_offering',
            name='msg',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='our_offering',
            name='title',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='testimonial_body',
            name='comments',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='top_executive',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='who_we_are',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='who_we_are_sub',
            name='msg',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='who_we_are_sub',
            name='title',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
