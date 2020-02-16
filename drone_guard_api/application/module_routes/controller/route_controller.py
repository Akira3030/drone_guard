# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
from flask_api import status

import os
import json
import uuid
import logging.config

from drone_guard_api.mock.domain.route.route_mock import RouteMock

from drone_guard_api.application.module_routes.domain.Route import Route
from drone_guard_api.application.module_routes.domain.RoutePoints import RoutePoints
from drone_guard_api.application.module_routes.domain.GeoPoint import GeoPoint
from drone_guard_api.application.module_routes.domain.RouteId import RouteId
from drone_guard_api.application.module_routes.domain.RouteAuthor import RouteAuthor

from drone_guard_api.application.module_routes.user_cases.delete_route_user_case import DeleteRouteUserCase
from drone_guard_api.application.module_routes.user_cases.update_route_use_case import UpdateRouteUseCase
from drone_guard_api.application.module_routes.user_cases.create_route_use_case import CreateRouteUseCase
from drone_guard_api.application.module_routes.user_cases.abort_route_use_case import AbortRouteUseCase
from drone_guard_api.application.module_routes.user_cases.planning_route_use_case import PlanningRouteUseCase
from drone_guard_api.application.module_routes.user_cases.find_all_routes_use_case import FindAllRoutesUseCase
from drone_guard_api.application.module_routes.user_cases.find_route_by_id_use_case import FindRouteByIdUseCase


from drone_guard_api.application.module_routes.commands_and_queys.commands.delete_route_command import DeleteRouteCommand
from drone_guard_api.application.module_routes.commands_and_queys.commands.create_route_command import CreateRouteCommand
from drone_guard_api.application.module_routes.commands_and_queys.commands.update_route_command import UpdateRouteCommand
from drone_guard_api.application.module_routes.commands_and_queys.commands.abort_route_command import AbortRouteCommand

from drone_guard_api.application.module_routes.commands_and_queys.querys.find_active_routes_query import FindActiveRoutesQuery
from drone_guard_api.application.module_routes.commands_and_queys.querys.find_all_routes_query import FindAllRoutesQuery
from drone_guard_api.application.module_routes.commands_and_queys.querys.find_route_by_criteria_query import FindRouteByCriteriaQuery
from drone_guard_api.application.module_routes.commands_and_queys.querys.find_route_by_id_query import FindRouteByIdQuery


route_blueprint = Blueprint('module_routes', __name__)

logfile = logging.getLogger('file')


APP_MESSAGE_HTTP_ERROR_500_JSON = '{"status": 500,"message": "Error to process the request"}'
APP_MESSAGE_HTTP_OK_200_JSON    = '{"status": 200,"message": "OK"}'
MIMETYPE_JSON                   = "application/json"


@route_blueprint.route("/routes", methods=['GET'])
def find_all_routes():

    try:
        command = FindAllRoutesQuery()
        use_case = FindAllRoutesUseCase(command)
        routes = use_case.execute()
        routes_json = json.dumps(routes, default=lambda x: x.__dict__)

        return Response(
            routes_json, 
            mimetype=MIMETYPE_JSON, 
            status=status.HTTP_200_OK
        )

    except:
        return Response(
            APP_MESSAGE_HTTP_ERROR_500_JSON, 
            mimetype=MIMETYPE_JSON, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@route_blueprint.route("/routes/<string:id>", methods=['GET'])
def find_route_by_id(id):

    try:
        command = FindRouteByIdQuery()
        user_case = FindRouteByIdUseCase(command)
        route = user_case.execute(id)
        route_json = json.dumps(route, default=lambda x: x.__dict__)

        return Response(
            route_json, 
            mimetype=MIMETYPE_JSON, 
            status=status.HTTP_200_OK
        )

    except Exception as error:

        logfile.exception("Se ha producido una excepción: %s",error)

        return Response(
            APP_MESSAGE_HTTP_ERROR_500_JSON, 
            mimetype=MIMETYPE_JSON, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@route_blueprint.route("/routes/<string:id>", methods=['DELETE'])
def delete_route_by_id(id):

    try:
        command = DeleteRouteCommand()
        user_case = DeleteRouteUserCase(command)
        user_case.execute(id)

        return Response(
            APP_MESSAGE_HTTP_OK_200_JSON,
            mimetype=MIMETYPE_JSON, 
            status=status.HTTP_200_OK
        )

    except Exception as error:

        logfile.exception(error)

        return Response(
            APP_MESSAGE_HTTP_ERROR_500_JSON, 
            mimetype=MIMETYPE_JSON, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@route_blueprint.route("/routes", methods=['POST'])
def create_route():

    try: 
        id_route = uuid.uuid1()
        #id_author = request.json['id_author']
        #id_routhe = request.json['id_route']
        # ...

        route = Route('mock','mock','mock')
        #command = CreateteRouteCommand(route)
        #user_case = CreateRouteUseCase(command)
        #user_case.execute(route)

        return Response(
            APP_MESSAGE_HTTP_OK_200_JSON, 
            mimetype=MIMETYPE_JSON, 
            status=status.HTTP_200_OK
        )

    except Exception as error:

        logfile.exception(error)

        return Response(
            APP_MESSAGE_HTTP_ERROR_500_JSON, 
            mimetype=MIMETYPE_JSON, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@route_blueprint.route("/routes/<string:id>", methods=['PUT'])
def update_route_by_id(id):

    try: 
        #id_author = request.json['id_author']
        #id_routhe = request.json['id_route']
        # ...

        route = Route('mock','mock','mock')
        #command = UpdateRouteCommand(route)
        #user_case = UpdateRouteUseCase(command)
        #user_case.execute(route)

        return Response(
            APP_MESSAGE_HTTP_OK_200_JSON, 
            mimetype=MIMETYPE_JSON, 
            status=status.HTTP_200_OK
        )

    except Exception as error:

        logfile.exception(error)

        return Response(
            APP_MESSAGE_HTTP_ERROR_500_JSON, 
            mimetype=MIMETYPE_JSON, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@route_blueprint.route("/routes/abort/<string:id>", methods=['GET'])
def abort_route_by_id(id):

    try:
        command = AbortRouteCommand()
        use_case = AbortRouteUseCase(command)
        use_case.execute(id)

        return Response(
            APP_MESSAGE_HTTP_OK_200_JSON, 
            mimetype=MIMETYPE_JSON, 
            status=status.HTTP_200_OK
        )

    except Exception as error:

        logfile.exception(error)

        return Response(
            APP_MESSAGE_HTTP_ERROR_500_JSON, 
            mimetype=MIMETYPE_JSON, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
