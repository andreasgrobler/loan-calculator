# Generated by Django 2.2.7 on 2019-11-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InModel',
            fields=[
                ('loan_number', models.IntegerField(primary_key=True, serialize=False)),
                ('name_of_loan', models.TextField(max_length=150)),
                ('price', models.FloatField()),
                ('deposit', models.FloatField()),
                ('term', models.FloatField()),
                ('interest_rate', models.FloatField()),
                ('principal', models.FloatField()),
                ('payment', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='OutModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_number', models.IntegerField()),
                ('period', models.IntegerField()),
                ('begin_value', models.FloatField()),
                ('payment_period', models.FloatField()),
                ('interest_period', models.FloatField()),
                ('principal_period', models.FloatField()),
                ('end_value', models.FloatField()),
            ],
        ),
    ]
