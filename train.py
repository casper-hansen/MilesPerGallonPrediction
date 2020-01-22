from sklearn.model_selection import train_test_split

from core.clean_data import CleanData
from core.predict_data import PredictData
from core.load_data import LoadData

loader = LoadData()
cleaner = CleanData()
predicter = PredictData()

df = loader.load_dataset_as_df()
df = cleaner.clear_question_marks(df)

y = df['mpg']
X = df.drop(['mpg'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
                                    X, y, 
                                    test_size=0.2, 
                                    random_state=42
                                   )

