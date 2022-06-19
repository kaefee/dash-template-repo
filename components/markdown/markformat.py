from dash import html, dcc
import pandas as pd
import dash_bootstrap_components as dbc

class markformat:
    """ A class to represent a card with kpi and mini-plot"""
    def __init__(self,title, text:str):
        """Constructs all the attributes for kpiplot class"""
        self.title = title
        self.text = text

    def show(self):
        """Displays the text in markdow format with proper format"""
        layout = html.Div(
            [
                html.H3(self.title,className='md-title d-flex justify-content-start '),
                dcc.Markdown([
                    self.text
                ])             
            ]
        )
        return layout
