# -*- coding: utf-8 -*-


class UpdateRouteUseCase:

    def __init__(self, updateRouteCommand):

        self._updateRouteCommand = updateRouteCommand

    def execute(self, route):

        # BUSINESS lOGIC HERE

        self._updateRouteCommand.execute(route)

        # BUSINESS lOGIC HERE


        