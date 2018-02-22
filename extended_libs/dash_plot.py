import plotly
from app import poll_dash_central

# Create plot from

class Plot:
    def __init__(self):
        self.cache_data = False

    def update_cache(self):

        # Load data from into local dict
        # return data_cache
        data = poll_dash_central()
        return data

    def generate_plot(self):
        # Generate the plot and return an image
        pass

    def upload_plot(self):
        # Upload the plot to the cloud
        pass