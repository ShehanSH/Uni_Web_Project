# Generated by Django 3.2.19 on 2023-07-25 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory_management', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SportsItemRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('request_date', models.DateField()),
                ('request_time', models.TimeField()),
                ('req_quantity', models.PositiveIntegerField()),
                ('approval_status', models.CharField(choices=[('A', 'Approval'), ('D', 'Disapproval'), ('I', 'Issued')], default='D', max_length=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.category')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.inventory_stock')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SportsItemReceived',
            fields=[
                ('received_id', models.AutoField(primary_key=True, serialize=False)),
                ('received_date', models.DateField()),
                ('received_time', models.TimeField()),
                ('received_quantity', models.PositiveIntegerField()),
                ('received_status', models.CharField(choices=[('R', 'Recived'), ('N', 'Not Recived')], default='N', max_length=1)),
                ('item_status', models.CharField(choices=[('D', 'Damaged'), ('ND', 'Not Damaged')], default='ND', max_length=2)),
                ('description', models.TextField(help_text='Enter a brief description of the recived item', max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.category')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.inventory_stock')),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports_items_req.sportsitemrequest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
