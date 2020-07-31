# Generated by Django 2.2.14 on 2020-07-31 10:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import poem_parser.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('poems', '0004_auto_20200731_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoemsFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=poem_parser.models.parser_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('html',))])),
                ('processed', models.BooleanField(default=False, verbose_name='Обработан?')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('poet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='poems.Poet')),
            ],
            options={
                'ordering': ('uploaded_at',),
            },
        ),
    ]
