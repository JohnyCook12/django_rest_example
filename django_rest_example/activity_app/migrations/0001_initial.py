# Generated by Django 4.1.3 on 2022-11-07 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=200)),
                ('when', models.DateTimeField(verbose_name='when happened')),
            ],
        ),
    ]