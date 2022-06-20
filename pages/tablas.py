import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

from components.table.table import *
from components.sampledf.model import df_costos, df_opsales

data = df_costos
data2 = df_opsales

register_page(__name__, path="/tablas")

params1 = {
            'title': 'Users', 
            'description': 'Tabla de lista de usuarios',
            'columns': ['ID', 'CIUDAD', 'TIPO', 'FECHA']
}

params2 = {
            'title': 'Municipios', 
            'description': 'Tabla de lista de municipios',
            'columns': ['Type','Sales per customer','Delivery Status','Category Name']
            
}


tablausuarios = table(data,params1)
tablamunicipios = table(data2, params2)

layout= dbc.Container([
    dbc.Row([
        dbc.Col([         
            tablamunicipios.display()
        ])
    ], className= "card"),
    dbc.Row([
        dbc.Col([
            tablausuarios.display()
        ])
    ], className= "card"),
])