import plotly.graph_objects as go
import plotly.offline as plt
from .models import Input

def get_Bar():
    
    x_values=list(range(1,11))
    y1_values=list(range(11,1,-1))
    y2_values=list(range(1,11,1))
    # animals=['giraffes', 'orangutans', 'monkeys']

    fig = go.Figure(data=[ go.Bar(name='SF Zoo', x=x_values, y=y1_values),
                    go.Bar(name='LA Zoo', x=x_values, y=y2_values)])

    fig.update_layout(barmode='stack')

    plot_div = plt.plot(fig, output_type='div', include_plotlyjs=False)

    return plot_div