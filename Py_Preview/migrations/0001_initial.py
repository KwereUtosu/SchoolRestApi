# Generated by Django 2.2.1 on 2019-06-06 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
