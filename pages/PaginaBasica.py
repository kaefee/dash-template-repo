#libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page


# dash-labs plugin call, menu name and route
register_page(__name__, path="/basicpage")

from components.maps.mapsample import mapsample

mapa_ejemplo = mapsample('This is my custom map', 'div_samplemap')

# specific layout for this page
layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                 html.H1(['Page Title'],id="div_title_maps"),
                 mapa_ejemplo.display()

            ], lg=12), 
           
        ]),
        ]
)