# Generated by Django 2.1.8 on 2019-04-27 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields
import model_utils.fields
import uuid
import swapper


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('level', models.CharField(choices=[('success', 'success'), ('info', 'info'), ('warning', 'warning'), ('error', 'error')], default='info', max_length=20)),
                ('unread', models.BooleanField(db_index=True, default=True)),
                ('actor_object_id', models.CharField(max_length=255)),
                ('verb', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('target_object_id', models.CharField(blank=True, max_length=255, null=True)),
                ('action_object_object_id', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('public', models.BooleanField(db_index=True, default=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('emailed', models.BooleanField(db_index=True, default=False)),
                ('data', jsonfield.fields.JSONField(blank=True, null=True)),
                ('action_object_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_action_object', to='contenttypes.ContentType')),
                ('actor_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notify_actor', to='contenttypes.ContentType')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
                ('target_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_target', to='contenttypes.ContentType')),
            ],
            options={
                'swappable': swapper.swappable_setting('notifications', 'Notification'),
                'abstract': False,
                'ordering': ('-timestamp',),
            },
        ),
        migrations.AlterIndexTogether(
            name='notification',
            index_together={('recipient', 'unread')},
        ),
        migrations.CreateModel(
            name='NotificationUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('receive', models.BooleanField(default=True, help_text='note: non-superadmin users receive notifications only for organizations of which they are member of.', verbose_name='receive notifications')),
                ('email', models.BooleanField(default=True, help_text='note: non-superadmin users receive notifications only for organizations of which they are member of.', verbose_name='email notifications')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user notification settings',
                'verbose_name_plural': 'user notification settings',
            },
        ),
    ]
