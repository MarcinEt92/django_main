# Generated by Django 4.2.9 on 2024-01-26 09:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("backEnd", "0005_alter_item_text"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="item",
            unique_together={("list", "text")},
        ),
    ]
