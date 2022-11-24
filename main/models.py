# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EstoqueMateria(models.Model):
    id_materia = models.IntegerField(primary_key=True)
    estoque_minimo_materia_id_estoque_minimo = models.ForeignKey('EstoqueMinimoMateria', models.CASCADE, db_column='estoque_minimo_materia_id_estoque_minimo')
    id_lote = models.IntegerField()
    dat_saida = models.DateTimeField(blank=True, null=True)
    qtd_estoque = models.FloatField(blank=True, null=True)
    item = models.CharField(max_length=45, blank=True, null=True)
    ord_compra = models.IntegerField(blank=True, null=True)
    dat_entrada = models.DateTimeField(blank=True, null=True)
    dat_validade = models.DateTimeField(blank=True, null=True)
    qtd_saida = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estoque_materia'


class EstoqueMinimo(models.Model):
    id_estoque_minimo = models.IntegerField(primary_key=True)
    qtd_min = models.FloatField(blank=True, null=True)
    produto_id_prod = models.ForeignKey('Produto', models.CASCADE, db_column='produto_id_prod')

    class Meta:
        managed = False
        db_table = 'estoque_minimo'


class EstoqueMinimoMateria(models.Model):
    id_estoque_minimo = models.IntegerField(primary_key=True)
    qtd_min = models.FloatField(blank=True, null=True)
    descricao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estoque_minimo_materia'


class EstoqueProduto(models.Model):
    id_estoque_produto = models.IntegerField(primary_key=True)
    estoque_produto = models.IntegerField(blank=True, null=True)
    produto_id_prod = models.ForeignKey('Produto', models.CASCADE, db_column='produto_id_prod')
    id_estoque_min = models.ForeignKey(EstoqueMinimo, models.CASCADE, db_column='id_estoque_min')

    class Meta:
        managed = False
        db_table = 'estoque_produto'


class Fornecedor(models.Model):
    id_fornecedor = models.IntegerField(primary_key=True)
    materia = models.CharField(max_length=45, blank=True, null=True)
    quantidade = models.FloatField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fornecedor'


class FornecedorHasEstoqueMateria(models.Model):
    fornecedor_id_fornecedor = models.OneToOneField(Fornecedor, models.CASCADE, db_column='fornecedor_id_fornecedor', primary_key=True)
    estoque_materia_id_materia = models.ForeignKey(EstoqueMateria, models.CASCADE, db_column='estoque_materia_id_materia')

    class Meta:
        managed = False
        db_table = 'fornecedor_has_estoque_materia'


class Manutencao(models.Model):
    id_manutencao = models.IntegerField(primary_key=True)
    dat_manutencao = models.DateTimeField(blank=True, null=True)
    dat_revisao = models.DateTimeField(blank=True, null=True)
    iten_substituido = models.CharField(max_length=45, blank=True, null=True)
    tecnico_id_tecnico = models.ForeignKey('Tecnico', models.CASCADE, db_column='tecnico_id_tecnico')
    maquina_id_maq = models.ForeignKey('Maquina', models.CASCADE, db_column='maquina_id_maq')

    class Meta:
        managed = False
        db_table = 'manutencao'


class Maquina(models.Model):
    id_maq = models.IntegerField(primary_key=True)
    estoque_materia_id_materia = models.ForeignKey(EstoqueMateria, models.CASCADE, db_column='estoque_materia_id_materia')
    descricao = models.CharField(max_length=100, blank=True, null=True)
    turno = models.CharField(max_length=45, blank=True, null=True)
    tip_maq = models.CharField(max_length=45, blank=True, null=True)
    itns_substituido = models.CharField(max_length=45, blank=True, null=True)
    maq_producao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maquina'


class Operador(models.Model):
    id_operador = models.IntegerField(primary_key=True)
    maquina_id_maq = models.ForeignKey(Maquina, models.CASCADE, db_column='maquina_id_maq')
    producao = models.CharField(max_length=45, blank=True, null=True)
    dat_ingre_funcao = models.DateTimeField(blank=True, null=True)
    turno = models.CharField(max_length=45, blank=True, null=True)
    funcao = models.CharField(max_length=45, blank=True, null=True)
    setor = models.CharField(max_length=45, blank=True, null=True)
    dat_uso_maq = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operador'


class Peca(models.Model):
    id_peca = models.IntegerField(primary_key=True)
    qtd_iten = models.FloatField(blank=True, null=True)
    descricao = models.CharField(max_length=45, blank=True, null=True)
    manutencao_id_manutencao = models.ForeignKey(Manutencao, models.CASCADE, db_column='manutencao_id_manutencao')

    class Meta:
        managed = False
        db_table = 'peca'


class Producao(models.Model):
    id_producao = models.IntegerField(primary_key=True)
    dat_fabricacao = models.DateField(blank=True, null=True)
    qtd_prodcao_item = models.FloatField(blank=True, null=True)
    lote_producao = models.IntegerField(blank=True, null=True)
    linha_producao = models.IntegerField(blank=True, null=True)
    qtd_descarte = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producao'


class Produto(models.Model):
    id_prod = models.IntegerField(primary_key=True)
    estoque_materia = models.ForeignKey(EstoqueMateria, models.CASCADE)
    producao_id_producao = models.ForeignKey(Producao, models.CASCADE, db_column='producao_id_producao')
    maquina_id_maq = models.ForeignKey(Maquina, models.CASCADE, db_column='maquina_id_maq')
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produto'




class Tecnico(models.Model):
    id_tecnico = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45, blank=True, null=True)
    especialidade = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tecnico'


class Verificacao(models.Model):
    id_verificacao = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=45, blank=True, null=True)
    manutencao_id_manutencao = models.ForeignKey(Manutencao, models.CASCADE, db_column='manutencao_id_manutencao')

    class Meta:
        managed = False
        db_table = 'verificacao'
