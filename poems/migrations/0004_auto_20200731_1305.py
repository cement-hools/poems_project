# Generated by Django 2.2.14 on 2020-07-31 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0003_auto_20200731_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poet',
            name='photo_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на фото'),
        ),
    ]
