from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0009_alter_habits_friday_alter_habits_monday_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habits",
            name="friday",
            field=models.BooleanField(
                choices=[(True, "Да"), (False, "Нет")],
                default=True,
                verbose_name="Пятница",
            ),
        ),
        migrations.AlterField(
            model_name="habits",
            name="monday",
            field=models.BooleanField(
                choices=[(True, "Да"), (False, "Нет")],
                default=True,
                verbose_name="Понедельник",
            ),
        ),
        migrations.AlterField(
            model_name="habits",
            name="saturday",
            field=models.BooleanField(
                choices=[(True, "Да"), (False, "Нет")],
                default=True,
                verbose_name="Суббота",
            ),
        ),
        migrations.AlterField(
            model_name="habits",
            name="sunday",
            field=models.BooleanField(
                choices=[(True, "Да"), (False, "Нет")],
                default=True,
                verbose_name="Воскресенье",
            ),
        ),
        migrations.AlterField(
            model_name="habits",
            name="thursday",
            field=models.BooleanField(
                choices=[(True, "Да"), (False, "Нет")],
                default=True,
                verbose_name="Четверг",
            ),
        ),
        migrations.AlterField(
            model_name="habits",
            name="tuesday",
            field=models.BooleanField(
                choices=[(True, "Да"), (False, "Нет")],
                default=True,
                verbose_name="Вторник",
            ),
        ),
        migrations.AlterField(
            model_name="habits",
            name="wednesday",
            field=models.BooleanField(
                choices=[(True, "Да"), (False, "Нет")],
                default=True,
                verbose_name="Среда",
            ),
        ),
    ]
