# -*- coding: utf-8 -*-


from drone_guard_api.mock.domain.route.route_list_mock import RouteListMock


class FindAllRoutesQuery:


    def execute(self):

        route_list = RouteListMock().create()

        return route_list



