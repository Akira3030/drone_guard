# -*- coding: utf-8 -*-


class FindAllRoutesUseCase:

    def __init__(self, findAllRoutesQuery):

        self._findAllRoutesQuery = findAllRoutesQuery

    def execute(self):

        # BUSINESS lOGIC HERE

        route_list = self._findAllRoutesQuery.execute()

        # BUSINESS lOGIC HERE

        return route_list
