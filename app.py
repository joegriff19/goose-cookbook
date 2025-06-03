import dash
import dash_bootstrap_components as dbc
# Dash instance
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(
        __name__,
        title="Goose Cookbook",
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        suppress_callback_exceptions=True,
        update_title=None
)
server = app.server #NEED THIS FOR RENDER