# Generated by Django 2.0.5 on 2018-06-22 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('votes', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.CharField(max_length=1000)),
                ('votes', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redditapp.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('karma', models.IntegerField(default=0)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subreddit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('moderators', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moderates', to='redditapp.Profile')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='subreddits', to='redditapp.Profile')),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redditapp.Post')),
                ('subscribers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='redditapp.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='redditapp.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='redditapp.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='redditapp.Comment'),
        ),
    ]
