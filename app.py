from flask import Flask
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tabelas.db'
db.init_app(app)


'''
1 - a rota /api mostrará uma página web com a ducomentação da API
2 - As rotas iniciadas com /api/municipios acessarão os dados da tabela Município
3 - As rotas iniciadas com /api/estado acessarão os dados da tabela Estado
    3.1 - Caso dê tempo fazer tudo, adicionamos mais uma rota pra acessar dados
4 - Pesquisar sobre como fazer a autenticação do acesso

Obs.: Antes de desenvolver as funções lembrar de criar/conectar/povoar banco de dados SQLite
'''

'''import csv

Dados dos muunicípios adicionados à tabela municipios
@app.route("/povoar_bd")
def index():
    f = open("data/mun_csv.csv", encoding='utf-8')
    data = csv.reader(f)
    output = ""

    id = 1
    for municipio, sigla_UF, regiao, vitimas, mes, ano in data:
        m = Municipio(id=id, municipio=municipio, sigla_UF=sigla_UF, regiao=regiao, vitimas=vitimas, mes=mes, ano=ano)
        db.session.add(m)
        output = output + f"Município {m.municipio} - {m.sigla_UF}."
        id = id+1
    db.session.commit()

    return output
'''

@app.route('/api')
def documentacao():

    '''
    :return: Página da documentação da API
    '''

@app.route('/api/municipio')
def municipios():
    '''
    :return: todos os dados da base de dados de municípios
    '''


@app.route('/api/municipio/uf=<string:uf>')
def municipio_nome(uf):
    '''
    :param uf: sigla da UF
    :return: Todos os dados de um estado específico
    '''


@app.route('/api/municipio/inicio=<string:data_inicio>&fim=<string:data_fim>')
def municipio_data(data_inicio, data_fim):
    '''
    Obs.: Criar rotas alternativas caso o usuário entre apenas com a data de início,
          ou apenas com a data final.
    :param data_inicio: Data inicial que se deseja obter os dados
    :param data_fim: Data final que se deseja obter os dados
    :return: Os dados de todos os municípios dentro do intervalo passados pelo usuário
    '''


@app.route('/api/municipio/uf=<string:uf>/inicio=<string:data_inicio>&fim=<string:data_fim>')
def municipio_e_data(uf, data_inicio, data_fim):
    '''
    Obs.: Essa função pode ser adicionada na função municipio_nome(), com parâmetros default
    :param uf: Sigla da UF
    :param data_inicio: Data inicial que se deseja obter os dados
    :param data_fim: Data final que se deseja obter os dados
    :return: Os dados de um estado específico dentro do intervalo passados pelo usuário
    '''


@app.route('/api/estado')
def estados():
    '''
    :return: todos os dados da base de dados por estado
    '''


@app.route('/api/estado/uf=<string:uf>')
def estado(uf):
    '''
    :param uf: sigla da UF
    :return: todos os dados da base de um estado específico
    '''


@app.route('/api/estado/inicio=<string:data_inicio>&fim=<string:data_fim>')
def estado_data(data_inicio, data_fim):
    '''
    :param data_inicio: Data inicial que se deseja obter os dados
    :param data_fim: Data final que se deseja obter os dados
    :return: Todos os dados da base de dados dos estados em um determinado intervalo de tempo
    '''


@app.route('/api/estado/uf=<string:uf>/inicio=<string:data_inicio>&fim=<string:data_fim>')
def estado_e_data(uf, data_inicio, data_fim):
    '''
    :param uf: siga da UF
    :param data_inicio: todos os dados da base de um estado específico
    :param data_fim: Data final que se deseja obter os dados
    :return: Os dados de um município específico dentro do intervalo passados pelo usuário
    '''


if __name__ == '__main__':
    app.run()