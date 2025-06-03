# Import Packages and other files for app
from app import app, server #NEED THE IMPORT SERVER FOR RENDER
from dash import dcc, html
from dash_iconify import DashIconify
from dash.dependencies import Output, Input
from datetime import date
import recipe_list
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import random
import time
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
today = date.today()

# padding for the page content
CONTENT_STYLE = {
   "margin-left": "2rem",
   "margin-right": "2rem",
   "padding": "2rem 1rem",
}

# Index Page Layout
colors = {
    'background': '#ffffff',
    'text': '#0000CD'
}

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

# define sidebar layout
app.layout = html.Div([
   dcc.Location(id="url"),
   content
])

GITHUB = 'https://github.com/joegriff19'
LINKEDIN = 'https://www.linkedin.com/in/joseph-m-griffin/'

# index page layout
index_layout = html.Div(
    children=[
            html.Header(
                children=[
                    html.Br(),
                    html.Div(children="🪿", style={"fontSize": "85px"}),
                    html.Div(children="Goose Cookbook", style={"fontSize": "45px"}),
                    html.Div(children="powered by JI", style={"fontSize": "18px"}),
                    html.Div(children="(Juliana's Intelligence)", style={"fontSize": "18px"}),
                ],
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'background': colors['background']
                }
            ),
            html.Br(),
            html.Div([
                "Select a meal category",
                dcc.Dropdown(
                    list(recipe_list.all_options.keys()),
                    clearable=False,
                    searchable=False,
                    id='meals-dd'
                ),
                html.Br(),
                html.Div("Select a recipe"),
                dcc.Dropdown(id='recipes-dd', options=[], searchable=False, clearable=False),
                html.Br(),
            ], style={
                'textAlign': 'center',
                'color': '#000080',
                'max-width': '500px',
                'margin': 'auto'
            }
            ),
            html.Div([
                dbc.Spinner(children=[html.Div(id='recipe_info')], size="lg", color="#000080", type="border",
                            show_initially=False,
                            spinner_style={"position": "absolute", "top": "-30px"}),
                html.Br(),
                html.Div(children=[
                    dmc.Group(
                        children=[
                            dmc.Anchor(
                                children=[DashIconify(
                                    icon='line-md:github-loop', width=40, color="#000080")
                                ],
                                href=GITHUB
                            ),
                            dmc.Anchor(
                                children=[
                                    DashIconify(
                                        icon='ri:linkedin-fill', width=40, color="#000080")
                                ],
                                href=LINKEDIN
                            )
                        ], position='center'
                    )
                ]),
                html.Br(),
            ], style={'textAlign': 'center',
                      'max-width': '900px',
                      'margin': 'auto',
                      'color': '#000080',
                      }
            ),
    ])


# page callback
@app.callback(
    Output('page-content', 'children',),
    [Input('url', 'pathname',)]
)
def render_page_content(pathname):
    if pathname == '/':
        return index_layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
       [
           html.H1("404: Not found", className="text-danger"),
           html.Hr(),
           html.P(f"The pathname {pathname} was not recognised..."),
       ]
    )


# dropdown callback
@app.callback(
    Output('recipes-dd', 'options'),
    Input('meals-dd', 'value'),
    prevent_initial_call=True
)
def set_recipes_options(selected_meal):
    return [{'label': i, 'value': i} for i in recipe_list.all_options[selected_meal]]


# dropdown2 callback
@app.callback(
    Output('recipe_info', 'children'),
    Input('recipes-dd', 'value'),
    prevent_initial_call=True
)
def set_display_children(value):
    # sleep time for spinner to spin
    if value is not None:
        time.sleep(1)

    # Breakfast
    if value == 'Breakfast1':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Breakfast2':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Breakfast3':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Breakfast4':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Breakfast5':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())

    # Lunch/Dinner
    if value == 'LD1':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'LD2':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'LD3':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'LD4':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'LD5':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())

    # Snack
    if value == 'Snack1':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Snack2':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Snack3':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Snack4':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Snack5':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())

    # Bread
    if value == 'Bread1':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Bread2':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Bread3':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Bread4':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Bread5':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())

    # Other
    if value == 'Other1':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Other2':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Other3':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Other4':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Other5':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())

    # Dessert
    if value == 'Dessert1':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Dessert2':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Dessert3':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Dessert4':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
    if value == 'Dessert5':
        return ('Insert recipe here',
                html.Br(), html.Br(),
                html.Img(
                    src="assets/test.jpg",
                    style={"width": "100%", "height": "auto"},
                    className="img-fluid"
                ),
                html.Br(), html.Br())
