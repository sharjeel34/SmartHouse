# This is a sample Python script.
import string

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request, jsonify
import pickle
import numpy as np

model = pickle.load(open('models.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def home():
    return "successful"


#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
@app.route('/predict', methods=['Post'])
def predict():
    # price = request.form.get('price')
    location = request.form.get('location')
    city = request.form.get('city')
    baths = request.form.get('baths')
    purpose = request.form.get('purpose')
    property_type = request.form.get('property_type')
    bedrooms = request.form.get('bedrooms')
    Total_Area = request.form.get('Total_Area')
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    input_query = np.array([[location, city, baths, purpose, property_type, bedrooms, Total_Area,
                             latitude, longitude]], dtype=float)
    result = model.predict(input_query)[0]

    # result = {'price': price, 'location': location, 'city': city, 'baths': baths}
    return jsonify(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
