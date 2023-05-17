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

    df = df.query('depressiveness == False or depression_diagnosis == True')

    df = df.groupby(["age", "depressiveness"]).size().reset_index(name="Count")

    fig = px.bar(df, x="age",y="Count" ,color="depressiveness", title="General depressiveness and diagnosis")

    # App layout
    app.layout = html.Div([
        html.H1(children='Depression diagnosis by age'),
        dcc.Graph(figure=fig, id="bar_plot"),
    ])

    if __name__ == '__main__':
        app.title = "Depression diagnosis by age"
        app.run_server(debug=True, port="8081")


if __name__ == "__main__":
    by_age_plot()
