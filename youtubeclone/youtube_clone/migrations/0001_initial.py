# Generated by Django 3.2.9 on 2021-11-23 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=50)),
                ('like', models.IntegerField(max_length=50)),
                ('dislike', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.CharField(max_length=50)),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='youtube_clone.comment')),
            ],
        ),
    ]
