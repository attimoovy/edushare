# Generated by Django 3.0.8 on 2020-10-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20201030_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='subject',
            field=models.CharField(choices=[('Math', 'Math'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('English', 'English'), ('Biology', 'Biology'), ('Physical Education', 'Physical Education'), ('Business', 'Business'), ('Economics', 'Economics')], default='other', max_length=64),
        ),
        migrations.AlterField(
            model_name='posts',
            name='uni',
            field=models.CharField(choices=[('KFUPM', 'KFUPM'), ('Harvard', 'Harvard'), ('Yale', 'Yale'), ('MIT', 'MIT'), ('Cambridge', 'Cambridge')], default='other', max_length=64),
        ),
    ]
