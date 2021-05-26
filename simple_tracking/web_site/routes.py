from flask import request

from simple_tracking.web_site.flask_application import create_flask_app
from simple_tracking.visitor.tracker import handle_request

flask_app = create_flask_app()


@flask_app.route('/')
def index():
    return handle_request(request)


@flask_app.route('/contact.html')
def contact():
    return handle_request(request)


@flask_app.route('/about.html')
def about():
    return handle_request(request)


if __name__ == '__main__':
    flask_app.run()
