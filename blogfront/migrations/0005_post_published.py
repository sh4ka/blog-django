# Generated by Django 2.1 on 2018-08-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogfront', '0004_auto_20180801_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
