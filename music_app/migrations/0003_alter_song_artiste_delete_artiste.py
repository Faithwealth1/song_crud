# Generated by Django 4.1.3 on 2022-11-04 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music_app", "0002_alter_artiste_id_alter_lyrics_id_alter_song_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="artiste",
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name="Artiste",
        ),
    ]
