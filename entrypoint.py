# -*- coding: utf-8 -*-

import flask
import logging, logging.config, yaml
import settings

from drone_guard_api.application.module_routes.controller.route_controller import route_blueprint


# Create app return a Flask instance
def create_app(config='dev'):
    app = flask.Flask(__name__)
    #app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    app.register_blueprint(route_blueprint)

    return app    
    

def log_config():
    logging.config.dictConfig(yaml.load(open('logging.conf')))


if __name__ == "__main__":

    app = create_app()

    logfile = logging.getLogger('file')

    log_config()

    logfile.debug("Init app - drone guard")

    app.run(debug=True, port=5002) 