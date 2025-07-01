from flask import Flask
from db import db  # added
from flask_cors import CORS  # added

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@127.0.0.1:3306/milma_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
