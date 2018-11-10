from flask import Flask
from apps.icbc.views import bp as icbc_bp
from apps.viruses.views import bp as viruses_bp
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.register_blueprint(icbc_bp)
app.register_blueprint(viruses_bp)

CSRFProtect(app)

if __name__ == '__main__':
    app.run()
