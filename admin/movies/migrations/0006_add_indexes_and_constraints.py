# Generated by Django 3.2 on 2022-04-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_rename_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filmwork',
            options={'verbose_name': 'film_work', 'verbose_name_plural': 'film_work_plural'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'person', 'verbose_name_plural': 'person_plural'},
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='role',
            field=models.TextField(choices=[('movie', 'Фильм'), ('tv_show', 'ТВ-шоу')], max_length=255, null=True, verbose_name='role'),
        ),
        migrations.AddIndex(
            model_name='filmwork',
            index=models.Index(fields=['creation_date', 'rating'], name='film_work_creatio_3335ac_idx'),
        ),
    ]
