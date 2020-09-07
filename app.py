import csv
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
app.config['JSON_AS_ASCII'] = False
db.init_app(app)
api = Api(app)


'''
# SCRIPT DE POVOAMENTO DO BANCO DE DADOS


@app.route("/povoa_bd")
def povoa_bd():
    with app.app_context():
        db.create_all()
    f = open("data/dados_mun.csv", encoding='utf-8')
    g = open("data/dados_uf.csv", encoding='utf-8')
    dataf = csv.reader(f)
    datag = csv.reader(g)

    id = 1

    for nome, tipo_crime, ano, mes, vitimas, ocorrencias, uf in datag:
        e = Estado(id=id,
                   sigla_UF=uf,
                   estado=nome,
                   crime=tipo_crime,
                   ano=ano,
                   mes=mes,
                   vitimas=vitimas,
                   ocorrencias=ocorrencias)
        db.session.add(e)
        id = id + 1

    id = 1
    for municipio, uf, regiao, vitimas, mes, ano in dataf:
        m = Municipio(id=id,
                      municipio=municipio,
                      sigla_UF=uf,
                      regiao=regiao,
                      vitimas=vitimas,
                      mes=mes,
                      ano=int("20"+str(ano)))

        db.session.add(m)
        id = id + 1
    db.session.commit()

    return "Success"
'''

# Retorna todos os dados de estados


class AllEstados(Resource):
    def get(self, page_num):
        ests = Estado.query.paginate(per_page=100, page=int(page_num))

        results = []
        for item in ests.items:
            temp = {"estado": item.estado,
                    "crime": item.crime,
                    "mes_ano": f"{item.mes}-{item.ano}",
                    "vitimas": item.vitimas,
                    "ocorrencias": item.ocorrencias}

            results.append(temp)

        num_items = len(results)

        if ests.has_next:
            next_page = ests.next_num
        else:
            next_page = None

        if ests.has_prev:
            prev_page = ests.prev_num
        else:
            prev_page = None

        return jsonify({"has_next": ests.has_next,
                        "next_page": next_page,
                        "has_prev": ests.has_prev,
                        "prev_page": prev_page,
                        "num_items": num_items,
                        "total_results": ests.total,
                        "num_pages": ests.pages,
                        "results": results})


class EstadosByUF(Resource):
    def get(self, uf, page_num):
        q1 = Estado.query.filter_by(sigla_UF=uf.upper())
        e = q1
        ests = e.paginate(per_page=100, page=int(page_num))

        results = []
        for item in ests.items:
            temp = {"estado": item.estado,
                    "crime": item.crime,
                    "mes_ano": f"{item.mes}-{item.ano}",
                    "vitimas": item.vitimas,
                    "ocorrencias": item.ocorrencias}

            results.append(temp)

        num_items = len(results)

        if ests.has_next:
            next_page = ests.next_num
        else:
            next_page = None

        if ests.has_prev:
            prev_page = ests.prev_num
        else:
            prev_page = None

        return jsonify({"has_next": ests.has_next,
                        "next_page": next_page,
                        "has_prev": ests.has_prev,
                        "prev_page": prev_page,
                        "num_items": num_items,
                        "total_results": ests.total,
                        "num_pages": ests.pages,
                        "results": results})


class EstadoByDataI(Resource):
    def get(self, data_inicio, page_num):
        pass


class EstadoByDataF(Resource):
    def get(self, data_fim, page_num):
        pass


class EstadoByDataIF(Resource):
    def get(self, data_inicio, data_fim, page_num):
        pass


class EstadoByUFDataI(Resource):
    def get(self, uf, data_inicio, page_num):
        try:
            mes = int(data_inicio.split("-")[0])
            ano = int(data_inicio.split("-")[1])

            if mes < 1 or mes > 12:
                return jsonify({"erro": "Data inválida, verifique a documentação da API."}), 422

        except:
            return jsonify({"erro": "Data inválida, verifique a documentação da API."}), 422

        q1 = Estado.query.filter_by(sigla_UF=uf.upper()
                                    ).filter(Estado.ano == ano
                                             ).filter(Estado.mes >= mes)

        q2 = Estado.query.filter_by(sigla_UF=uf.upper()
                                    ).filter(Estado.ano > ano)

        e = q1.union_all(q2)

        ests = e.paginate(per_page=100, page=int(page_num))

        results = []
        for item in ests.items:
            temp = {"estado": item.estado,
                    "sigla_UF": item.sigla_UF,
                    "tipo_crime": item.crime,
                    "mes_ano": f"{item.mes}-{item.ano}",
                    "vitimas": item.vitimas,
                    "ocorrencias": item.ocorrencias}

            results.append(temp)

        num_items = len(results)

        if ests.has_next:
            next_page = ests.next_num
        else:
            next_page = None

        if ests.has_prev:
            prev_page = ests.prev_num
        else:
            prev_page = None

        return jsonify({"has_next": ests.has_next,
                        "next_page": next_page,
                        "has_prev": ests.has_prev,
                        "prev_page": prev_page,
                        "num_items": num_items,
                        "total_results": ests.total,
                        "num_pages": ests.pages,
                        "results": results})


