from dash import html, dcc
import pandas as pd
import dash_bootstrap_components as dbc
from markdown2 import Markdown

class markformat:
    """ A class to represent a card with kpi and mini-plot"""
    def __init__(self,title, text):
        """Constructs all the attributes for kpiplot class"""
        self.title = title
        self.text= text

        
    @staticmethod
    def transform(self):
      
        md_to_html  = Markdown.convert(self.text)
        return md_to_html

    def show(self):
        """Displays the text in markdow format with proper format"""
        layout = html.Div(
            [
                html.H4(self.title,className='md-title d-flex justify-content-start '),
                html.Div([
                    self.transform(self)
                ])             
            ]
        )
        return layout
