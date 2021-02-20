# Generated by Django 3.1.5 on 2021-01-23 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Omdata_dc33fb340034418c8fbb3baf15525e86',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flow_uuid', models.UUIDField(blank=True, null=True, verbose_name='流程編號')),
                ('dataid_header', models.CharField(max_length=3, verbose_name='資料代碼')),
                ('data_no', models.IntegerField(blank=True, null=True, verbose_name='資料編號')),
                ('history', models.BooleanField(default=False, verbose_name='歷史資料')),
                ('status', models.CharField(blank=True, max_length=200, null=True, verbose_name='狀態')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='標題')),
                ('level', models.CharField(blank=True, max_length=200, null=True, verbose_name='燈號')),
                ('group', models.CharField(blank=True, max_length=500, null=True, verbose_name='受派群組')),
                ('closed', models.BooleanField(default=False, verbose_name='關閉標記')),
                ('stop_uuid', models.TextField(blank=True, null=True, verbose_name='關卡')),
                ('stop_chart_type', models.TextField(blank=True, null=True, verbose_name='關卡類型')),
                ('stop_chart_text', models.TextField(blank=True, null=True, verbose_name='關卡名稱')),
                ('running', models.BooleanField(default=False, verbose_name='執行標記')),
                ('error', models.BooleanField(default=False, verbose_name='是否異常')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='更新時間')),
                ('stoptime', models.DateTimeField(blank=True, null=True, verbose_name='停止時間')),
                ('data_param', models.TextField(blank=True, null=True, verbose_name='流程參數')),
                ('error_message', models.TextField(blank=True, null=True, verbose_name='錯誤訊息')),
                ('is_child', models.BooleanField(default=False, verbose_name='子單')),
                ('formitm_1', models.TextField(blank=True, null=True)),
                ('formitm_2', models.TextField(blank=True, null=True)),
                ('formitm_3', models.TextField(blank=True, null=True)),
                ('formitm_4', models.TextField(blank=True, null=True)),
                ('formitm_5', models.TextField(blank=True, null=True)),
                ('formitm_6', models.TextField(blank=True, null=True)),
                ('formitm_7', models.TextField(blank=True, null=True)),
            ],
            options={
                'permissions': (('Omdata_dc33fb340034418c8fbb3baf15525e86_Add', '新增任務單'), ('Omdata_dc33fb340034418c8fbb3baf15525e86_Modify', '修改任務單'), ('Omdata_dc33fb340034418c8fbb3baf15525e86_View', '檢視任務單'), ('Omdata_dc33fb340034418c8fbb3baf15525e86_Delete', '刪除任務單')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Omdata_dc33fb340034418c8fbb3baf15525e86_DataNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Omdata_dc33fb340034418c8fbb3baf15525e86_ValueHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flow_uuid', models.UUIDField(blank=True, null=True, verbose_name='流程編號')),
                ('data_no', models.IntegerField(blank=True, null=True, verbose_name='資料編號')),
                ('data_id', models.IntegerField(blank=True, null=True, verbose_name='多重資料編號')),
                ('chart_id', models.CharField(blank=True, max_length=500, null=True, verbose_name='功能點')),
                ('stop_chart_type', models.TextField(blank=True, null=True, verbose_name='關卡類型')),
                ('stop_chart_text', models.TextField(blank=True, null=True, verbose_name='關卡名稱')),
                ('input_data', models.TextField(blank=True, null=True, verbose_name='輸入參數')),
                ('output_data', models.TextField(blank=True, null=True, verbose_name='輸出參數')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='更新時間')),
                ('error', models.BooleanField(default=False, verbose_name='異常標記')),
            ],
            options={
                'default_permissions': (),
            },
        ),
    ]
