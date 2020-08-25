from flask import Flask

app = Flask(__name__)

'''
1 - a rota /api mostrará uma página web com a ducomentação da API
2 - As rotas iniciadas com /api/municipios acessarão os dados da tabela Município
3 - As rotas iniciadas com /api/estado acessarão os dados da tabela Estado
    3.1 - Caso dê tempo fazer tudo, adicionamos mais uma rota pra acessar dados
4 - Pesquisar sobre como fazer a autenticação do acesso
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


@app.route('api/municipio/uf=<str:uf>')
def municipio_nome(uf):
    '''
    :param uf: sigla da UF
    :return: Todos os dados de um município específico
    '''


@app.route('api/municipio/inicio=<str:data_inicio>&fim=<str:data_fim>')
def municipio_data(data_inicio, data_fim):
    '''
    Obs.: Criar rotas alternativas caso o usuário entre apenas com a data de início,
          ou apenas com a data final.
    :param data_inicio: Data inicial que se deseja obter os dados
    :param data_fim: Data final que se deseja obter os dados
    :return: Os dados de todos os municípios dentro do intervalo passados pelo usuário
    '''


@app.route('api/municipio/uf=<str:uf>/inicio=<str:data_inicio>&fim=<str:data_fim>')
def municipio_mun_data(uf, data_inicio, data_fim):
    '''
    Obs.: Essa função pode ser adicionada na função municipio_nome(), com parâmetros default
    :param uf: Sigla da UF
    :param data_inicio: Data inicial que se deseja obter os dados
    :param data_fim: Data final que se deseja obter os dados
    :return: Os dados de um município específico dentro do intervalo passados pelo usuário
    '''


@app.route('api/estado')
def estados():
    '''
    :return: todos os dados da base de dados por estado
    '''


@app.route('api/estado/uf=<str:uf>')
def estado(uf):
    '''
    :param uf: sigla da UF
    :return: todos os dados da base de um estado específico
    '''


@app.route('api/estado/inicio=<str:data_inicio>&fim=<str:data_fim>')
def estado_data(data_inicio, data_fim):
    '''
    :param data_inicio: Data inicial que se deseja obter os dados
    :param data_fim: Data final que se deseja obter os dados
    :return: Todos os dados da base de dados dos estados em um determinado intervalo de tempo
    '''


@app.route('api/estado/uf=<str:uf>/inicio=<str:data_inicio>&fim=<str:data_fim>')
def estado_data(uf, data_inicio, data_fim):
    '''
    :param uf: siga da UF
    :param data_inicio: todos os dados da base de um estado específico
    :param data_fim: Data final que se deseja obter os dados
    :return: Os dados de um município específico dentro do intervalo passados pelo usuário
    '''


if __name__ == '__main__':
    app.run()
