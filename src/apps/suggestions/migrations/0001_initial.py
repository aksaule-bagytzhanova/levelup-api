# Generated by Django 5.0.6 on 2024-07-04 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('type', models.CharField(choices=[('nutritionist', 'Nutritionist Doctor'), ('dietitian', 'Dietitian Doctor'), ('acupuncturists', 'Acupuncturists Doctor'), ('homeopaths', 'Homeopaths Doctor'), ('naturopaths', 'Naturopaths Doctor')], max_length=20)),
                ('is_saved', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]
