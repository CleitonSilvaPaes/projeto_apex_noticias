# Generated by Django 4.1.1 on 2022-10-11 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artigo', '0005_alter_comentario_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controleviews',
            name='artigo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visualizacao', to='artigo.artigo'),
        ),
    ]
