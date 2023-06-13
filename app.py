import pandas as pd
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Get the absolute path of the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the relative file path to the dataset
dataset_file_path = os.path.join(current_directory, 'data.csv')

# Load the dataset into a Pandas DataFrame
df = pd.read_csv(dataset_file_path)

# API 1: Total items sold in Marketing for the last quarter (Q3) of the year
@app.route('/api/total_items', methods=['GET'])
def get_total_items():
    start_date = pd.to_datetime(request.args.get('start_date'))
    end_date = pd.to_datetime(request.args.get('end_date'))
    department = request.args.get('department')

    # Filter the DataFrame based on the provided parameters
    filtered_df = df[
        (df['department'] == department) &
        (df['date'] >= start_date) &
        (df['date'] <= end_date)
    ]

    # Calculate the total items sold
    total_items = filtered_df['seats'].sum()

    return jsonify(total_items)


# API 2: Second most sold item in terms of quantity sold in Q4
@app.route('/api/nth_most_total_item', methods=['GET'])
def get_nth_most_total_item():
    item_by = request.args.get('item_by')
    start_date = pd.to_datetime(request.args.get('start_date'))
    end_date = pd.to_datetime(request.args.get('end_date'))
    n = int(request.args.get('n'))

    # Filter the DataFrame based on the provided parameters
    filtered_df = df[
        (df['date'] >= start_date) &
        (df['date'] <= end_date)
    ]

    # Group by item and calculate the total quantity sold
    item_sales = filtered_df.groupby('software')['seats'].sum()

    # Retrieve the nth most sold item
    if item_by == 'quantity':
        nth_most_item = item_sales.nlargest(n).index[n-1]
    else:
        nth_most_item = item_sales.nlargest(n, key=lambda x: df[df['software'] == x]['amount'].sum()).index[n-1]

    return jsonify(nth_most_item)

@app.route('/')
def index():
    return 'Welcome to the root URL!'

if __name__ == '__main__':
    app.run(debug=True)
