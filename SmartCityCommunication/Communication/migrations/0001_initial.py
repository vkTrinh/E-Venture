# Generated by Django 3.0.3 on 2020-02-21 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wann', models.DateTimeField(auto_now_add=True)),
                ('von', models.EmailField(max_length=254)),
                ('grund', models.CharField(max_length=95)),
                ('nachricht', models.TextField()),
            ],
        ),
    ]
