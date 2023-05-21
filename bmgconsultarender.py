
from zeep import Client
import logging
logging.getLogger('zeep.wsdl.bindings.soap').setLevel(logging.ERROR)
from openpyxl import Workbook
from flask import Flask

app = Flask(__name__)


import pandas as pd
contatos_df = pd.read_excel("bmgconsulta.xlsx")




for i, cpf2 in enumerate(contatos_df['cpf']):

    cpf = str(cpf2)

    username = 'vitor.helpvix'
    password = '70da6fe%'
    codigoEntidade = 1581

    client = Client('https://ws1.bmgconsig.com.br/webservices/SaqueComplementar?wsdl')

    entrada = {
      'login': username,
      'senha': password,
      'codigoEntidade': codigoEntidade,
      'cpf': cpf,


    }
    # Aqui você pode chamar as operações disponíveis no Web Service
    result = client.service.buscarCartoesDisponiveis(entrada)

    # Imprimir o resultado da operação
    #print(result)
    cartoesRetorno = result.cartoesRetorno
    #numeroContaInterna = cartoesRetorno.numeroContaInterna
    #print(cartoesRetorno)
    numeroContaInterna = cartoesRetorno[0]['numeroContaInterna']
    for i in range(3):
        try:
            numeroContaInterna = cartoesRetorno[i]['numeroContaInterna']
            #print(numeroContaInterna)

        except:
            break
    #print(i)

        #print(cpf2, 'cliente possui dois beneficios')
    for i in range(2):
        numeroContaInterna = cartoesRetorno[i]['numeroContaInterna']
        with client.settings(strict=False):
            entrada = {
                'login': username,
                'senha': password,
                'codigoEntidade': '1581',
                'cpf': cpf,
                'numeroContaInterna': numeroContaInterna,
                'tipoSaque': 1,
                'cpfImpedidoComissionar': False
            }
            result = client.service.buscarLimiteSaque(entrada)
            #print(result)

            valorSaqueMaximo = result.valorSaqueMaximo
            valorSaqueMaximo = str(valorSaqueMaximo).replace(".", ",")
#             if valorSaqueMaximo == 0:
#                 pass
#             else:
            print(cpf2, valorSaqueMaximo)




            




if __name__ == '__main__':
    app.run()
