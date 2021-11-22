# Generated by Django 3.2.9 on 2021-11-22 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=50)),
                ('like', models.CharField(max_length=50)),
                ('dislike', models.CharField(max_length=50)),
            ],
        ),
    ]