class EstadoByUFDataF(Resource):
    def get(self, uf, data_fim, page_num):
        try:
            mes = int(data_fim.split("-")[0])
            ano = int(data_fim.split("-")[1])

            if mes < 1 or mes > 12:
                return jsonify({"erro": "Data inválida, verifique a documentação da API."}), 422

        except:
            return jsonify({"erro": "Data inválida, verifique a documentação da API."}), 422

        q1 = Estado.query.filter_by(sigla_UF=uf.upper()
                                    ).filter(Estado.ano < ano)

        q2 = Estado.query.filter_by(sigla_UF=uf.upper()
                                    ).filter(Estado.ano == ano
                                             ).filter(Estado.mes <= mes)

        e = q1.union_all(q2)

        ests = e.paginate(per_page=100, page=int(page_num))

        results = []
        for item in ests.items:
            temp = {"estado": item.estado,
                    "sigla_UF": item.sigla_UF,
                    "tipo_crime": item.crime,
                    "mes_ano": f"{item.mes}-{item.ano}",
                    "vitimas": item.vitimas,
                    "ocorrencias": item.ocorrencias}

            results.append(temp)

        num_items = len(results)

        if ests.has_next:
            next_page = ests.next_num
        else:
            next_page = None

        if ests.has_prev:
            prev_page = ests.prev_num
        else:
            prev_page = None

        return jsonify({"has_next": ests.has_next,
                        "next_page": next_page,
                        "has_prev": ests.has_prev,
                        "prev_page": prev_page,
                        "num_items": num_items,
                        "total_results": ests.total,
                        "num_pages": ests.pages,
                        "results": results})


class EstadoByUFDataIF(Resource):
    def get(self, uf, data_inicio, data_fim, page_num):
        try:
            mes_inicio = int(data_inicio.split("-")[0])
            ano_inicio = int(data_inicio.split("-")[1])
            mes_fim = int(data_fim.split("-")[0])
            ano_fim = int(data_fim.split("-")[1])

            if mes_inicio < 1 or mes_inicio > 12 or mes_fim < 1 or mes_inicio > 12:
                return jsonify({"erro": "Data inválida, verifique a documentação da API."}), 422

        except:
            return jsonify({"erro": "Data inválida, verifique a documentação da API."}), 422

        q1 = Estado.query.filter_by(sigla_UF=uf.upper()
                                    ).filter(Estado.ano == ano_inicio
                                             ).filter(Estado.mes >= mes_inicio)

        q2 = Estado.query.filter_by(sigla_UF=uf.upper()
                                    ).filter(Estado.ano > ano_inicio
                                             ).filter(Estado.ano < ano_fim)

        q3 = Estado.query.filter_by(sigla_UF=uf.upper()
                                    ).filter(Estado.ano == ano_fim
                                             ).filter(Estado.mes <= mes_fim)

        e = q1.union_all(q2).union_all(q3)

        ests = e.paginate(per_page=100, page=int(page_num))

        results = []
        for item in ests.items:
            temp = {"estado": item.estado,
                    "sigla_UF": item.sigla_UF,
                    "tipo_crime": item.crime,
                    "mes_ano": f"{item.mes}-{item.ano}",
                    "vitimas": item.vitimas,
                    "ocorrencias": item.ocorrencias}

            results.append(temp)

        num_items = len(results)

        if ests.has_next:
            next_page = ests.next_num
        else:
            next_page = None

        if ests.has_prev:
            prev_page = ests.prev_num
        else:
            prev_page = None

        return jsonify({"has_next": ests.has_next,
                        "next_page": next_page,
                        "has_prev": ests.has_prev,
                        "prev_page": prev_page,
                        "num_items": num_items,
                        "total_results": ests.total,
                        "num_pages": ests.pages,
                        "results": results})


