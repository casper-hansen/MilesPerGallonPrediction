from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


from core.clean_data import CleanData
from core.predict_data import PredictData
from core.load_data import LoadData

loader = LoadData()
cleaner = CleanData()
predicter = PredictData()

df = loader.load_dataset_as_df()
df = cleaner.clear_question_marks(df)

y = df['mpg']
X = cleaner.drop_unused_columns(df)

X_train, X_test, y_train, y_test = train_test_split(
                                    X, y, 
                                    test_size=0.2, 
                                    random_state=42
                                   )

rf = RandomForestRegressor()
rf.fit(X_train, y_train)

pred = predicter.predict(X_test, rf)
score = predicter.score_r2(y_test)

print(score)