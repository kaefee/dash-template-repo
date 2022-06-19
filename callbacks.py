import dash
from dash import dcc, html, Input, Output, callback

def register_callbacks(app):
        
        #@app.callback()
        def update_call1():
            value2= 125
            return value2