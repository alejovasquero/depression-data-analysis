import plotly.express as px
from dash import Dash, dcc, html

from src.data import data_consumption


def treatment():
    df = data_consumption.obtain_file_as_dataframe(
        file="depression_anxiety_data.csv",
        directory="../../data",
        delimiter=","
    )

    # Initialize the appe
    app = Dash(__name__)

    anxiety = df.query('anxiety_diagnosis == True')
    depression = df.query('depression_diagnosis == True')

    fig_anxiety = px.pie(anxiety, names='anxiety_treatment', title="Anxiety Depression treatment ratio")
    fig_depression = px.pie(depression, names='depression_treatment', title="Depression treatment ratio")

    # App layout
    app.layout = html.Div([
        html.Title("Depression and anxiety treatment"),
        html.H1(children='Anxiety treatment'),
        dcc.Graph(figure=fig_anxiety, id="pie_plot"),
        html.H1(children='Depression severity'),
        dcc.Graph(figure=fig_depression, id="pie_plot_severity"),
    ])

    if __name__ == '__main__':
        app.title = "Depression and anxiety treatment"
        app.run_server(debug=True, port="8084")


if __name__ == "__main__":
    treatment()
