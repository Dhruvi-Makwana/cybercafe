# Generated by Django 4.1.5 on 2023-02-14 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_alter_system_name_alter_system_user_histories_system_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="system_user_histories",
            name="finish_time",
            field=models.DateTimeField(blank=True, max_length=20, null=True),
        ),
    ]