class AllMuns(Resource):
    def get(self, page_num):
        muns = Municipio.query.paginate(per_page=100, page=int(page_num))

        results = []
        for item in muns.items:
            temp = {"municipio": item.municipio,
                    "Sigla_UF": item.sigla_UF,
                    "Regiao": item.regiao,
                    "mes_ano": f"{item.mes}-{item.ano}",
                    "vitimas": item.vitimas}

            results.append(temp)

        num_items = len(results)

        if muns.has_next:
            next_page = muns.next_num
        else:
            next_page = None

        if muns.has_prev:
            prev_page = muns.prev_num
        else:
            prev_page = None

        return jsonify({"has_next": muns.has_next,
                        "next_page": next_page,
                        "has_prev": muns.has_prev,
                        "prev_page": prev_page,
                        "num_items": num_items,
                        "total_results": muns.total,
                        "num_pages": muns.pages,
                        "results": results})


class MunByUF(Resource):
    def get(self, uf, page_num):

        q1 = Municipio.query.filter_by(sigla_UF=uf.upper())

        muns = q1.paginate(per_page=100, page=int(page_num))

        results = []
        for item in muns.items:
            temp = {"municipio": item.municipio,
                    "sigla_UF": item.sigla_UF,
                    "regiao": item.regiao,
                    "mes_ano": f"{item.mes}-{item.ano}",
                    "vitimas": item.vitimas}
            results.append(temp)

        num_items = len(results)

        if muns.has_next:
            next_page = muns.next_num
        else:
            next_page = None

        if muns.has_prev:
            prev_page = muns.prev_num
        else:
            prev_page = None

        return jsonify({"has_next": muns.has_next,
                        "next_page": next_page,
                        "has_prev": muns.has_prev,
                        "prev_page": prev_page,
                        "num_items": num_items,
                        "total_results": muns.total,
                        "num_pages": muns.pages,
                        "results": results})


class MunByDataI(Resource):
    def get(self, data_inicio, page_num):
        pass


class MunByDataF(Resource):
    def get(self, data_fim, page_num):
        pass


class MunByDataIF(Resource):
    def get(self, data_inicio, data_fim, page_num):
        pass


class MunByUFDataI(Resource):
    def get(self, uf, data_inicio, page_num):
        try:
            mes = int(data_inicio.split("-")[0])
            ano = int(data_inicio.split("-")[1])

            if mes < 1 or mes > 12:
                return jsonify({"erro": "Data inválida, verifique a documentação da API."}), 422

        except:
            return jsonify({"erro": "Data inválida, verifique a documentação da API."}), 422

        q1 = Municipio.query.filter_by(sigla_UF=uf.upper()
                                       ).filter(Municipio.ano == ano
                                                ).filter(Municipio.mes >= mes)

        q2 = Municipio.query.filter_by(sigla_UF=uf.upper()
                                       ).filter(Municipio.ano > ano)

        m = q1.union_all(q2)

        muns = m.paginate(per_page=100, page=int(page_num))

        results = []
        for item in muns.items:
            temp = {"municipio": item.municipio,
                    "sigla_UF": item.sigla_UF,
                    "regiao": item.regiao,
                    "mes_ano": f"{item.mes}-{item.ano}",
                    "vitimas": item.vitimas}
            results.append(temp)

        num_items = len(results)

        if muns.has_next:
            next_page = muns.next_num
        else:
            next_page = None

        if muns.has_prev:
            prev_page = muns.prev_num
        else:
            prev_page = None

        return jsonify({"has_next": muns.has_next,
                        "next_page": next_page,
                        "has_prev": muns.has_prev,
                        "prev_page": prev_page,
                        "num_items": num_items,
                        "total_results": muns.total,
                        "num_pages": muns.pages,
                        "results": results})


class MunByUFDataF(Resource):
    def get(self, uf, data_fim, page_num):
        try:
            mes = int(data_fim.split("-")[0])
            ano = int(data_fim.split("-")[1])

            if mes < 1 or mes > 12:
                return jsonify({"erro": "Data inválida, verifique a documentação da API."}), 422

        except:
            return jsonify({"erro": "Data inválida, verifique a documentação da API."}), 422

        q1 = Municipio.query.filter_by(sigla_UF=uf.upper()
                                       ).filter(Municipio.ano < ano)

        q2 = Municipio.query.filter_by(sigla_UF=uf.upper()
                                       ).filter(Municipio.ano == ano
                                                ).filter(Municipio.mes <= mes)

        m = q1.union_all(q2)

        muns = m.paginate(per_page=100, page=int(page_num))

        results = []
        for item in muns.items:
            temp = {"municipio": item.municipio,
                    "sigla_UF": item.sigla_UF,
                    "regiao": item.regiao,
                    "mes_ano": f"{item.mes}-{item.ano}",
                    "vitimas": item.vitimas}
            results.append(temp)

        num_items = len(results)

        if muns.has_next:
            next_page = muns.next_num
        else:
            next_page = None

        if muns.has_prev:
            prev_page = muns.prev_num
        else:
            prev_page = None

        return jsonify({"has_next": muns.has_next,
                        "next_page": next_page,
                        "has_prev": muns.has_prev,
                        "prev_page": prev_page,
                        "num_items": num_items,
                        "total_results": muns.total,
                        "num_pages": muns.pages,
                        "results": results})


