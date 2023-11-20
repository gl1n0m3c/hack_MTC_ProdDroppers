# Generated by Django 4.2.7 on 2023-11-20 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users_music", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Rooms",
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
                    "name",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="название"
                    ),
                ),
                (
                    "current",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rooms",
                        to="users_music.music",
                        verbose_name="музыка",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rooms",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="админ",
                    ),
                ),
            ],
            options={
                "verbose_name": "комната",
                "verbose_name_plural": "комнаты",
            },
        ),
        migrations.CreateModel(
            name="Messages",
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
                ("message", models.TextField(verbose_name="сообщение")),
                ("date", models.DateTimeField(auto_now=True, verbose_name="дата")),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="комнаты",
                        to="rooms.rooms",
                        verbose_name="комната",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="сообщение",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "сообщение",
                "verbose_name_plural": "сообщения",
            },
        ),
    ]
