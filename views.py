from functools import update_wrapper

from UploadApi import app
import os
from flask import jsonify, request, send_file, current_app, make_response
from functions import generate_filename


@app.route("/")
def hellow_world():
    return "Hello world!"


@app.route('/upload/file', methods=["POST"])
def general_file_upload():
    if request.method == 'POST':
        try:
            f = request.files['image']
            filename = generate_filename(f.filename)
            file_path = os.path.join(app.config["UPLOADS_FOLDER"], filename)
            name_not_unique = True
            while name_not_unique:
                if not os.path.isfile(file_path):
                    name_not_unique = False
                    f.save(file_path)
                else:
                    filename = generate_filename(f.filename)
            return jsonify({'success': {"response_code": "200",
                                        'filename': filename,
                                        'full_link': app.config["DOMAIN"] + filename}})
        except Exception as e:
            print(e)
            return "Error uploading file.", 500


@app.route('/<file_name>')
def get_image_file(file_name):
    path = os.getcwd() + "/uploads"
    file = os.path.join(path, file_name)
    return send_file(file)


@app.errorhandler(404)
def page_not_found(e):
    return 'Page not found', 404


@app.errorhandler(405)
def method_not_allowed(e):
    return 'Method not allowed', 405


