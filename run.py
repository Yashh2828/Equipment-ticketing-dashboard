from waitress import serve
from main import app  # 'main' is the file name of your Flask app

serve(app, host='0.0.0.0', port=5000)
