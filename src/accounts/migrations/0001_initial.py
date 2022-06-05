# Generated by Django 3.2.13 on 2022-06-05 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('customerID', models.OneToOneField(help_text='ID for the desired customer to be looked up.', on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('date', models.DateTimeField(auto_now=True)),
                ('accountID', models.ForeignKey(help_text='ID for the desired customer to be looked up.', on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='accounts.account')),
            ],
        ),
    ]
