# Generated by Django 2.1 on 2018-08-01 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogfront', '0002_auto_20180801_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=150),
        ),
    ]
