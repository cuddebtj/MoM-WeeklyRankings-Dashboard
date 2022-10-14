import dash
import dash_bootstrap_components as dbc

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SLATE, dbc_css],
)
app.title = "MoM FFBL"