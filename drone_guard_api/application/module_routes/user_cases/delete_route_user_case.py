# -*- coding: utf-8 -*-

# [DEMO] SOLID --> Principio de Responsabilidad Única
# Esta clase hace una única cosa
# ventajas --> mejora el mantenimiento y la claridad

class DeleteRouteUserCase:

    def __init__(self, deleteRouteCommand):

        self._deleteRouteCommand = deleteRouteCommand

    def execute(self, id):

        # [DEMO] aqui iria la lógica de negocio

        self._deleteRouteCommand.execute(id)

        # [DEMO] aqui iria la lógica de negocio
        
