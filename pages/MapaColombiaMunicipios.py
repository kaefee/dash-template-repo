#libraries
import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from components.maps.mapcol_municipios import mapcol_municipios


from components.sampledf.model import df_costos
from components.sampledf.model import df_markers

dash.register_page(__name__, path="/mapa_municipios")

mapa_colombia_municipios = mapcol_municipios('Mapa municipios Colombia', 'id_figura_mapa_colombia',df_costos, df_markers)

layout= html.Div(
    [
        dbc.Row([
            dbc.Col([
                 html.H1("Mapas", className='title ml-2'),
            ])
           
        ]),
        dbc.Row([
            dbc.Col([
                mapa_colombia_municipios.display()
            ])
        ], className= "card")
    ], className='container-fluid', style={'margin': 'auto', 'width':'100%'}
) 
