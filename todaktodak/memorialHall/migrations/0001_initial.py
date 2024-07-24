# Generated by Django 5.0.7 on 2024-07-24 09:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="MemorialHall",
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
                ("name", models.CharField(max_length=100, verbose_name="추모관 이름")),
                ("date", models.DateTimeField(verbose_name="추모일")),
                ("info", models.CharField(max_length=50, verbose_name="소개글")),
                ("public", models.BooleanField(default=True, verbose_name="공개")),
                ("private", models.BooleanField(default=False, verbose_name="비공개")),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="thumbnail",
                        verbose_name="대표사진",
                    ),
                ),
                (
                    "participation",
                    models.ManyToManyField(
                        related_name="participation_halls", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
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
                ("content", models.TextField(default="", verbose_name="추모글")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성일"),
                ),
                (
                    "commemorate",
                    models.ManyToManyField(
                        related_name="com_msg", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "hall",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="memorialHall.memorialhall",
                    ),
                ),
                (
                    "nickname",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sad",
                    models.ManyToManyField(
                        related_name="sad_msg", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "sympathize",
                    models.ManyToManyField(
                        related_name="sym_msg", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "todak",
                    models.ManyToManyField(
                        related_name="todak_message", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "together",
                    models.ManyToManyField(
                        related_name="together_msg", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Wreath",
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
                    "donation",
                    models.IntegerField(default=1000, verbose_name="헌화금액"),
                ),
                (
                    "comment",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="헌화 한마디"
                    ),
                ),
                ("name", models.CharField(max_length=10, verbose_name="성함")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성일"),
                ),
                (
                    "hall",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="memorialHall.memorialhall",
                    ),
                ),
                (
                    "nickname",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
