from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

from core.clean_data import CleanData
from core.predict_data import PredictData
from core.load_data import LoadData

loader = LoadData()
cleaner = CleanData()
predicter = PredictData()

df = loader.load_dataset_as_df()
df = cleaner.clear_question_marks(df)

y = df['mpg']
X = df.drop(['mpg', 'car_name'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
                                    X, y, 
                                    test_size=0.2, 
                                    random_state=42
                                   )

rf = RandomForestRegressor()
rf.fit(X_train, y_train)

pred = rf.predict(X_test)
score = r2_score(y_test, pred)

print(score)