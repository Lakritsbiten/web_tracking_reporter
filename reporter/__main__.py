import sys
import getopt
import dateparser

from reporter.reporting import Reporter


def usage():
    return '-s <start_time> -e <end_time> -l <logfile>'


def main():
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'hs:e:l:', ['help', 'start_time=', 'end_time=', 'logfile='])
    except getopt.GetoptError as err:
        print(err)  # will print something like "option -a not recognized"
        print(usage())
        sys.exit(2)
    start_time = None
    end_time = None
    logfile = None
    for opt, arg in options:
        if opt in ("-h", "--help"):
            print(usage())
            sys.exit()
        elif opt in ("-s", "--start_time"):
            start_time = dateparser.parse(arg)
        elif opt in ("-e", "--end_time"):
            end_time = dateparser.parse(arg)
        elif opt in ("-l", "--logfile"):
            logfile = arg

    if not (start_time and end_time):
        print(usage())
        sys.exit(2)

    print(Reporter(log_file=logfile).get_report(start_time=start_time, end_time=end_time))


if __name__ == "__main__":
    main()
