# Generated by Django 4.2.6 on 2024-11-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0023_dukalako_expo_push_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ujumbe unahusiana na ?')),
                ('SentMessage', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Ujumbe')),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'InformUsers',
            },
        ),
    ]