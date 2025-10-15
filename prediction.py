import pickle
import warnings
warnings.filterwarnings('ignore')

# Load the model
pickle_in = open("artifacts/pred.pkl", "rb")
pred = pickle.load(pickle_in)
pickle_in.close()

# Define the prediction function
def prediction_count(season, weather, temp, humidity,windspeed,casual, year, month, day, weekday, am_or_pm, holidays):
    prediction = pred.predict([[season, weather, temp, humidity,windspeed ,casual, year, month, day, weekday, am_or_pm, holidays]])
    return abs(prediction)



