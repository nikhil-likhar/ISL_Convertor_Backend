# Generated by Django 3.1.3 on 2021-09-01 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deafApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('data', models.FileField(upload_to='Word/')),
            ],
        ),
    ]