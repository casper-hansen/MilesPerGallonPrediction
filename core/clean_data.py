
class CleanData():
    def __init__(self):
        pass

    def clear_question_marks(self, df):
        df = df[df['horsepower'] != '?']
        df['horsepower'] = df['horsepower'].astype('float')

        return df