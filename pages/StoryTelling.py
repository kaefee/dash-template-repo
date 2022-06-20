#libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

# dash-labs plugin call, menu name and route
register_page(__name__, path="/storytelling")

from components.markdown.markformat import markformat
from components.maps.mapsample import mapsample

file1 = open('./data/mdsamples/story1.md')
file2 = open('./data/mdsamples/story2.md')

texto1  = markformat('Citizenship', file1.read())
texto2  = markformat('Global Diversity', file2.read())

mapa_ejemplo_story = mapsample('Mapa elecciones', 'id_mapa_story1')


# specific layout for this page
layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                 html.H1(['Pages Title'],id="div_title_maps"),
                 html.Hr()
            ], lg=12), 
           
        ]),

        dbc.Row([
            dbc.Col([
                 texto1.show()

            ], lg=4), 

            dbc.Col([
                 mapa_ejemplo_story.display()

            ], lg=8), 
   
        ]),


        dbc.Row([
            dbc.Col([
                 texto2.show()

            ], lg=4), 

            dbc.Col([
                 mapa_ejemplo_story.display()

            ], lg=8), 
   
        ]),



        
    ]
)