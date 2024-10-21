from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0005_alter_habits_prize"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habits",
            name="prize",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Вознаграждение"
            ),
        ),
    ]
