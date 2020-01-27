# -*- coding: utf-8 -*-


class AbortRouteUseCase:

    def __init__(self, abortRouteCommand):

        self._abortRouteCommand = abortRouteCommand

    def execute(self, id):

        # BUSINESS lOGIC HERE

        self._abortRouteCommand.execute(id)

        # BUSINESS lOGIC HERE
    