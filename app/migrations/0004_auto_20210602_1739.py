# Generated by Django 3.1.4 on 2021-06-02 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210602_1639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='stripe_change_id',
            new_name='stripe_charge_id',
        ),
    ]
