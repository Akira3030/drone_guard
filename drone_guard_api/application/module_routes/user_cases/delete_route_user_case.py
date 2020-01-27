# -*- coding: utf-8 -*-


class DeleteRouteUserCase:

    def __init__(self, deleteRouteCommand):

        self._deleteRouteCommand = deleteRouteCommand

    def execute(self, id):

        # BUSINESS lOGIC HERE

        self._deleteRouteCommand.execute(id)

        # BUSINESS lOGIC HERE
        
