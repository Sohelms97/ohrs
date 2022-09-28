# Generated by Django 3.2.7 on 2022-09-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
