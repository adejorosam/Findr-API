# Generated by Django 3.0 on 2019-12-27 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=60, verbose_name='username')),
                ('phone_number', models.CharField(max_length=11, unique=True, verbose_name='phone_number')),
                ('is_admin', models.BooleanField(default=False, max_length=6, verbose_name='staff_status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('house_address', models.CharField(max_length=10000, verbose_name='house_address')),
                ('house_name', models.CharField(max_length=60, verbose_name='house_name')),
                ('house_pic', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=60, verbose_name='price')),
                ('isFurnished', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, verbose_name='furnished')),
                ('isParkingSpace', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=70, verbose_name='parkingspace')),
                ('isAvailable', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='available')),
                ('isFenced', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='fenced')),
                ('isHaveWater', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='water')),
                ('isNewHouse', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=80, verbose_name='new')),
                ('isNegotiable', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=80, verbose_name='bargained')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
