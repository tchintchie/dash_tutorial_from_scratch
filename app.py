import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

ext_ccs = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
ext_css1 = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

df = pd.read_csv("lex.csv")

markdown_text = """
This is a markdown text... blabla
I´m very excited about Dash and Python
web visualization :-)

"""

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
    dcc.Markdown(children=markdown_text),
    html.Label("Dropdown"),
    dcc.Dropdown(
        options=[
            {"label":"New York City","value":"NYC"},
            {"label":"Tokyo","value":"TYO"},
            {"label":"Imst","value":"IM"}
        ],
        value="MTL"
    ),
    html.Label("Multi Select Dropdown"),
    dcc.Dropdown(
        options=[
            {"label":"New York City","value":"NYC"},
            {"label":"Tokyo","value":"TYO"},
            {"label":"Imst","value":"IM"}
        ],
        value=["TYO","IM"],
        multi=True
    ),
    html.Label("Radio Items"),
    dcc.RadioItems(
        options=[
            {"label": "New York City", "value": "NYC"},
            {"label": "Tokyo", "value": "TYO"},
            {"label": "Imst", "value": "IM"}
        ],
        value="TYO"
    ),
    html.Label("Checkboxes"),
    dcc.Checklist(
        options=[
            {"label":"New York City","value":"NYC"},
            {"label":"Tokyo","value":"TYO"},
            {"label":"Imst","value":"IM"}
        ],
        value=["TYO","IM"]
    ),
    html.Label("Text Input"),
    dcc.Input(value="IM",type="text"),
    html.Label("Slider"),
    dcc.Slider(
        min=0,
        max=9,
        marks={i:"Label {}".format(i) if i == 1 else str(i) for i in range(1,6)},
        value=5,
    ),


    dcc.Graph(
        id="sample_graph",
        figure={
            "data": [
                dict(
                    x=df[df.continent==i]["gdp per capita"],
                    y=df[df.continent==i]["life expectancy"],
                    text=df[df.continent==i]["country"],
                    mode="markers",
                    opacity=0.7,
                    marker={
                        "size":15,
                        "line":{"width":0.5, "color":"white"}
                    },
                    name=i
                )for i in df.continent.unique()
            ],
            "layout": dict(
                xaxis={"type":"log","title":"GDP per Capita"},
                yaxis={"title":"Life Expectancy"},
                margin={"l":40,"b":40,"t":10,"r":10},
                legend={"x":0,"y":1},
                hovermode="closest"
            )
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
#todo: https://dash.plot.ly/getting-started continue from there