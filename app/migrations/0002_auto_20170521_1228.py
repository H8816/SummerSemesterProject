# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-21 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Postings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_data', models.CharField(max_length=500)),
                ('imagelink', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagelink', models.CharField(max_length=50)),
                ('topic', models.CharField(max_length=30)),
                ('comment', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField(max_length=50)),
                ('category', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('topics', models.CharField(max_length=100)),
                ('topicsCounter', models.IntegerField()),
                ('posts', models.CharField(max_length=500)),
                ('postsCounter', models.IntegerField()),
                ('ip', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='thread',
            name='start_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='postings',
            name='thread',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.Thread'),
        ),
        migrations.AddField(
            model_name='postings',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]
