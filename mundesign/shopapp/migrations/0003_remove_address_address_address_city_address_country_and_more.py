# Generated by Django 5.0.6 on 2024-06-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_alter_paymentdetails_card_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.CharField(default='unknown city', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.CharField(default='unknown country', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='line1',
            field=models.CharField(default='line1 address', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='line2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='postal_code',
            field=models.CharField(default='123456', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.CharField(default='unknown state', max_length=100),
            preserve_default=False,
        ),
    ]
