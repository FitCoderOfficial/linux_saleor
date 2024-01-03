# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 12:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("product", "0035_auto_20170919_0846")]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "permissions": (
                    ("view_product", "Can view products"),
                    ("edit_product", "Can edit products"),
                    ("view_properties", "Can view product properties"),
                    ("edit_properties", "Can edit product properties"),
                ),
                "verbose_name": "product",
                "verbose_name_plural": "products",
            },
        )
    ]
