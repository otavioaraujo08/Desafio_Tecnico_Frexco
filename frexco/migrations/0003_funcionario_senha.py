# Generated by Django 4.0.3 on 2022-03-25 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frexco', '0002_funcionario_delete_funcionarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='senha',
            field=models.CharField(default='admin123', max_length=30, null=True),
        ),
    ]