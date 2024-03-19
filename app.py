#libraries
import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from callbacks import register_callbacks

# Dash instance declaration
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY])

app.config.suppress_callback_exceptions=True



#Top menu, items get from all pages registered with plugin.pages
navbar = dbc.NavbarSimple([

    dbc.NavItem(dbc.NavLink( "Inicio", href="/")),
    dbc.DropdownMenu(
        [
            
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="Data Science",
    ),
    dbc.NavItem(dbc.NavLink("Nosotros", href="/nosotros")),
    ],
    brand="DS4A Project - Team 300",
    color="primary",
    dark=True,
    className="mb-2",
)

#Main layout
app.layout = dbc.Container(
    [
        navbar,
	    dash.page_container
    ],
    className="dbc",
    fluid=True,
)

# Call to external function to register all callbacks
register_callbacks(app)

# This call will be used with Gunicorn server
server = app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8050, debug=True)