from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('Batting.csv')

# applicationの base object
app = Dash()


# HTMLタグおよび組み込みのコンポーネントでページを作る
app.layout = [
    html.H1(children='Dash App for Baseball', style={'textAlign':'center'}),
    dcc.Dropdown(df.playerID.unique(), 'ohtansh01', id='dropdown-selection'),  # default value is Ohtani,Shohei('ohtansh01')
    dcc.Graph(id='graph-content'),
    html.P('Sample data is "Lahman Baseball Database"', style={'textAlign':'center'})
]

# Drop downの選択でcallback発火 -> グラフを更新
@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.playerID==value]
    return px.bar(dff, x='yearID', y='HR')

if __name__ == '__main__':
    app.run(debug=True)
