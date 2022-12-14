# Generated by Django 4.1.1 on 2022-10-11 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artigo', '0003_categoria_texto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('mensagem', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=False)),
                ('artigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='artigo.artigo')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
