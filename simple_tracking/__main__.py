import sys
import getopt

from simple_tracking.web_site.routes import flask_app
from simple_tracking.utils.logger import VisitorLog


def usage():
    return '-l <logfile>'


def main():
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'hl:', ['help', 'logfile='])
    except getopt.GetoptError as err:
        print(err)  # will print something like "option -a not recognized"
        print(usage())
        sys.exit(2)
    log_file = None
    for opt, arg in options:
        if opt in ("-h", "--help"):
            print(usage())
            sys.exit()
        elif opt in ("-l", "--logfile"):
            log_file = arg

    if not logfile:
        print('logfile argument must be supplied')
        print(usage())
        sys.exit(2)

    VisitorLog(log_file)        # singleton
    # turn on the flask rest service in the main thread
    flask_app.run(debug=True)


if __name__ == "__main__":
    main()
