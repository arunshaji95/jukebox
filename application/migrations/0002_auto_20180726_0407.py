# Generated by Django 2.0.7 on 2018-07-26 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['votes']},
        ),
    ]