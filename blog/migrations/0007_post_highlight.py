# Generated by Django 2.1.7 on 2019-05-12 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190508_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='highlight',
            field=models.BooleanField(default=False),
        ),
    ]