import plotly.graph_objects as go
import plotly.offline as plt
from .models import Input, Output
from django.db.models import Sum

def get_Bar():
    
    latest_record_id = Input.objects.last().loan_number
    
    period = int(Input.objects.get(pk = latest_record_id).term*12)
    interest = [object.interest_period for object in Output.objects.filter(loan_number = latest_record_id)] 
    principal = [object.principal_period for object in Output.objects.filter(loan_number = latest_record_id)]
    
    x_values=list(range(1,period+1))
    y1_values=interest
    y2_values=principal

    fig = go.Figure(data=[ go.Bar(name='Interest', x=x_values, y=y1_values, marker_color='rgb(242,89,82)'),
                    go.Bar(name='Principal', x=x_values, y=y2_values, marker_color='rgb(13,196,163)')])

    fig.update_layout(
                    title='Interest and Principal payments per period',
                    yaxis=dict(title='Amount', titlefont_size=16, tickfont_size=14,),
                    xaxis=dict(title='Period', titlefont_size=16, tickfont_size=14,),
                    barmode='stack')


    plot_div = plt.plot(fig, output_type='div', include_plotlyjs=False)

    return plot_div

def get_record_number():
    latest_record_id = Input.objects.last().loan_number
    return latest_record_id