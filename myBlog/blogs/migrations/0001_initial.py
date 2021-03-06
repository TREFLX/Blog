# Generated by Django 3.1 on 2022-05-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(default='Описание')),
                ('keywords', models.CharField(default='Ключевые_слова', max_length=120)),
                ('content', models.TextField()),
                ('visible', models.BooleanField(default=1)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id', '-timestamp'],
            },
        ),
    ]
