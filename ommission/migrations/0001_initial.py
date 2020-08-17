# Generated by Django 2.2 on 2020-08-14 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('omuser', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Missions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flow_uuid', models.UUIDField(blank=True, null=True, verbose_name='流程編號')),
                ('flow_name', models.TextField(blank=True, null=True, verbose_name='流程名稱')),
                ('status', models.TextField(blank=True, null=True, verbose_name='狀態')),
                ('level', models.TextField(blank=True, null=True, verbose_name='燈號')),
                ('title', models.TextField(blank=True, null=True, verbose_name='標題')),
                ('data_no', models.IntegerField(blank=True, null=True, verbose_name='資料編號')),
                ('data_id', models.IntegerField(blank=True, null=True, verbose_name='資料流水號')),
                ('history', models.BooleanField(default=False, verbose_name='歷史資料')),
                ('stop_uuid', models.TextField(blank=True, null=True, verbose_name='關卡')),
                ('stop_chart_text', models.TextField(blank=True, null=True, verbose_name='關卡名稱')),
                ('ticket_createtime', models.DateTimeField(blank=True, null=True, verbose_name='開單時間')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='更新時間')),
                ('action', models.TextField(blank=True, null=True, verbose_name='快速操作')),
                ('attachment', models.BooleanField(default=False, verbose_name='附加檔案')),
                ('closed', models.BooleanField(default=False, verbose_name='關單')),
                ('assign_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_mission', to='omuser.OmGroup', verbose_name='受派群組')),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_mission', to=settings.AUTH_USER_MODEL, verbose_name='受派人')),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='create_ticket', to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='開單人員')),
                ('update_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_ticket', to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='更新人員')),
            ],
            options={
                'default_permissions': (),
            },
        ),
    ]