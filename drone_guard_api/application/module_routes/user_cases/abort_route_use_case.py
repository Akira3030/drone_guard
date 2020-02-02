# -*- coding: utf-8 -*-


# [DEMO] SOLID --> Principio de Responsabilidad Única
# Esta clase hace una única cosa
# ventajas --> mejora el mantenimiento, la claridad, el testing y la automatización

class AbortRouteUseCase:

    def __init__(self, abortRouteCommand):

        self._abortRouteCommand = abortRouteCommand

    def execute(self, id):

        # [DEMO] aqui iria la lógica de negocio

        self._abortRouteCommand.execute(id)

        # [DEMO] aqui iria la lógica de negocio
    