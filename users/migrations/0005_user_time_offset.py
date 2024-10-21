# Generated by Django 5.0.7 on 2024-08-03 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_user_tg_chat_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="time_offset",
            field=models.IntegerField(
                default=3,
                help_text="От -12 до +14, по умолчанию UTC+3 (Московское время)",
                verbose_name="Смещение часового пояса",
            ),
        ),
    ]