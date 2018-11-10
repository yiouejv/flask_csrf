from flask import Flask
from apps.icbc.views import bp as icbc_bp
from apps.viruses.views import bp as viruses_bp

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.register_blueprint(icbc_bp)
app.register_blueprint(viruses_bp)


if __name__ == '__main__':
    app.run()
