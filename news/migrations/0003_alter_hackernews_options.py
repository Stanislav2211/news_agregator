# Generated by Django 5.0.6 on 2024-07-22 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_bbc_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hackernews',
            options={'verbose_name_plural': 'HackerNews'},
        ),
    ]
