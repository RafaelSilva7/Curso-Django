# Projeto BLOG

Projeto em Django que simula um blog.

## Instalação

Estas são as instruções gerais para se ter o servidor rodando localmente.

### Criação do banco de dados com o postgresql

Antes da clonagem do projeto devemos criar um banco de dados com o postgresql. Este passo precisa ser feito apenas uma vez. Primeiro instala-se o postgresql com o apt.

```
$ sudo apt install libpq-dev postgresql postgresql-contrib
```

Usa-se o seguinte comando para acessar a linha de comando do postgres.

```
$ sudo -u postgres psql
```

Criamos um novo banco de dados, um novo usuário e o configuramos. Após a configuração garantimos o acesso do usuário ao banco criado.

```
CREATE DATABASE blogservidor;
CREATE USER blogadmin WITH PASSWORD 'blogadmin';

ALTER ROLE blogadmin SET client_encoding TO 'utf8';
ALTER ROLE blogadmin SET default_transaction_isolation TO 'read committed';
ALTER ROLE blogadmin SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE blogservidor TO blogadmin;
```

Podemos então sair da linha de comando do postgresql.

```
\q
```

### Clonagem do projeto

Usa-se os seguintes comandos para criar uma pasta para o projeto e cloná-lo.

```
$ mkdir servidor
$ cd servidor
$ git clone https://bcunhasa@bitbucket.org/abo_uft/servidor.git
```

### Criação do ambiente virtual

Para que não haja conflitos entre as versões das bibliotecas usadas com as que já estão na máquina, usamos um ambiente virtual.

```
$ sudo apt install python3-venv
$ python3 -m venv env
```

Para ativar o ambiente virtual usamos o seguinte comando:

```
$ source env/bin/activate
```

Para desativar:

```
$ deactivate
```

### Instalação das bibliotecas

Com o ambiente virtual ativado, instalamos as bibliotecas com o seguinte comando:

```
$ pip3 install -r requirements.txt
```

O arquivo requiriments possui as informações necessárias para a instalação dos arquivos. Caso haja algum problema com o comando anterior, é possível utilizar o seguinte:

```
$ python env/bin/pip3 install -r requirements.txt
```

### Iniciando o servidor django

É necessário, agora, migrar o banco de dados.

```
$ python manage.py migrate
$ python manage.py makemigrations administracao
$ python manage.py migrate administracao
```

Criamos, então, um usuário administrador.

```
$ python manage.py createsuperuser
```

Finalmente podemos iniciar o servidor.

```
$ python manage.py runserver
```

Ele pode ser acessado pelo URL padrão "localhost:8000" ou "127.0.0.1:8000".
