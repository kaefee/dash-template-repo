from dash import html , dcc
import plotly.graph_objects as go

          
class mapcol_municipios:
    """A Class to represent a map of Colombia with two Layers, one for Municipios and 
    the second one for markers as overlay
    
    based in json file of 
    https://www.kaggle.com/code/alfredomaussa/colombia-municipios/notebook?scriptVersionId=39794627
    
    Towns codes available in
    https://www.dane.gov.co/files/censo2005/provincias/subregiones.pdf

    """
    def __init__(self,map_title:str, ID:str,df,markers):
        """__init__ _summary_

        Args:
            map_title (str): Titulo del mapa, html H4 element
            ID (str): css id to use with callbacks
            df (_type_): dataframe with info to use in choropleth
            markers (_type_): small point as overlay in map
        """        
        self.map_title = map_title 
        self.id = ID
        self.df = df 
        self.markers = markers

 
    #@staticmethod
    def figura(self):
        import json
        with open ('./data/jsonmaps/MunicipiosColombia.json', encoding='utf-8') as json_file:
            municipios = json.load(json_file)

        mapa = go.Choroplethmapbox(
            geojson=municipios, 
            locations=self.df.ID, 
            z=self.df['VALUE'],
            colorscale="dense",
            text=self.df.MUNICIPIO,
            marker_opacity=0.9, 
            marker_line_width=0.5,
            colorbar_title = "COP",
            )
        annotations = [
            dict(
                showarrow=False,
                align="right",
                text="",
                font=dict(color="#000000"),
                bgcolor="#f9f9f9",
                x=0.95,
                y=0.95,
            )
        ]

        fig = go.Figure(data=mapa)

        fig.add_scattermapbox(
            lat = self.markers['LAT'],
            lon = self.markers['LON'],
            mode = 'markers+text',
            text = self.markers['TEXT'],  
            below='',                 
            marker_size=8, marker_color='rgb(235, 0, 100)')

        fig.update_layout(
            geo_scope='south america',
            mapbox_style="carto-positron",
            mapbox_zoom=5.5, 
            mapbox_center = {"lat": 4.570868, "lon": -74.2973328},
            annotations=annotations,
            height=1000),

        
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.update_geos(fitbounds="locations")

        
        return fig


    def display(self):   
        layout = html.Div(
            [
                html.H4([self.map_title]),
                html.Div([
                    dcc.Graph(figure=mapcol_municipios.figura(self), id=self.id)
                ])
                
            ]
        )
        return layout
            
        
    