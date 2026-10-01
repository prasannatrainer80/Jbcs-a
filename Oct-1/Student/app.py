from flask import Flask

from config import Config
from database import db
from controller.student_controller import student_controller


def create_app():

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Register controllers
    app.register_blueprint(student_controller)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":

    app = create_app()

    app.run(
        host="localhost",
        port=5000,
        debug=True
    )