# Generated by Django 4.1.4 on 2023-01-09 17:01

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="App",
            fields=[
                ("Appid", models.IntegerField(primary_key=True, serialize=False)),
                ("Appname", models.CharField(max_length=20)),
                ("url", models.CharField(default="None", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Behavior",
            fields=[
                (
                    "behid",
                    models.IntegerField(default=0, primary_key=True, serialize=False),
                ),
                ("beh", models.CharField(max_length=100)),
                ("cost", models.IntegerField(default=0)),
                ("pic", models.FileField(upload_to="")),
                ("time", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Exchange",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("memid", models.CharField(max_length=43)),
                ("edate", models.DateField(auto_now=True)),
                ("npoint", models.IntegerField(default=0)),
                ("elist", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="History",
            fields=[
                (
                    "ordid",
                    models.AutoField(default=0, primary_key=True, serialize=False),
                ),
                ("memid", models.CharField(max_length=43)),
                ("cdate", models.DateField()),
                ("gpoint", models.IntegerField(default=0)),
                ("c_amount", models.IntegerField(default=0)),
                ("amount", models.IntegerField(default=0)),
                ("appname", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="LOGIN",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "FKcheck",
                    models.CharField(default=myapp.models.UUIDrand, max_length=36),
                ),
                ("Rstate", models.CharField(max_length=42)),
                ("RuserID", models.CharField(max_length=43)),
                ("Raccess_code", models.CharField(max_length=43)),
            ],
        ),
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "memid",
                    models.CharField(max_length=43, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=10)),
                ("point", models.IntegerField(default=0)),
                ("pic", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("memid", models.CharField(max_length=43)),
                ("rdate", models.DateField(auto_now=True)),
                ("disc", models.CharField(max_length=1000)),
            ],
        ),
    ]
