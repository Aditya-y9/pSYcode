from flask import Flask, render_template, request
from apify_client import ApifyClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = ApifyClient("apify_api_8rT0FRHAYgyexeHGDstXGMLkFae1fz3d9ydG")

# # Get Apify API key from environment variable
# APIFY_TOKEN = os.getenv('APIFY_TOKEN')
# apify_client = ApifyClient(APIFY_TOKEN)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addProduct')
def add_product():
    return render_template('addProduct.html')

@app.route('/myProducts')
def my_products():
    return render_template('myProducts.html')

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


if __name__ == '__main__':
    app.run(debug="True")