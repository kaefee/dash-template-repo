from dash_labs.plugins.pages import register_page

register_page(__name__, path="/heatmaps")

from dash import  dcc, html, Input, Output, callback
import plotly.express as px

df = px.data.medals_wide(indexed=True)

layout = html.Div(
    [
        html.P("Medals included:"),
        dcc.Dropdown(
                    id="heatmaps-medals",
                    options=[
                        {"label": "GOLD", "value": "gold"},
                        {"label": "SILVER", "value": "silver"},
                        {"label": "BRONZE", "value": "bronze"},
                    ],
                    value=['gold', 'silver', 'bronze'],
                    multi = True
                ),
        dcc.Graph(id="heatmaps-graph"),
    ]
)


@callback(
    Output("heatmaps-graph", "figure"), 
    Input("heatmaps-medals", "value"))
def filter_heatmap(cols):
    fig = px.imshow(df[cols])
    return fig