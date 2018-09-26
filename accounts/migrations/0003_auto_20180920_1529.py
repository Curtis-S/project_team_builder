# Generated by Django 2.1.1 on 2018-09-20 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180920_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userskill',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_skill_relation', to='accounts.Skill'),
        ),
    ]