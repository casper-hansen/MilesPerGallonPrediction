from core.clean_data import CleanData
from core.predict_data import PredictData
from core.load_data import LoadData

loader = LoadData()
cleaner = CleanData()
predicter = PredictData()

df = loader.load_dataset_as_df()
df = cleaner.clear_question_marks(df)