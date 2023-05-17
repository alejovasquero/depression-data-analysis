import plotly.express as px
from dash import Dash, dcc, html

from src.data import data_consumption


def by_age_plot():
    df = data_consumption.obtain_file_as_dataframe(
        file="depression_anxiety_data.csv",
        directory="../../data",
        delimiter=","
    )

    # Initialize the appe
    app = Dash(__name__)

    df = df.query('depression_diagnosis == True')

    fig = px.pie(df, names='anxiousness', title="Anxiety (not diagnosed) and depression")

    anxiety_severity = df.query('anxiousness == True')

    fig_severity = px.pie(anxiety_severity, names='anxiety_severity', title="Anxiety (not diagnosed) and depression")

    # App layout
    app.layout = html.Div([
        html.H1(children='Anxiety (not diagnosed) and depression'),
        dcc.Graph(figure=fig, id="pie_plot"),
        html.H1(children='Anxiety severity'),
        dcc.Graph(figure=fig_severity, id="pie_plot_severity"),
    ])

    if __name__ == '__main__':
        app.title = "Anxiety and depression"
        app.run_server(debug=True, port="8083")


if __name__ == "__main__":
    by_age_plot()
