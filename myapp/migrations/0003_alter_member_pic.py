# Generated by Django 4.1.4 on 2023-01-10 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_alter_member_point"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="pic",
            field=models.CharField(max_length=1000),
        ),
    ]
