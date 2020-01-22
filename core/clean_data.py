
class CleanData():
    def __init__(self):
        pass

    def clear_question_marks(self, df):
        df = df[df['horsepower'] != '?']
        df.astype({"horsepower": float})

        return df

    def drop_unused_columns(self, df):
        return df.drop(['mpg', 'car_name'], axis=1)