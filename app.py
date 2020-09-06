from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tabelas.db'
app.config['JSON_AS_ASCII'] = False
db.init_app(app)
api = Api(app)


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
        pass


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
        pass


class EstadoByUFDataF(Resource):
    def get(self, uf, data_fim, page_num):
        pass


class EstadoByUFDataIF(Resource):
    def get(self, uf, data_inicio, data_fim, page_num):
        pass


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
        pass


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
        except:
            return jsonify({"erro": "Data inválida, verifique a documentação da API."}), 422

        q1 = Municipio.query.filter_by(sigla_UF=uf.upper()
                                       ).filter(Municipio.ano > ano)

        q2 = Municipio.query.filter_by(sigla_UF=uf.upper()
                                      ).filter(Municipio.ano == ano
                                               ).filter(Municipio.mes >= mes)

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
        pass


# Rotas Igor
# Concluídas
api.add_resource(MunByUFDataF, '/municipio/uf=<uf>/fim=<data_fim>/page=<page_num>')

# Não concluídas
api.add_resource(MunByUFDataI, '/municipio/uf=<uf>/inicio=d<ata_inicio>/page=<page_num>')
api.add_resource(MunByUFDataIF, '/municipio/uf=<uf>/inicio=<data_inicio>&fim=<data_fim>/page=<page_num>')

api.add_resource(EstadoByUFDataI, '/estado/uf=<uf>/inicio=<data_inicio>/page=<page_num>')
api.add_resource(EstadoByUFDataF, '/estado/uf=<uf>/fim=<data_fim>/page=<page_num>')
api.add_resource(EstadoByUFDataIF, '/estado/uf=<uf>/inicio=<data_inicio>&fim=<data_fim>/page=<page_num>')

# Ruan
# Concluídas
api.add_resource(AllMuns, '/municipio/page=<page_num>')

# Não Concluídas
api.add_resource(MunByUF, '/municipio/uf=<uf>/page=<page_num>')
api.add_resource(EstadosByUF, '/estado/uf=<uf>/page=<page_num>')

# Não Concluídas

# Fabrício
# Concluídas
api.add_resource(AllEstados, '/estado/page=<page_num>')

# Não Concluídas
api.add_resource(MunByDataI, '/municipio/uf=<uf>/inicio=<data_inicio>/page=<page_num>')
api.add_resource(MunByDataF, '/municipio/uf=<uf>/fim=<data_fim>/page=<page_num>')
api.add_resource(MunByDataIF, '/municipio/uf=<uf>/inicio=<data_inicio>&fim=<data_fim>/page=<page_num>')
api.add_resource(EstadoByDataI, '/estado/inicio=<data_inicio>/page=<page_num>')
api.add_resource(EstadoByDataF, '/estado/fim=<data_fim>/page=<page_num>')
api.add_resource(EstadoByDataIF, '/estado/inicio=<data_inicio>&fim=<data_fim>/page=<page_num>')


if __name__ == '__main__':
    app.run(debug=True)
