import plotly.plotly as py
import plotly.graph_objs as go
from extended_libs.airtable import load_from_airtable
import numpy as np
import matplotlib.pyplot
import time

'''
def gen_plot_n_upload():
    data = load_from_airtable()
    print(data)

    # Transform data into numpy columns
    yes_y = 0
    no_y = 0
    abstain_y = 0
    current_ratio_y = 0
    timestamp = 0

    # Create traces
    yes_count = go.Scatter(
        x=timestamp,
        y=random_y0,
        mode='lines+markers',
        name='lines+markers'
    )
    no_count = go.Scatter(
        x=timestamp,
        y=random_y1,
        mode='lines+markers',
        name='lines+markers'
    )
    abstain_count = go.Scatter(
        x=timestamp,
        y=random_y2,
        mode='lines+markers',
        name='lines+markers'
    )
    current_ratio = go.Scatter(
        x=timestamp,
        y=random_y2,
        mode='lines+markers',
        name='lines+markers'
    )

    data = [yes_count, no_count, abstain_count, current_ratio]

    py.iplot(data, filename='dope_plot')

'''

data_example = load_from_airtable()

def transform_data(airtable_historical_data):
    #print(airtable_historical_data)

    ratio_y = []
    yes_y = []
    no_y = []
    abstain_y = []
    timestamp_x = []

    count = 0

    for event in airtable_historical_data:
        print(event[0])
        time.sleep(1)
        ratio_y.append(event[0][0])
        print(ratio_y)

        count += 1


def gen_plot_n_upload():
    pass

#print(transform_data(data_example))