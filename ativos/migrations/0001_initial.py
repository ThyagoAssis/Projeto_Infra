# Generated by Django 4.2.18 on 2025-02-04 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoAtivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('fabricante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelos', to='ativos.fabricante')),
            ],
        ),
        migrations.CreateModel(
            name='Ativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('mac_address', models.CharField(blank=True, max_length=17, null=True)),
                ('data_aquisicao', models.DateField(blank=True, null=True)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.departamento')),
                ('fabricante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ativos.fabricante')),
                ('modelo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ativos.modelo')),
                ('tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ativos.tipoativo')),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ativos', to='core.unidade')),
            ],
        ),
    ]
