# Generated by Django 4.0.2 on 2022-03-21 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0012_alter_tickits_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='faang',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='info',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='login',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='otp',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tickits',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]