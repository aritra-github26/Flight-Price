from flask import Flask, request, render_template
import datetime

from src.pipelines.predict_pipeline import PredictPipeline, CustomData

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        source = request.form['source']
        destination = request.form['destination']
        airline = request.form['airline']
        additional_info = request.form['additional_info']
        total_stops = request.form['total_stops']
        date_str = request.form['date']
        day, month, _ = map(int, date_str.split('-'))        # day = request.form['day']
        # month = request.form['month']
        # duration_min = request.form['duration_min']
        duration_str = request.form['duration_min']
        duration = datetime.datetime.strptime(duration_str, '%H:%M')
        duration_min = duration.hour * 60 + duration.minute
        
        custom_data = CustomData(
            source, destination, airline, additional_info, int(total_stops), int(day), int(month), int(duration_min)
        )
        
        features = custom_data.get_data_as_df()
        predict_pipeline = PredictPipeline()
        prediction = predict_pipeline.predict(features)
        
        return render_template('home.html', prediction_text='Predicted Flight Fare: {}'.format(prediction))
    else:
        return render_template('home.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080 , debug=True)