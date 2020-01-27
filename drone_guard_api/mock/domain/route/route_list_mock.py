    #!/usr/bin/env python
# -*- coding: utf-8 -*-

from drone_guard_api.application.module_routes.domain.Route import Route
from drone_guard_api.application.module_routes.domain.RouteAuthor import RouteAuthor
from drone_guard_api.application.module_routes.domain.RouteId import RouteId
from drone_guard_api.application.module_routes.domain.GeoPoint import GeoPoint
from drone_guard_api.application.module_routes.domain.RoutePoints import RoutePoints

from drone_guard_api.mock.domain.route.route_mock import RouteMock


class RouteListMock():

    def create(self):

        route1 = RouteMock().create()
        route2 = RouteMock().create()
        route3 = RouteMock().create()
        route4 = RouteMock().create()

        route_list = [route1, route2, route3, route4]

        return route_list






