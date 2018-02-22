import logging
from logging.handlers import SocketHandler

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_debug_message(string):
    log.debug(string)
    print("{}{}{}".format(bcolors.OKBLUE, string, bcolors.ENDC))

def print_info(string):
    log.info(string)
    print(string)

def print_warning_message(string):
    log.warning(string)
    print("{}{}{}".format(bcolors.WARNING, string, bcolors.ENDC))

def print_error_message(string):
    log.error(string)
    print("{}{}{}".format(bcolors.FAIL, string, bcolors.ENDC))

log = logging.getLogger('Mass_converter')
logging.basicConfig(filename='log.log', level=logging.DEBUG)
log.setLevel(1)  # to send all messages to cutelog
socket_handler = SocketHandler('127.0.0.1', 19996)  # default listening address
log.addHandler(socket_handler)