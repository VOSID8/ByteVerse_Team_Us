# Generated by Django 4.1.7 on 2023-02-26 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slot', '0002_scheduledslot_channel_scheduledslot_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledslot',
            name='uid',
            field=models.CharField(blank=True, default='', max_length=1500),
        ),
        migrations.AlterField(
            model_name='scheduledslot',
            name='channel',
            field=models.CharField(blank=True, default='', max_length=1500),
        ),
        migrations.AlterField(
            model_name='scheduledslot',
            name='token',
            field=models.CharField(blank=True, default='', max_length=2500),
        ),
    ]