from flask import Flask, render_template, request, redirect
from apify_client import ApifyClient
#from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
#load_dotenv()
from PIL import Image
import io

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    price = db.Column(db.Integer, default=0)
    score = db.Column(db.Integer, default=0)

    def __repr__(self):
       return f"<YourModel id={self.id}, name={self.name}, price={self.price}, score={self.score}>"


   
client = ApifyClient("apify_api_8rT0FRHAYgyexeHGDstXGMLkFae1fz3d9ydG")

# # Get Apify API key from environment variable
# APIFY_TOKEN = os.getenv('APIFY_TOKEN')
# apify_client = ApifyClient(APIFY_TOKEN)


@app.route('/')
def index():
    return render_template('imageForm.html')

@app.route('/addProduct')
def add_product():
    return render_template('addProduct.html')

@app.route('/myProducts')
def my_products():
    todos = Todo.query.all()
    return render_template('myProducts.html', todos=todos)




@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get form data from the request
        product_category = request.form.get('product_category')
        product = request.form.get('product')
        product_name = request.form.get('product_name')
        product_description = request.form.get('product_description')
        price = request.form.get('price')
        business_coverage = request.form.get('business_coverage')
        target_audience = request.form.get('target_audience')
        marketing_budget = request.form.get('marketing_budget')

        new_todo = Todo(name=product_name, price = price)

        db.session.add(new_todo)
        db.session.commit()
        return redirect('/database')

        # Pass the form data to the ML model for processing
        # Here you would write code to process the form data using your ML model
        # For demonstration purposes, let's just print the form data
        print('Product Category:', product_category)
        print('Product:', product)
        print('Product Name:', product_name)
        print('Product Description:', product_description)
        print('Price:', price)
        print('Business Coverage:', business_coverage)
        print('Target Audience:', target_audience)
        print('Marketing Budget:', marketing_budget)

        # You can return a response to the client, for example, a success message
        return 'Form submitted successfully!'

@app.route('/get_instagram_data', methods=['POST'])
def get_instagram_data():
    # Extract input data from the form
    username = request.form['username']
    results_limit = int(request.form['results_limit'])  # Assuming you have a form field for the results limit

    # Prepare the Actor input
    run_input = {
        "username": [username],
        "resultsLimit": results_limit,
    }

    # Run the Actor and wait for it to finish
    run = client.actor("nH2AHrwxeTRJoN5hX").call(run_input=run_input)

    # Fetch relevant data (URL, comments count, likes count) from the run's dataset (if there are any)
        # Fetch relevant data (URL, comments count, likes count) from the run's dataset (if there are any)
    items = []
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    # Extract the desired fields from each item
        url = item.get('url')
        commentsCount = item.get('commentsCount')
        likesCount = item.get('likesCount')

    # Check for None values and replace with a default message
        if commentsCount is None:
            commentsCount = 'Comments data not available'
        if likesCount is None:
            likesCount = 'Likes data not available'

    # Create a dictionary with the extracted data
        extracted_data = {
            'url': url,
            'commentsCount': commentsCount,
            'likesCount': likesCount
        }

        items.append(extracted_data)

    return render_template('result.html', items=items)

@app.route('/database')
def database():
    todos = Todo.query.all()
    return render_template('database.html', todos=todos)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the POST request has the file part
    if 'imageFile' not in request.files:
        return 'No file uploaded', 400

    file = request.files['imageFile']

    # Check if the file is empty
    if file.filename == '':
        return 'No selected file', 400

    # Read the image file
    img_bytes = file.read()
    img = Image.open(io.BytesIO(img_bytes))

    # Process the image (you can replace this with your ML model code)
    # For example, resize the image to 100x100 pixels
    resized_img = img.resize((100, 100))

    # Here you would pass the processed image to your ML model
    # For demonstration purposes, let's just return a success message
    return 'Image uploaded and processed successfully'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug="True")