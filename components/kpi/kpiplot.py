from dash import html, dcc
import pandas as pd
import dash_bootstrap_components as dbc

class kpiplot:
    """ A class to represent a card with kpi and mini-plot"""
    def __init__(self,label, data, kpimethod):
        """Constructs all the attributes for kpiplot class"""
        self.label = label
        self.data= data
        self.kpimethod = kpimethod
        self.kpi = self.data.count()
    
    @staticmethod
    def figura(self):
        datadict = [dict(x=self.data,type='histogram')]
        layout = dict(
            autosize=True,
            margin=dict(l=1, r=0, t=0, b=0, pad=0),
            height=120,
            plot_bgcolor='rgba(0,0,0,0)',
            yaxis_visible=False,
            yaxis_showticklabels=False,
            xaxis=dict(
                title='',
                type='linear'
            ),
        )
        fig=dict(data=datadict,layout=layout)
        return fig


    def display(self):
        """Displays the card with label, kpi and a mini-plot from the data"""
        layout = html.Div(
            [
             html.Div(self.label,className='kpi-label'),
             html.H2(self.kpi,className='kpi-number d-flex justify-content-end '),
             dcc.Graph(figure=kpiplot.figura(self),
             config={
                 'displayModeBar':False,
                 'staticPlot':True,
                 'fillFrame': False,
                 'frameMargins':0
             }
             ),
            ]
        )
        return layout