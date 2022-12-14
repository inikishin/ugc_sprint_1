# Generated by Django 3.2 on 2022-04-01 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_test_add_fields'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filmwork',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='filmwork',
            old_name='modified',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='modified',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='genrefilmwork',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='genrefilmwork',
            old_name='film_work',
            new_name='film_work_id',
        ),
        migrations.RenameField(
            model_name='genrefilmwork',
            old_name='genre',
            new_name='genre_id',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='modified',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='personfilmwork',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='personfilmwork',
            old_name='film_work',
            new_name='film_work_id',
        ),
        migrations.RenameField(
            model_name='personfilmwork',
            old_name='person',
            new_name='person_id',
        ),
        migrations.RemoveField(
            model_name='filmwork',
            name='certificate',
        ),
        migrations.RemoveField(
            model_name='filmwork',
            name='file_path',
        ),
    ]
