# Generated by Django 5.1.4 on 2024-12-15 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='React',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DomainName', models.CharField(max_length=35)),
                ('IPAddress', models.CharField(max_length=35)),
                ('Class', models.CharField(max_length=2)),
            ],
        ),
    ]
