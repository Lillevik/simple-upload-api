from app import app
import os

if __name__ == '__main__':
    app.run(port="5000")


if not os.path.isdir(app.config['UPLOADS_FOLDER']):
    os.mkdir(app.config['UPLOADS_FOLDER'])