from dash import html , dcc
import plotly.express as px


class mapsample:    
    """A class to represent a samplemap of Montreal Elections"""        
    def __init__(self,map_title:str,ID:str):
        """__init__
        Construct all the attributes for the sample map
     
        Args:
            map_title (str): _Title for the map_
            ID (str): _div id to specify unique #id with callbacks and css_
        
        Methods:

        display()
            Function to display a sample map with no arguments, uses plotly express data.
            
            Arguments:
                None

            Returns:
                html.Div : A Div container with a dash core component dcc.Graph() inside
        """
        
        self.map_title = map_title
        self.id = ID

    @staticmethod
    def figura():
         
        df = px.data.election() # replace with your own data source
        geojson = px.data.election_geojson()
        fig = px.choropleth(
             df, geojson=geojson, color="Bergeron",
             locations="district", featureidkey="properties.district",
             projection="mercator"                 
            )
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        return fig

    def display(self):
       
        layout = html.Div(
            [
                html.H4([self.map_title]),
                html.Div([
                    dcc.Graph(figure=self.figura())
                ])
                
            ],id=self.id
        )
        return layout

