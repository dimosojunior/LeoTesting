# Generated by Django 4.2.6 on 2024-10-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_chatmessage_mypostid'),
    ]

    operations = [
        migrations.AddField(
            model_name='dukalako',
            name='YouTubeLink',
            field=models.URLField(blank=True, max_length=5000, null=True, verbose_name='YouTube Video Link'),
        ),
    ]
