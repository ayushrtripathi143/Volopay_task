flask from flask import jsonify

def handle_error(error):
    error_message = str(error)
    error_code = 500  # Default error code

    if isinstance(error, ValueError):
        error_code = 400  # Bad Request
    elif isinstance(error, FileNotFoundError):
        error_code = 404  # Not Found

    error_response = {
        'error': error_message,
    }

    return jsonify(error_response), error_code
