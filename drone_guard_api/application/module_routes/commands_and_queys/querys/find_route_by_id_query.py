# -*- coding: utf-8 -*-

from drone_guard_api.mock.domain.route.route_mock import RouteMock

class FindRouteByIdQuery:

    def execute(self, id):

        route_mock = RouteMock().create()

        return route_mock