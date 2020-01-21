import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import dash_table

df = pd.read_csv("clean_diabetes.csv")
app = dash.Dash(__name__)

app.layout = html.Div(children=[
               html.Header("Hello and welcome to my CSS Bootstrap Dash Test"),
               html.H1("My Name is Marina"),
               html.Div(
                   html.Article("lorem ipsumd blakshd  alkjwehaiwuehasjbc aasdhfiauhwejbgdhc"),
                   html.Article(df.head())
               )

])


if __name__ == "__main__":
    app.run_server(debug=True)