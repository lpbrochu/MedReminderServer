from bottle import Bottle
from medicine_service import medicine_service

rootApp = Bottle()


@rootApp.route('/')
def root_index():
    return 'Application Suite Home Page'


if __name__ == '__main__':
    rootApp.merge(medicine_service)
    rootApp.run(host='localhost', port=8080, debug=True)