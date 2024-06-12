from flask import Flask, render_template, request, redirect, url_for
from mongoengine import connect, Document, StringField
import joblib
import numpy as np
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import warnings
from sklearn.exceptions import InconsistentVersionWarning

app = Flask(__name__)

# Suppressing version inconsistency warnings
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

# MongoDB configuration
db = connect('salesdata', host='mongodb://localhost:27017/salesdata')

# Define User document
class User(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/salespre')
def salespre():
    return render_template('salespre.html')

@app.route('/learn_more')
def learn_more():
    # Redirect to Streamlit app URL for exploring the data further
    return redirect("http://localhost:8501", code=302)

@app.route('/Logout')
def Logout():
    return render_template('index.html')

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if User.objects(username=username).first() or User.objects(email=email).first():
            return render_template('signup.html', error='Username or email already exists.')

        user = User(username=username, email=email, password=password)
        user.save()

        return redirect(url_for('login'))

    return render_template('signup.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.objects(username=username).first()
        if user and user.password == password:
            return render_template('success.html', username=username)
        else:
            return render_template('login.html', error='Invalid username or password.')

    return render_template('login.html')


def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None

# Prediction route
@app.route('/predict', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        # Parse form data
        item_weight = float(request.form['item_weight'])
        item_fat_content = float(request.form['item_fat_content'])
        item_visibility = float(request.form['item_visibility'])
        # item_visibility = convert_to_float(request.form['item_visibility'])
        item_type = float(request.form['item_type'])
        item_mrp = float(request.form['item_mrp'])
        outlet_establishment_year = float(request.form['outlet_establishment_year'])
        outlet_size = float(request.form['outlet_size'])
        outlet_location_type = float(request.form['outlet_location_type'])
        outlet_type = float(request.form['outlet_type'])

        # Create input array
        X = np.array([[item_weight, item_fat_content, item_visibility, item_type, item_mrp,
                       outlet_establishment_year, outlet_size, outlet_location_type, outlet_type]])

        # Load scaler
        scaler_path = r'C:\Users\Sumit\Desktop\por\models\sc.sav'  # Update the path accordingly
        sc = joblib.load(scaler_path)

        # Standardize input data
        X_std = sc.transform(X)

        # Load model
        model_path =  r'C:\Users\Sumit\Desktop\por\models\lr.sav'  # Update the path accordingly
        model = joblib.load(model_path)

        # Make prediction
        Y_pred = model.predict(X_std)


        # Render result page
        return render_template("result.html", prediction=Y_pred)
    else:
        return render_template("salespre.html")

if __name__ == '__main__':
    app.run(debug=True)
