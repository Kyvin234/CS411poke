# Generated by Django 3.1.1 on 2020-10-20 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokewiki', '0003_auto_20201020_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f_table',
            name='atk',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='f_table',
            name='df',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='f_table',
            name='hp',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='f_table',
            name='spatk',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='f_table',
            name='spd',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='f_table',
            name='spdf',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
