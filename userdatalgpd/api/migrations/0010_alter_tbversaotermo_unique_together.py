# Generated by Django 4.0.3 on 2022-04-28 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_historico_adicao_usuario_terceiro_grupo_cnpj_terceiro_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tbversaotermo',
            unique_together={('fk_ter_id', 'vte_versao')},
        ),
    ]
