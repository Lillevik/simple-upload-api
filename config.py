import os

DOMAIN = "http://localhost:5000/"  # The last slash is important for now
UPLOADS_FOLDER = os.path.dirname(__file__) + "/uploads"
MAX_CONTENT_LENGTH = 20 * 1024 * 1024 # Limit to 20 megabytes

