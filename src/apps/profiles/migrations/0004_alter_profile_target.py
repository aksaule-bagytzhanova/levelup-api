# Generated by Django 5.0.6 on 2024-07-04 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_profile_is_filled_profile_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='target',
            field=models.CharField(blank=True, choices=[('LW', 'Lose Weight'), ('GW', 'Gain Weight'), ('GMM', 'Gain Muscle Mass'), ('APA', 'Add Physical Activities')], max_length=128, null=True),
        ),
    ]
