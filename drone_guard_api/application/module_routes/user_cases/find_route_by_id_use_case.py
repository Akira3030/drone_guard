# -*- coding: utf-8 -*-


class FindRouteByIdUseCase:

    def __init__(self, findRouteByIdQuery):

        self._findRouteByIdQuery = findRouteByIdQuery

    def execute(self, id):

        # BUSINESS lOGIC HERE

        route_list = self._findRouteByIdQuery.execute(id)

        # BUSINESS lOGIC HERE

        return route_list
