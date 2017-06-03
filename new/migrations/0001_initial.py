# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-02 18:39
from __future__ import unicode_literals

import annoying.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(default='IIM-A', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(default='Aditya', max_length=120)),
                ('monthly_forcast', models.PositiveIntegerField(default=1000)),
                ('monthly_forcast_update', models.PositiveIntegerField(default=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Forcast',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('forcast', models.PositiveIntegerField(default=60)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('style', models.BooleanField(default=False)),
                ('storage', models.BooleanField(default=False)),
                ('extended_battery', models.BooleanField(default=False)),
                ('durability', models.BooleanField(default=False)),
                ('unit_cost', models.PositiveIntegerField(default=130)),
                ('unit_price', models.PositiveIntegerField(default=200)),
                ('inventory_cost', models.PositiveIntegerField(default=4)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('monthly_order1', models.PositiveIntegerField(default=0, help_text='Max Value is 45', validators=[django.core.validators.MaxValueValidator(45)])),
                ('monthly_order2', models.PositiveIntegerField(default=0, help_text='Max Value is 45', validators=[django.core.validators.MaxValueValidator(45)])),
                ('monthly_order3', models.PositiveIntegerField(default=0, help_text='Max Value is 25', validators=[django.core.validators.MaxValueValidator(25)])),
                ('monthly_order4', models.PositiveIntegerField(default=0, help_text='Max Value is 25', validators=[django.core.validators.MaxValueValidator(25)])),
                ('start_month1', models.CharField(choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], default='Jan', max_length=3)),
                ('start_month2', models.CharField(choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], default='Jan', max_length=3)),
                ('start_month3', models.CharField(choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], default='Jan', max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='demand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='college',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='college', to=settings.AUTH_USER_MODEL),
        ),
    ]
