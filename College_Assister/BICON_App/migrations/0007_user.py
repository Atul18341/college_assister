# Generated by Django 3.2 on 2021-09-01 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BICON_App', '0006_data_contributors'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
