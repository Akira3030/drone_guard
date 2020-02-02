# -*- coding: utf-8 -*-

# [DEMO] SOLID --> Principio de Responsabilidad Única
# Esta clase hace una única cosa
# ventajas --> mejora el mantenimiento y la claridad

class CreateRouteUseCase:

    def __init__(self, createRouteCommand):

        self._createRouteCommand = createRouteCommand

    def execute(self, route):

        # [DEMO] aqui iria la lógica de negocio

        self._createRouteCommand.execute(route)

        # [DEMO] aqui iria la lógica de negocio