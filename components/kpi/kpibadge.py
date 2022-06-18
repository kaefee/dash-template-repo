from dash import html 

import dash_bootstrap_components as dbc

class kpibadge:
    def __init__(self,kpi,label, badgetype):
        self.kpi = kpi
        self.label = label
        self.badgetype = badgetype
        if badgetype=='Danger':
            self.color = "danger"
        else:
             self.color = "success"

    def display(self):
        layout = html.Div(
            [
             html.Div(self.label,className='h6'),
             html.H2(self.kpi,className='d-flex justify-content-end'),
             dbc.Badge(self.badgetype, color=self.color, className="mr-1"),
            ], className='card m-2'
        )
        return layout
  