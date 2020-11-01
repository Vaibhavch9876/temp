# Generated by Django 3.1.2 on 2020-10-31 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('p_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('p_statement', models.CharField(max_length=1000)),
                ('p_tags', models.CharField(max_length=1000)),
                ('p_rating', models.IntegerField()),
                ('p_A', models.CharField(max_length=100)),
                ('p_B', models.CharField(max_length=100)),
                ('p_C', models.CharField(max_length=100)),
                ('p_D', models.CharField(max_length=100)),
                ('p_E', models.CharField(max_length=100)),
                ('p_correct', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
    ]
