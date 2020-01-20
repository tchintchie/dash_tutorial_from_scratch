import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

ext_ccs = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
ext_css1 = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

df = pd.read_csv('clean_diabetes.csv')


def generate_table(df, max_rows=10):
    return html.Table(
        # header
        [html.Tr([html.Th(col) for col in df.columns])] +

        # body
        [html.Tr([
            html.Td(df.iloc[i][col]) for col in df.columns
        ]) for i in range(min(len(df), max_rows))]
    )


app = dash.Dash(__name__, external_stylesheets=ext_css1)

colors = {
    "background": "#111111",
    "text": "#7fdbff"
}

app.layout = html.Div(style={"backgroundColor": colors["background"]}, children=[
    html.H4(children="US Diabetes Stats"),
    generate_table(df),
    html.H1(children="Hello Dash",
            style={
                "textAlign": "center",
                "color": colors["text"]
            }),
    html.Div(style={"textAlign": "center", "color": colors["text"]}, children="""
    Dash: A web Application framework for Python.
    
    """),
    dcc.Graph(
        id="sample_graph",
        figure={
            "data": [
                {"x": [1, 3, 2, 5, 6], "y": [5, 5, 6, 2, 3], "type": "bar", "name": "Imst"},
                {"x": [12, 4, 5, 5, 6], "y": [6, 9, 1, 5, 6], "type": "bar", "name": "Innsbruck"},
            ],
            "layout": {
                "plot_bgcolor": colors["background"],
                "paper_bgcolor": colors["background"],
                "font": {"color": colors["text"]},
                "title": "Dash Sample Data Viz"

            }
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
#todo: https://dash.plot.ly/getting-started continue from there