# API Development and Data Transformation

This project contains an API development task that involves working with a dataset of card transaction data. The objective is to develop APIs to retrieve information from the dataset based on specified criteria.

## Dataset

The dataset used in this project is available at the following location:

[Card Transaction Data](https://drive.google.com/file/d/1YfhCPZbofAekMy9tPH_7ZXChVX8w_OUF/view?usp=sharing)

Please download the dataset and save it as `dataset.csv` in the project directory.

## Prerequisites

To run the APIs, make sure you have the following installed:

- Python 3.x
- Flask
- Pandas

## Setup

1. Clone this repository to your local machine or download the project files.

2. Install the required dependencies by running the following command in the project directory:
pip install -r requirements.txt

css

3. Modify the `app.py` file and update the file path of the dataset CSV file to the correct path on your system:
```python
df = pd.read_csv('path/to/dataset.csv')
Running the APIs
Open a terminal or command prompt and navigate to the project directory.

Run the following command to start the Flask development server:
python app.py
The APIs should now be accessible at http://localhost:5000/. You can test the APIs using a tool like Postman or by sending HTTP requests directly.

API Documentation
The API endpoints and their usage are documented in the api_docs.md file. Please refer to this documentation for information on how to use the APIs and the expected input and output formats.

Additional Notes
Input validation and error handling have been implemented to handle invalid requests. The code includes input_validation.py and error_handling.py modules to ensure the APIs validate the input parameters and provide appropriate error responses.

Test cases have been provided for each API endpoint to ensure the functionality is working as expected. You can run the tests using a testing framework of your choice.

Make sure to customize the code and add any additional functionality or improvements as per your requirements.