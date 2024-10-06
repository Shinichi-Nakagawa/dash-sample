from dash import html, register_page

register_page(__name__, path='/')

# HTMLタグおよび組み込みのコンポーネントでページを作る
layout = [
    html.H1(children='Dash App for Baseball(Top)', style={'textAlign':'center'}),
    html.P('こちらはダミーのページ', style={'textAlign':'center'})
]
