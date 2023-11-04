# Generated by Django 4.2.7 on 2023-11-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField(default='Descrição do produto', max_length=800)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=4)),
                ('quantidade', models.PositiveIntegerField()),
                ('categoria', models.CharField(choices=[('Eletrônicos', 'Eletrônicos'), ('Casa e Decoração', 'Casa e Decoração'), ('Moda', 'Moda')], max_length=16)),
            ],
        ),
    ]