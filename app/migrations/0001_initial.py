# Generated by Django 3.2.9 on 2022-09-17 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, verbose_name='Código')),
                ('nome_modernizado', models.CharField(max_length=100, verbose_name='Nome modernizado')),
                ('grafia_conservadora', models.CharField(max_length=100, verbose_name='Grafia conservadora do nome')),
                ('trecho_nomeacao', models.TextField(max_length=400, verbose_name='Trecho modernizado de nomeação')),
                ('trecho_voz', models.TextField(max_length=350, verbose_name='Trecho modernizado da voz')),
                ('detalhamento_perfil', models.TextField(max_length=350, verbose_name='Detalhamento do perfil')),
                ('unidade_menor_nascimento', models.CharField(max_length=100, verbose_name='Unidade administrativa menor do local de nascimento')),
                ('conservadora_menor_nascimento', models.CharField(max_length=100, verbose_name='Forma conservadora da unidade administrativa menor do local de nascimento')),
                ('unidade_intermediaria_nascimento', models.CharField(max_length=100, verbose_name='Unidade administrativa intermediária do local de nascimento')),
                ('conservadora_intermediaria_nascimento', models.CharField(max_length=100, verbose_name='Forma conservadora da unidade administrativa intermediária de nascimento')),
                ('unidade_maior_nascimento', models.CharField(max_length=100, verbose_name='Unidade administrativa maior do local de nascimento')),
                ('conservadora_maior_nascimento', models.CharField(max_length=100, verbose_name='Forma conservadora da unidade administrativa maior de nascimento')),
                ('point_nascimento', models.CharField(max_length=100, verbose_name='Point de georreferenciamento do local de nascimento')),
                ('total_filhs', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Número total de filhas e filhos')),
                ('total_filhas', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Número total de filhas')),
                ('total_filhos', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Número total de filhos')),
                ('nome_filhs_modernizado', models.TextField(max_length=200, verbose_name='Filhas(os) nomeadas(os)')),
                ('referencia_dmb', models.CharField(max_length=100, verbose_name='Referência no DMB')),
                ('trecho_bibliografia', models.TextField(max_length=400, verbose_name='Trecho de menção na bibliografia')),
                ('fonte_bibliografia', models.TextField(max_length=200, verbose_name='Fonte da menção na bibliografia')),
                ('responsavel_catalogacao', models.CharField(max_length=100, verbose_name='Responsabilidade pela catalogação')),
                ('informacoes_internas', models.TextField(blank=True, verbose_name='Informações internas')),
                ('data_catalogacao', models.DateTimeField(null=True, verbose_name='Data da Catalogação')),
                ('responsavel_revisao_catalogacao', models.CharField(max_length=100, null=True, verbose_name='Responsabilidade pela revisão da catalogação')),
                ('data_edicao', models.DateTimeField(blank=True, null=True, verbose_name='Data de Edição')),
                ('data_revisao_catalogacao', models.DateTimeField(null=True, verbose_name='Data da revisão mais recente da catalogação')),
                ('publicar', models.BooleanField(null=True, verbose_name='Habilitar para publicação')),
                ('perfil_documental', models.CharField(choices=[('OP1', 'Opção 1'), ('OP2', 'Opção 2'), ('OP3', 'Opção 3'), ('OP4', 'Opção 4'), ('OP5', 'Opção 5')], default='OP1', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_escrita', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Ano de escrita do documento')),
                ('datacao_cronologica_inicial', models.CharField(max_length=15, verbose_name='Datação cronológica inicial')),
                ('datacao_cronologica_final', models.CharField(max_length=15, verbose_name='Datação cronológica final')),
                ('descricao_conteudo_documento', models.TextField(max_length=1000, verbose_name='Descrição do conteúdo do documento')),
                ('descricao_materia_documento', models.TextField(max_length=1500, verbose_name='Descrição material do documento')),
                ('autoria_documento', models.CharField(max_length=100, verbose_name='Autoria intelectual do documento')),
                ('autoria_institucional', models.CharField(max_length=100, verbose_name='Autoria institucional do documento')),
                ('autoria_material', models.CharField(max_length=100, verbose_name='Autoria material do documento')),
                ('chave_pesquisa', models.CharField(max_length=100, verbose_name='Chave de pesquisa')),
                ('condicao_documento', models.CharField(max_length=100, verbose_name='Condição de acesso ao documento primário')),
                ('indexador_fonte', models.TextField(max_length=500, verbose_name='Indexador na fonte')),
                ('url_fonte', models.CharField(max_length=1000, verbose_name='URL da fonte')),
                ('idade_catalogada_documento', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Idade da catalogada mencionada no documento')),
                ('qualificacao_social_documento', models.CharField(max_length=100, verbose_name='Qualificação social explicitada no documento')),
                ('unidade_menor_escrita', models.CharField(max_length=100, verbose_name='Unidade administrativa menor de escrita')),
                ('conservadora_menor_escrita', models.CharField(max_length=100, verbose_name='Forma conservadora da unidade administrativa menor do local de escrita')),
                ('unidade_intermediaria_escrita', models.CharField(max_length=100, verbose_name='Unidade administrativa intermediária de escrita')),
                ('conservadora_intermediaria_escrita', models.CharField(max_length=100, verbose_name='Forma conservadora da unidade administrativa intermediária do local de escrita')),
                ('unidade_maior_escrita', models.CharField(max_length=100, verbose_name='Unidade administrativa maior de escrita')),
                ('conservadora_maior_escrita', models.CharField(max_length=100, verbose_name='Forma conservadora da unidade administrativa maior do local de escrita')),
                ('point_escrita', models.CharField(max_length=100, verbose_name='Point de georreferenciamento do local de escrita')),
                ('unidade_menor_morada', models.CharField(max_length=100, verbose_name='Unidade administrativa menor de morada')),
                ('conservadora_menor_morada', models.CharField(max_length=100, verbose_name='Forma conservadora da unidade administrativa menor de morada')),
                ('unidade_intermediaria_morada', models.CharField(max_length=100, verbose_name='Unidade administrativa intermediária de morada')),
                ('conservadora_intermediaria_morada', models.CharField(max_length=100, verbose_name='Forma conservadora da unidade administrativa intermediária de morada')),
                ('unidade_maior_morada', models.CharField(max_length=100, verbose_name='Unidade administrativa maior de morada')),
                ('conservadora_maior_morada', models.CharField(max_length=100, verbose_name='Forma conservadora da unidade administrativa maior de morada')),
                ('point_morada', models.CharField(max_length=20, verbose_name='Point de georreferenciamento do local de morada')),
                ('edicao_filologica_parcial', models.TextField(max_length=3000, verbose_name='Edição filológica modernizada parcial do documento')),
                ('autoria_edicao_conservadora', models.TextField(max_length=100, verbose_name='Autoria da edição filológica conservadora')),
                ('autoria_edicao_modernizada', models.TextField(max_length=100, verbose_name='Autoria da edição filológica modernizada')),
                ('responsabilidade_revisao_parcial', models.TextField(max_length=100, verbose_name='Responsabilidade pela revisão da edição parcial')),
                ('data_revisao', models.CharField(max_length=15, verbose_name='Data da revisão mais recente da edição parcial')),
                ('ligacao_edicao_filologica', models.CharField(max_length=1000, verbose_name='Ligação para a edição filológica')),
                ('rede_documental', models.TextField(max_length=500, verbose_name='Rede documental')),
                ('terceira_referida', models.CharField(max_length=100, verbose_name='Terceira(s) referida(s)')),
                ('trabalhos_andamento', models.TextField(verbose_name='Trabalho(s) em andamento no M.A.P.')),
                ('trabalhos_derivados', models.TextField(verbose_name='Trabalhos derivados publicados pelo M.A.P.')),
                ('tema', models.CharField(max_length=100, verbose_name='Tema')),
                ('subtema', models.CharField(max_length=100, verbose_name='Subtema')),
                ('informacoes_internas', models.TextField(blank=True, verbose_name='Informações internas do documento')),
                ('link_gdrive', models.CharField(max_length=1000, verbose_name='Link para a pasta de imagens no GDrive')),
                ('gx_media_links', models.CharField(max_length=1000, verbose_name='gx_media_links')),
                ('colaboracao', models.CharField(blank=True, max_length=100, verbose_name='Colaborador(a)')),
                ('creditos_imagem', models.CharField(blank=True, max_length=100, verbose_name='Créditos de imagem')),
                ('responsavel_documento', models.CharField(max_length=100, verbose_name='Responsabilidade pelo documento')),
                ('data_documento', models.DateTimeField(null=True, verbose_name='Data do documento')),
                ('data_edicao_documento', models.DateTimeField(null=True, verbose_name='Data da edição do documento')),
                ('publicar', models.BooleanField(null=True, verbose_name='Habilitar para publicação')),
                ('tipo_documento', models.CharField(choices=[('OP1', 'Opção 1'), ('OP2', 'Opção 2'), ('OP3', 'Opção 3'), ('OP4', 'Opção 4'), ('OP5', 'Opção 5')], default='OP1', max_length=100)),
                ('subtipo_documento', models.CharField(choices=[('OP1', 'Opção 1'), ('OP2', 'Opção 2'), ('OP3', 'Opção 3'), ('OP4', 'Opção 4'), ('OP5', 'Opção 5')], default='OP1', max_length=100)),
                ('ano_inferencia', models.CharField(choices=[('OP1', 'Opção 1'), ('OP2', 'Opção 2'), ('OP3', 'Opção 3'), ('OP4', 'Opção 4'), ('OP5', 'Opção 5')], default='OP1', max_length=100)),
                ('cronologica_inicial_inferencia', models.CharField(choices=[('OP1', 'Opção 1'), ('OP2', 'Opção 2'), ('OP3', 'Opção 3'), ('OP4', 'Opção 4'), ('OP5', 'Opção 5')], default='OP1', max_length=100)),
                ('cronologica_final_inferencia', models.CharField(choices=[('OP1', 'Opção 1'), ('OP2', 'Opção 2'), ('OP3', 'Opção 3'), ('OP4', 'Opção 4'), ('OP5', 'Opção 5')], default='OP1', max_length=100)),
                ('perfil_documental', models.CharField(choices=[('ATR', 'Autora'), ('ATRP', 'Autora indireta'), ('NDP', 'Nomeada em documento primário')], default='ATR', max_length=100)),
                ('arquivo_guarda', models.CharField(choices=[('OP1', 'Opção 1'), ('OP2', 'Opção 2'), ('OP3', 'Opção 3'), ('OP4', 'Opção 4'), ('OP5', 'Opção 5')], default='OP1', max_length=100)),
                ('estado_civil', models.CharField(choices=[('OP1', 'Opção 1'), ('OP2', 'Opção 2'), ('OP3', 'Opção 3'), ('OP4', 'Opção 4'), ('OP5', 'Opção 5')], default='OP1', max_length=100)),
                ('catalogadas', models.ManyToManyField(related_name='documentos', to='app.Catalogada', verbose_name='Catalogada')),
            ],
        ),
    ]
