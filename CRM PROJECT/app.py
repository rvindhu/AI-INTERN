from flask import Flask, render_template, send_file
import csv

app = Flask(__name__)

# Sample customer data (replace with your actual data source)
customers = [
    {"name": "John Doe", "email": "john@example.com", "phone": "123-456-7890"},
    {"name": "Jane Smith", "email": "jane@example.com", "phone": "987-654-3210"}
]

@app.route('/')
def index():
    return render_template('index.html', customers=customers)

@app.route('/download-csv')
def download_csv():
    # Define CSV file name
    csv_filename = "customer_data.csv"

    # Define CSV file headers
    fields = ["name", "email", "phone"]

    # Write customer data to CSV
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for customer in customers:
            writer.writerow(customer)

    # Return CSV file for download
    return send_file(csv_filename, as_attachment=True, attachment_filename=csv_filename)

if __name__ == '__main__':
    app.run(debug=True)
