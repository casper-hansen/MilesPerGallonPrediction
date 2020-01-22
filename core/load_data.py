import pandas as pd

class LoadData():
    def __init__(self):
        self.columns = ['mpg',
                        'cylinders',
                        'displacement',
                        'horsepower',
                        'weight',
                        'acceleration',
                        'model_year',
                        'origin',
                        'car_name']

    def load_dataset_as_df(self):
        df = pd.read_table("data/auto-mpg.data", header=None, delim_whitespace=True)
        df.columns = self.columns

        return df