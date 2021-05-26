from flask import make_response

from simple_tracking.web_site.resource import html
from simple_tracking.utils.logger import VisitorLog
from simple_tracking.web_site.generator import IdGenerator

cookie_name = 'visitor_id'


def handle_request(page_request):
    # try get cookie
    cookie_content = page_request.cookies.get(cookie_name)
    # web page content
    resp = make_response(html.format(page_request.path, cookie_content))
    if not cookie_content:
        # place new cookie
        cookie_content = IdGenerator().next()
        resp.set_cookie(cookie_name, str(cookie_content))
    VisitorLog('../').log(page_request.path, cookie_content)
    return resp
