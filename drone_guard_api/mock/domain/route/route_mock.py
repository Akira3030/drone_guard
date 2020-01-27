    #!/usr/bin/env python
# -*- coding: utf-8 -*-

from drone_guard_api.application.module_routes.domain.Route import Route
from drone_guard_api.application.module_routes.domain.RouteAuthor import RouteAuthor
from drone_guard_api.application.module_routes.domain.RouteId import RouteId
from drone_guard_api.application.module_routes.domain.GeoPoint import GeoPoint
from drone_guard_api.application.module_routes.domain.RoutePoints import RoutePoints


class RouteMock():

    def create(self):

        route_author = self.__create_RouteAuthor()
        route_id     = self.__create_RouteId()
        route_points = self.__create_RoutePoints()

        route = Route(route_author, route_id, route_points)

        return route

    def __create_RouteAuthor(self):

        routeAuthor = RouteAuthor(
            'Juan', 
            'Alvarez', 
            'Garcia', 
            '622102039', 
            'juan.garcia@gmail.com')
            
        return routeAuthor


    def __create_RouteId(self):

        routeId = RouteId(12)
        return routeId


    def __create_RoutePoints(self):

        geoPoint1 = GeoPoint(40.513170, -3.678592)
        geoPoint2 = GeoPoint(40.513171, -3.678592)
        geoPoint3 = GeoPoint(40.513172, -3.678593)
        geoPoint4 = GeoPoint(40.513173, -3.678599)
        geoPoint5 = GeoPoint(40.513176, -3.678593)
        geoPoint6 = GeoPoint(40.513178, -3.678591)

        geoPoints = [geoPoint1, geoPoint2, geoPoint3, geoPoint4, geoPoint5, geoPoint6]

        routePoints = RoutePoints(geoPoints)

        return routePoints


