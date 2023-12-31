# Generated by Django 3.2.19 on 2023-07-25 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory_Stock',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('stock_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('reorder_level', models.IntegerField(blank=True, default=0, null=True)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='inventory_management.category')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supply_Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supply_date', models.DateField(blank=True, null=True)),
                ('supply_time', models.TimeField(blank=True, null=True)),
                ('supply_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('Supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory_management.supplier')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='inventory_management.category')),
                ('item', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='inventory_management.inventory_stock')),
            ],
        ),
    ]
