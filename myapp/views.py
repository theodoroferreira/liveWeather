from django.http import JsonResponse
from rethinkdb import r
from .models import RealTimeData
import pandas as pd


def get_connection():
    try:
        conn = r.connect(host='10.41.20.16',
                         port=58015,
                         db='santa_rosa',
                         user='theodoro.ferreira@sou.unijui.edu.br',
                         password='DS3hs7k28fj')

        estacoes_metereologicas = 'estacoes_metereologicas'
        estacoes_metereologicas = r.table(estacoes_metereologicas).run(conn)

        conn.close()

        return estacoes_metereologicas

    except Exception as e:
        print(f"Ocorreu um erro ao executar o script: {e}")


def get_data():

    estacoes_metereologicas = get_connection()

    df = pd.DataFrame(list(estacoes_metereologicas))

    return df.to_json(orient='records')


def show_real_time_data(request):
    data = RealTimeData.objects.all()
    data_list = []
    for item in data:
        data_list.append({
            'data_field_1': item.data_field_1,
            'data_field_2': item.data_field_2,
            # Add more fields as needed
        })

    return JsonResponse({'real_time_data': data_list})
