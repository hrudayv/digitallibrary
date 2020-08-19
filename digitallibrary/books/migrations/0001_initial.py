# Generated by Django 3.0.3 on 2020-07-12 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=100)),
                ('authorname', models.CharField(max_length=200)),
                ('booknum', models.IntegerField()),
                ('stockavail', models.IntegerField()),
            ],
        ),
    ]