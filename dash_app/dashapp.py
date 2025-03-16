import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go  # Используем graph_objects вместо express
import requests
import logging

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)

# URL API Django-приложения
DJANGO_API_URL = "http://127.0.0.1:8000/posts/"

# Загружаем данные из Django-приложения
def fetch_data():
    try:
        response = requests.get(DJANGO_API_URL)
        logging.debug(f"Response status code: {response.status_code}")
        if response.status_code == 200:
            return response.json()
        return []
    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        return []

# Создаем Dash-приложение
app = dash.Dash(__name__)

# Макет приложения
app.layout = html.Div([
    html.H1("Визуализация данных постов"),
    dcc.Graph(id='posts-graph'),
    dcc.Interval(
        id='interval-component',
        interval=60*1000,  # Обновление каждую минуту
        n_intervals=0
    )
])

# Callback для обновления графика
@app.callback(
    Output('posts-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    data = fetch_data()
    if data:
        try:
            # Пример: строим график по количеству постов и авторам
            authors = [item["author"]["username"] for item in data]
            titles = [item["title"] for item in data]
            created_at = [item["created_at"] for item in data]

            fig = go.Figure(data=[
                go.Bar(x=authors, y=created_at, text=titles, name="Посты")
            ])
            fig.update_layout(title="Посты по авторам", xaxis_title="Автор", yaxis_title="Дата создания")
            return fig
        except Exception as e:
            logging.error(f"Error updating graph: {e}")
            return {}
    return {}

# Запуск приложения
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8051, debug=True)
