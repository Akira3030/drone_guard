# -*- coding: utf-8 -*-


class CreateRouteUseCase:

    def __init__(self, createRouteCommand):

        self._createRouteCommand = createRouteCommand

    def execute(self, route):

        # BUSINESS lOGIC HERE

        self._createRouteCommand.execute(route)

        # BUSINESS lOGIC HERE