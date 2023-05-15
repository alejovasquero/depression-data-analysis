import plotly.express as px
from dash import Dash, dcc, html

from src.data import data_consumption


def by_age_plot():
    df = data_consumption.obtain_file_as_dataframe(
        file="depression_anxiety_data.csv",
        directory="../../data",
        delimiter=","
    )

    # Initialize the app
    app = Dash(__name__)

    diagnosed = df.query('depression_diagnosis == True')

    not_diagnosed = df.query('depression_diagnosis == False')

    fig_diag = px.box(diagnosed, x="age", y="bmi")
    fig_not_diag = px.box(not_diagnosed, x="age", y="bmi")

    # App layout
    app.layout = html.Div([
        html.H1(children='Body mass index comparison'),
        html.H2(children='Diagnosed sample'),
        dcc.Graph(figure=fig_diag, id="bar_plot_diag"),
        html.H2(children='Not Diagnosed sample'),
        dcc.Graph(figure=fig_not_diag, id="bar_plot_not_diag"),
    ])

    if __name__ == '__main__':
        app.run_server(debug=True, port="8082")


if __name__ == "__main__":
    by_age_plot()
