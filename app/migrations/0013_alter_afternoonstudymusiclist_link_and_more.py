# Generated by Django 4.2.1 on 2023-05-24 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_morningmusicname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afternoonstudymusiclist',
            name='link',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='eveningsleepmusiclist',
            name='link',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='morningmusiclist',
            name='link',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='morningmusicname',
            name='names',
            field=models.TextField(default=''),
        ),
    ]
