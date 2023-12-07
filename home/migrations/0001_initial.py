# Generated by Django 4.2.4 on 2023-12-07 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=12)),
                ('food_type', models.TextField()),
                ('quantity', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
