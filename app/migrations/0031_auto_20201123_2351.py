# Generated by Django 3.0.8 on 2020-11-23 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20201123_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='doc',
            field=models.FileField(blank=True, null=True, upload_to='posts/doc/'),
        ),
    ]
