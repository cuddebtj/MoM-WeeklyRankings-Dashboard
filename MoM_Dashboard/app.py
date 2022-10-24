import dash
import dash_bootstrap_components as dbc

# bootstrap theme
# https://bootswatch.com/slate/
external_stylesheets = [dbc.themes.SLATE]

app = dash.Dash(
    external_stylesheets=[dbc.themes.SLATE],
    # these meta_tags ensure content is scaled correctly on different devices
    # see: https://www.w3schools.com/css/css_rwd_viewport.asp for more
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

server = app.server
app.config.suppress_callback_exceptions = True
