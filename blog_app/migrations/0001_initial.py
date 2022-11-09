# Generated by Django 4.1.3 on 2022-11-09 16:54

import blog_app.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, help_text='First name', max_length=50, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, help_text='Last name', max_length=50, null=True, verbose_name='Last name')),
                ('nickname', models.CharField(max_length=100, unique=True)),
                ('acc_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('bio', models.TextField(blank=True)),
                ('avatar', models.ImageField(upload_to='cover_images/<function user_directory_path at 0x7fa941663760>')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('post_text', models.TextField(blank=True, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.blogauthor')),
            ],
        ),
        migrations.CreateModel(
            name='PostImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=blog_app.models.get_image_filename, verbose_name='Image')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog_app.blogpost')),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=280)),
                ('comment_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.blogauthor')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.blogpost')),
            ],
        ),
    ]