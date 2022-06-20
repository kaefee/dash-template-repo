import dash_bootstrap_components as dbc
from dash import html
from dash_labs.plugins.pages import register_page


register_page(__name__, path="/404")

layout = dbc.Row([
    dbc.Col([
        dbc.Row(["404"], className= "flex-fill bigtextgray"),
        dbc.Row(["Where is my dash?"], className= "flex-fill ")
    ], md=6, className = "d-flex display-4 align-self-center flex-column align-items-end"),
    dbc.Col([
        html.Img(src='/assets/404.png')
    ], md=6,  className = "d-flex align-items-center display-6 justify-content-start")

])
