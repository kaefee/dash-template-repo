#libraries
import dash
from dash import html , dcc
import dash_bootstrap_components as dbc

# dash-labs plugin call, menu name and route
dash.register_page(__name__, path="/historytelling")

from components.maps.mapsample import mapsample
from components.markdown.markformat import markformat

texto1  = markformat('label', '*some markdown* $\phi$')

# specific layout for this page
layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                 html.H1(['Page Title'],id="div_title_maps"),
                 texto1.show()

            ], lg=12), 
           
        ]),
        ]
)