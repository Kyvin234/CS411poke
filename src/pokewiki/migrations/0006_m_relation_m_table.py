# Generated by Django 3.1.1 on 2020-10-24 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokewiki', '0005_a_relation_is_hidden'),
    ]

    operations = [
        migrations.CreateModel(
            name='m_table',
            fields=[
                ('m_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('m_id', models.IntegerField(default=0)),
                ('pp', models.IntegerField(default=0)),
                ('power', models.IntegerField(default=0, null=True)),
                ('accuaracy', models.IntegerField(default=0)),
                ('priority', models.IntegerField(default=0, null=True)),
                ('types', models.CharField(default='', max_length=10)),
                ('dmg_class', models.CharField(default='', max_length=10)),
                ('effect', models.CharField(default='', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='m_relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learn_method', models.CharField(default='', max_length=10)),
                ('level_learned', models.IntegerField(default=0)),
                ('m_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokewiki.m_table')),
                ('s_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokewiki.s_table')),
            ],
        ),
    ]