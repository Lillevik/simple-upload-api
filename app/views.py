from run import app
import os
from flask import jsonify, request, send_file, abort
from functions import generate_filename


@app.route("/")
def hellow_world():
    return "Hello world!"


@app.route('/upload/file', methods=["POST"])
def general_file_upload():

    """ Uploads a file and saves it to the uploads folder declared in the config """

    if request.method == 'POST':
        try:
            f = request.files['file']
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
    else:
        abort(405)


@app.route('/<file_name>')
def get_file(file_name):
    path = os.getcwd() + "/uploads/"
    if os.path.isfile(path + file_name):
        file = os.path.join(path, file_name)
        return send_file(file)
    else:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    return 'File not found', 404


@app.errorhandler(405)
def method_not_allowed(e):
    return 'Method not allowed', 405


