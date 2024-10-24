from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0007_rename_is_good_habits_is_nice"),
    ]

    operations = [
        migrations.AddField(
            model_name="habits",
            name="friday",
            field=models.BooleanField(default=True, verbose_name="Пятница"),
        ),
        migrations.AddField(
            model_name="habits",
            name="monday",
            field=models.BooleanField(default=True, verbose_name="Понедельник"),
        ),
        migrations.AddField(
            model_name="habits",
            name="saturday",
            field=models.BooleanField(default=True, verbose_name="Суббота"),
        ),
        migrations.AddField(
            model_name="habits",
            name="sunday",
            field=models.BooleanField(default=True, verbose_name="Воскресенье"),
        ),
        migrations.AddField(
            model_name="habits",
            name="thursday",
            field=models.BooleanField(default=True, verbose_name="Четверг"),
        ),
        migrations.AddField(
            model_name="habits",
            name="tuesday",
            field=models.BooleanField(default=True, verbose_name="Вторник"),
        ),
        migrations.AddField(
            model_name="habits",
            name="wednesday",
            field=models.BooleanField(default=True, verbose_name="Среда"),
        ),
        migrations.AlterField(
            model_name="habits",
            name="duration",
            field=models.SmallIntegerField(
                verbose_name="Время на выполнение (в минутах) "
            ),
        ),
    ]
