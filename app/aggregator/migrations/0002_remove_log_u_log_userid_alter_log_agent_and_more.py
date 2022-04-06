# Generated by Django 4.0.3 on 2022-04-06 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='u',
        ),
        migrations.AddField(
            model_name='log',
            name='userid',
            field=models.CharField(default='-', help_text='u, frank', max_length=5),
        ),
        migrations.AlterField(
            model_name='log',
            name='agent',
            field=models.CharField(help_text='User-agent', max_length=600),
        ),
        migrations.AlterField(
            model_name='log',
            name='code',
            field=models.IntegerField(help_text='>s'),
        ),
        migrations.AlterField(
            model_name='log',
            name='hyphen',
            field=models.CharField(default='-', help_text='l', max_length=1),
        ),
        migrations.AlterField(
            model_name='log',
            name='ip',
            field=models.GenericIPAddressField(help_text='h', protocol='IPv4'),
        ),
        migrations.AlterField(
            model_name='log',
            name='method',
            field=models.CharField(default='-', help_text='%r -> m', max_length=6),
        ),
        migrations.AlterField(
            model_name='log',
            name='protocol',
            field=models.CharField(default='-', help_text='%r -> H', max_length=1),
        ),
        migrations.AlterField(
            model_name='log',
            name='referer',
            field=models.URLField(help_text='Referer'),
        ),
        migrations.AlterField(
            model_name='log',
            name='size',
            field=models.IntegerField(help_text='b'),
        ),
        migrations.AlterField(
            model_name='log',
            name='time',
            field=models.DateTimeField(help_text='t'),
        ),
        migrations.AlterField(
            model_name='log',
            name='url',
            field=models.CharField(default='-', help_text='%r -> U', max_length=500),
        ),
    ]
