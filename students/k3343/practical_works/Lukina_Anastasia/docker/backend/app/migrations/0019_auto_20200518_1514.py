# Generated by Django 2.1.11 on 2020-05-18 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20200518_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compparticipation',
            name='result',
        ),
        migrations.AddField(
            model_name='result',
            name='comp_participation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.CompParticipation', verbose_name='Участие'),
            preserve_default=False,
        ),
    ]