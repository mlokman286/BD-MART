# Generated by Django 4.2.6 on 2023-10-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menproduct',
            name='img',
            field=models.ImageField(null=True, upload_to='men'),
        ),
        migrations.AlterField(
            model_name='menproduct',
            name='price',
            field=models.IntegerField(),
        ),
    ]
