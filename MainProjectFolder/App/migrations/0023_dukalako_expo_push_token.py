# Generated by Django 4.2.6 on 2024-10-30 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_myuser_expo_push_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='dukalako',
            name='expo_push_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]