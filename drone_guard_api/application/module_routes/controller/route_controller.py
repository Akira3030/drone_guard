# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import Flask
from flask import request
from flask import jsonify
from flask import Response

import os
import json
import logging.config

from drone_guard_api.mock.domain.route.route_mock import RouteMock

from drone_guard_api.application.module_routes.domain.Route import Route
from drone_guard_api.application.module_routes.domain.RoutePoints import RoutePoints
from drone_guard_api.application.module_routes.domain.GeoPoint import GeoPoint

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



@route_blueprint.route("/routes", methods=['GET'])
def get_all_routes():

    
    command = FindAllRoutesQuery()

    # INJECCIÓN DE DEPENDENCIAS
    user_case = FindAllRoutesUseCase(command)
    routes = user_case.execute()

    routes_json = json.dumps(routes, default=lambda x: x.__dict__)

    return Response(routes_json, mimetype="application/json", status=200)

@route_blueprint.route("/routes/<string:id>", methods=['GET'])
def find_route_by_id(id):

    command = FindRouteByIdQuery()

    # INJECCIÓN DE DEPENDENCIAS
    user_case = FindRouteByIdUseCase(command)
    route = user_case.execute(id)

    route_json = json.dumps(route, default=lambda x: x.__dict__)

    return Response(route_json, mimetype="application/json", status=200)

@route_blueprint.route("/routes/<string:id>", methods=['DELETE'])
def delete_route_by_id(id):

    command = DeleteRouteCommand()

    # INJECCIÓN DE DEPENDENCIAS
    user_case = DeleteRouteUserCase(command)
    user_case.execute(id)

    return '', 200


@route_blueprint.route("/routes/<string:id>", methods=['PUT'])
def update_route_by_id(id):


    route = Route("Juan Garcia Sanchez", "2", "a")
    
    # INJECCIÓN DE DEPENDENCIAS
    command = UpdateRouteCommand(route)

    user_case = UpdateRouteUseCase(command)
    user_case.execute(route)

    return "update_route_by_id", 200


@route_blueprint.route("/routes/abort/<string:id>", methods=['GET'])
def abort_route_by_id(id):

    # INJECCIÓN DE DEPENDENCIAS
    command = AbortRouteCommand()

    use_case = AbortRouteUseCase(command)
    use_case.execute(id)

    return "abort_route_by_id", 200
