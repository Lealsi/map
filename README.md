## Sobre
O Projeto Mulheres na América Portuguesa - M.A.P. - é um Projeto conduzido por pesquisadoras do Grupo de Pesquisas Humanidades Digitais , abrigado no Núcleo de Apoio à Pesquisas em Etimologia e História da Língua Portuguesa ( NEHiLP) da Universidade de São Paulo e ligado ao Laboratório Virtual de Humanidades Digitais (LaViHD).

O M.A.P. está reunindo um conjunto de fontes documentais imensamente importantes para os estudos filológicos e para os estudos da história das mulheres no Brasil, na forma de documentos escritos por mulheres, ou que relatam seu discurso, entre 1500 e 1822, no espaço atlântico português (veja aqui nosso projeto completo e as perguntas que o motivaram).

A metodologia seguida no Projeto trata essa documentação a partir de duas premissas: primeiro, importa-nos, centralmente, a literalidade da expressão e a literalidade do relato da expressão, sendo esta uma investigação originária do campo da filologia e da linguística histórica. Segundo, do ponto de vista computacional, partimos do compromisso com as tecnologias transferíveis e o acesso aberto, sendo nosso objetivo a difusão e democratização da informação encerrada na documentação trabalhada.

Para reunir esses documentos, pesquisamos em arquivos e acervos digitais no Brasil e em Portugal. Depois de ler, discutir e preparar filologicamente cada documento, sistematizamos as informações em um Catálogo Digital com acesso livre.

## Procedimentos mínimos para ambiente de desenvolvimento

Dependências Debian:

    sudo apt-get install pkg-config python3-dev default-libmysqlclient-dev build-essential

Opção se for usar virtualenv:

    python3 -m venv venv
    source venv/bin/activate
    ./venv/bin/pip3 install -r requirements.txt

Gerando uma secret key:

    python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

Configurando variáveis de ambiente (secret key gerada anteriormente e mysql):

    cp .env.sample .env

Rodando migrations e subindo server:

    python manage.py migrate
    python manage.py runserver
