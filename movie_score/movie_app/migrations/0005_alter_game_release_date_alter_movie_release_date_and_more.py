# Generated by Django 4.1.7 on 2023-04-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_gamegenre_gamescore_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='series',
            name='release_date',
            field=models.IntegerField(),
        ),
    ]
