# Generated by Django 4.2.6 on 2024-10-08 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_alter_hudumazawazalishaji_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='watejawote',
            name='TotalAmount',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Kiasi Cha Jumla'),
        ),
    ]