# Generated by Django 5.0.4 on 2024-06-05 15:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
        ('item', '0003_alter_item_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to='item.item'),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='members',
            field=models.ManyToManyField(related_name='conversations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='conversationmessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
