# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app, server
from pages import index, predictions

# Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
navbar = dbc.NavbarSimple(
    brand='Potency Calculator',
    brand_href='/',
    #children=[
        #dbc.NavItem(dcc.Link('Potency Calculator', href='/potency-calculator', className='nav-link'))
    #],
    sticky='top',
    color='primary',
    light=True,
    dark=False
)

# Footer docs:
# dbc.Container, dbc.Row, dbc.Col: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# html.P: https://dash.plot.ly/dash-html-components
# fa (font awesome) : https://fontawesome.com/icons/github-square?style=brands
# mr (margin right) : https://getbootstrap.com/docs/4.3/utilities/spacing/
# className='lead' : https://getbootstrap.com/docs/4.3/content/typography/#lead
footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            [
                html.P(
                [
                    html.Span('Med Cabinet 3 (The most awesome MedCab Team)', className='mr-2'),
                    #html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:<you>@<provider>.com'),
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/MedCabinet/Weed-Calculator'),
                    #html.A('Return to Med Cabinet', href='https://medcabinetog.netlify.com/'),
                    #html.A(html.I(className='fab fa-twitter-square mr-1'), href='https://twitter.com/<you>'),
                ],
                className='lead'
            ),
            html.P(html.A('Return to Med Cabinet', href='https://medcabinetog.netlify.com/'))
            ]
        )
    )
)

# Layout docs:
# html.Div: https://dash.plot.ly/getting-started
# dcc.Location: https://dash.plot.ly/dash-core-components/location
# dbc.Container: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dbc.Container(id='page-content', className='mt-4'),
    html.Hr(),
    footer
])


# URL Routing for Multi-Page Apps: https://dash.plot.ly/urls
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/potency-calculator':
        return predictions.layout
    else:
        return dcc.Markdown('## Page not found')

# Run app server: https://dash.plot.ly/getting-started
if __name__ == '__main__':
    app.run_server(debug=True)
