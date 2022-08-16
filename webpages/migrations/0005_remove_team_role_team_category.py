# Generated by Django 4.0.6 on 2022-07-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_team_youtube_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='role',
        ),
        migrations.AddField(
            model_name='team',
            name='category',
            field=models.CharField(blank=True, choices=[('comedy', 'Comedy'), ('music', 'Music'), ('news', 'News'), ('education', 'Education'), ('business', 'Business'), ('movies', 'Movies')], max_length=255, null=True),
        ),
    ]
