# Generated by Django 4.2.6 on 2023-10-29 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_app', '0010_alter_product_catagory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catagories',
            old_name='productCatagories',
            new_name='name',
        ),
    ]
