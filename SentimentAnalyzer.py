import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import sqlite3
import pandas as pd

app = dash.Dash(__name__)
sentiment_term = "COVID-19"

colors = {
    'text': '#00acee'
}

app.layout = html.Div(
    [   html.H2('Live Twitter Sentiment Analysis'),
		dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*1000
        ),
    ], style={'textAlign': 'center', 'color': colors['text']}
)

@app.callback(Output('live-graph', 'figure'),
			  [Input('graph-update', 'n_intervals')])
			   
def update_graph_scatter(input_data):
    try:
        conn = sqlite3.connect('twitter.db')
        c = conn.cursor()
        df = pd.read_sql("SELECT * FROM sentiment WHERE tweet LIKE ? ORDER BY unix DESC LIMIT 1000", conn, params=('%' + sentiment_term + '%',))
        df.sort_values('unix', inplace=True)
        df['date'] = pd.to_datetime(df['unix'], unit='ms')
        df.set_index('date', inplace=True)
        df['sentiment_smoothed'] = df['sentiment'].rolling(int(len(df)/5)).mean()
        df.dropna(inplace=True)
        df = df.resample('600ms').mean()

        X = df.index[-100:]
        Y = df.sentiment_smoothed.values[-100:]

        data = plotly.graph_objs.Scatter(
			x=list(X),
			y=list(Y),
			name='Scatter',
			mode= 'lines+markers'
		)

        return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),
												title='Term: {}'.format(sentiment_term),)}

    except Exception as e:
        with open('errors.txt','a') as f:
            f.write(str(e))
            f.write('\n')


if __name__ == '__main__':
    app.run_server(debug=True)