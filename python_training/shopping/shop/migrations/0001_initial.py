# Generated by Django 3.2.6 on 2021-08-19 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('emailid', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('phono', models.BigIntegerField()),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('confirm_password', models.CharField(max_length=50)),
            ],
        ),
    ]
