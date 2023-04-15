# Generated by Django 3.2 on 2023-04-15 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20210709_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderAnon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=15)),
                ('quan', models.IntegerField()),
                ('phone_number', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=30)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
    ]
