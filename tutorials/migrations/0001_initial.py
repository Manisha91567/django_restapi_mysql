# Generated by Django 4.0.5 on 2022-06-16 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_title', models.CharField(default='', max_length=70)),
                ('Book_author', models.CharField(default='', max_length=200)),
                ('Page_numbers', models.CharField(default='', max_length=200)),
                ('Prize', models.CharField(default='', max_length=200)),
                ('Ratings', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