class MunByUFDataIF(Resource):
    def get(self, uf, data_inicio, data_fim, page_num):
        try:
            mes_inicio = int(data_inicio.split("-")[0])
            ano_inicio = int(data_inicio.split("-")[1])
            mes_fim = int(data_fim.split("-")[0])
            ano_fim = int(data_fim.split("-")[1])

            if mes_inicio < 1 or mes_inicio > 12 or mes_fim < 1 or mes_inicio > 12:
                return jsonify({"erro": "Data inválida, verifique a documentação da API."}), 422

        except:
            return jsonify({"erro": "Data inválida, verifique a documentação da API."}), 422

        q1 = Municipio.query.filter_by(sigla_UF=uf.upper()
                                       ).filter(Municipio.ano == ano_inicio
                                                ).filter(Municipio.mes >= mes_inicio)

        q2 = Municipio.query.filter_by(sigla_UF=uf.upper()
                                       ).filter(Municipio.ano > ano_inicio
                                                ).filter(Municipio.ano < ano_fim)

        q3 = Municipio.query.filter_by(sigla_UF=uf.upper()
                                       ).filter(Municipio.ano == ano_fim
                                                ).filter(Municipio.mes <= mes_fim)

        m = q1.union_all(q2).union_all(q3)

        muns = m.paginate(per_page=100, page=int(page_num))

        results = []
        for item in muns.items:
            temp = {"municipio": item.municipio,
                    "sigla_UF": item.sigla_UF,
                    "regiao": item.regiao,
                    "mes_ano": f"{item.mes}-{item.ano}",
                    "vitimas": item.vitimas}
            results.append(temp)

        num_items = len(results)

        if muns.has_next:
            next_page = muns.next_num
        else:
            next_page = None

        if muns.has_prev:
            prev_page = muns.prev_num
        else:
            prev_page = None

        return jsonify({"has_next": muns.has_next,
                        "next_page": next_page,
                        "has_prev": muns.has_prev,
                        "prev_page": prev_page,
                        "num_items": num_items,
                        "total_results": muns.total,
                        "num_pages": muns.pages,
                        "results": results})


# Rotas Igor
# Concluídas
api.add_resource(
    MunByUFDataF, '/municipio/uf=<uf>/fim=<data_fim>/page=<page_num>')

api.add_resource(
    MunByUFDataI, '/municipio/uf=<uf>/inicio=<data_inicio>/page=<page_num>')
api.add_resource(
    MunByUFDataIF, '/municipio/uf=<uf>/inicio=<data_inicio>&fim=<data_fim>/page=<page_num>')

api.add_resource(
    EstadoByUFDataI, '/estado/uf=<uf>/inicio=<data_inicio>/page=<page_num>')
api.add_resource(
    EstadoByUFDataF, '/estado/uf=<uf>/fim=<data_fim>/page=<page_num>')
api.add_resource(EstadoByUFDataIF,
                 '/estado/uf=<uf>/inicio=<data_inicio>&fim=<data_fim>/page=<page_num>')

# Ruan
# Concluídas
api.add_resource(AllMuns, '/municipio/page=<page_num>')
api.add_resource(MunByUF, '/municipio/uf=<uf>/page=<page_num>')
api.add_resource(EstadosByUF, '/estado/uf=<uf>/page=<page_num>')
# Não Concluídas

# Fabrício
# Concluídas
api.add_resource(AllEstados, '/estado/page=<page_num>')

# Não Concluídas
api.add_resource(
    MunByDataI, '/municipio/uf=<uf>/inicio=<data_inicio>/page=<page_num>')
api.add_resource(
    MunByDataF, '/municipio/uf=<uf>/fim=<data_fim>/page=<page_num>')
api.add_resource(
    MunByDataIF, '/municipio/uf=<uf>/inicio=<data_inicio>&fim=<data_fim>/page=<page_num>')
api.add_resource(EstadoByDataI, '/estado/inicio=<data_inicio>/page=<page_num>')
api.add_resource(EstadoByDataF, '/estado/fim=<data_fim>/page=<page_num>')
api.add_resource(
    EstadoByDataIF, '/estado/inicio=<data_inicio>&fim=<data_fim>/page=<page_num>')


if __name__ == '__main__':
    app.run(debug=True)
