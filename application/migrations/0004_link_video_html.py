# Generated by Django 2.0.7 on 2018-07-26 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20180726_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='video_html',
            field=models.CharField(default='<iframe width="400" height="225" src="https://www.youtube.com/embed/9g2U12SsRns?feature=oembed&autoplay=1&iv_load_policy=3" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>', max_length=255, verbose_name='video HTML'),
            preserve_default=False,
        ),
    ]