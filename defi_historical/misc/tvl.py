import requests
import json 
from datetime import datetime

'''
API_KEY = ''
eth_price = requests.get('https://api.glassnode.com/v1/metrics/market/price_usd_close', params={'a': 'ETH', 'i': '24h', 's': '1603843200', 'api_key': API_KEY})
print(eth_price.json())
print(len(eth_price.json()))
gn_date = []
gn_value = []
for x in eth_price.json(): 
    gn_date.append(datetime.fromtimestamp(int(x['t'])))
    gn_value.append(x['v'])
'''
tvl = requests.get('https://api.llama.fi/protocol/saffron')
tvl = tvl.json()
print(tvl)
tvl = tvl['tvl']

'''
tvl = requests.get('https://api.llama.fi/charts')
tvl = tvl.json()
print(len(tvl))
'''
date = []
value = []
for x in tvl: 
    date.append(datetime.fromtimestamp(int(x['date'])))
    value.append(x['totalLiquidityUSD'])


import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = go.Figure()
fig.add_trace(go.Scatter(x=date, y=value,
                    mode='lines',
                    name='eth_price',
                    line_color='blue'))

fig = make_subplots(specs=[[{"secondary_y": True}]])


#eth_price = '$' + str(int(float((eth_price.json()[-1]['v']))))
fig.add_trace(go.Scatter(x=date, y=value,
                    mode='lines',
                    name='Total Value Locked',
                    line_color='blue'))
'''
fig.add_trace(go.Scatter(x=gn_date, y=gn_value,
                    mode='lines',
                    name='Ethereum Price'),secondary_y=True)
'''
fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linewidth=2,
        zeroline=True,
        linecolor='#F4F4F4',
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=22,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
        gridcolor='#F4F4F4',
        tickfont=dict(
            family='Arial',
            size=22,
            color='blue',
        ),
    ),
    yaxis2=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
        gridcolor='#F4F4F4',
        tickfont=dict(
            family='Arial',
            size=22,
            color='blue',
        ),
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    autosize=True,

    plot_bgcolor='white'
)

'''
fig.add_layout_image(
    dict(
        source="https://images.plot.ly/language-icons/api-home/python-logo.png",
        xref="x",
        yref="y",
        x=0,
        y=3,
        sizex=2,
        sizey=2,
        sizing="stretch",
        opacity=0.5,
        layer="below")
)
'''
fig.show()