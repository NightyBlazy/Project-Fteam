# Generated by Django 4.1.7 on 2023-02-27 08:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayType',
            fields=[
                ('paytype_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('paytype_name', models.CharField(max_length=10)),
                ('paytype_rate', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.AlterField(
            model_name='sales',
            name='sale_paytype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.paytype'),
        ),
    ]