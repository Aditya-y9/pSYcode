from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('addProduct.html')

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

if __name__ == '__main__':
    app.run(debug="True")