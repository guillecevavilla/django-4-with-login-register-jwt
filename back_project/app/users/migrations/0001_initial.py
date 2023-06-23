# Generated by Django 3.2.7 on 2023-06-22 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '__first__'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('last_name', models.CharField(blank=True, max_length=250, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('rol', models.PositiveIntegerField(blank=True, choices=[(0, 'Root'), (1, 'Administrador'), (2, 'Cliente')], default=0, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, choices=[('OO', 'None'), ('F', 'Femenino'), ('M', 'Masculino'), ('X', 'Otro'), ('Y', 'No Binario'), ('MT', 'Transgénero MTF'), ('FT', 'Transexual FTM')], max_length=3, null=True)),
                ('status', models.PositiveIntegerField(choices=[(0, 'Inactivo'), (1, 'Activo'), (2, 'Deshabilitado')], default=1)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_email_verified', models.BooleanField(blank=True, default=False, null=True)),
                ('is_phone_verified', models.BooleanField(blank=True, default=False, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=100, null=True)),
                ('is_online', models.BooleanField(blank=True, default=False, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_client', to='clients.client')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalUser',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(db_index=True, max_length=30)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('last_name', models.CharField(blank=True, max_length=250, null=True)),
                ('photo', models.TextField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(db_index=True, max_length=254, verbose_name='email address')),
                ('rol', models.PositiveIntegerField(blank=True, choices=[(0, 'Root'), (1, 'Administrador'), (2, 'Cliente')], default=0, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, choices=[('OO', 'None'), ('F', 'Femenino'), ('M', 'Masculino'), ('X', 'Otro'), ('Y', 'No Binario'), ('MT', 'Transgénero MTF'), ('FT', 'Transexual FTM')], max_length=3, null=True)),
                ('status', models.PositiveIntegerField(choices=[(0, 'Inactivo'), (1, 'Activo'), (2, 'Deshabilitado')], default=1)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('is_email_verified', models.BooleanField(blank=True, default=False, null=True)),
                ('is_phone_verified', models.BooleanField(blank=True, default=False, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=100, null=True)),
                ('is_online', models.BooleanField(blank=True, default=False, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('client', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='clients.client')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical user',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
