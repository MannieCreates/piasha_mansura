# Generated by Django 5.0.2 on 2024-02-25 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0003_alter_login_info_options_alter_login_info_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login_info',
            name='security_answer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='login_info',
            name='security_question',
            field=models.CharField(blank=True, choices=[('q1', 'What is your favorite color?'), ('q2', 'What is the name of your first pet?'), ('q3', 'In which city were you born?')], max_length=255, null=True),
        ),
    ]
