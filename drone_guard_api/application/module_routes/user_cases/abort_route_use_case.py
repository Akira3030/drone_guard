# -*- coding: utf-8 -*-


class AbortRouteUseCase:

    def __init__(self, abortRouteCommand):

        self._abortRouteCommand = abortRouteCommand

    def execute(self, id):

        # [DEMO] aqui iria la lógica de negocio

        self._abortRouteCommand.execute(id)

        # [DEMO] aqui iria la lógica de negocio
    