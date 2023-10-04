# Generated by Django 4.2.5 on 2023-10-04 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PeripheralSaved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peripheral_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'peripheral_saved',
            },
        ),
    ]
