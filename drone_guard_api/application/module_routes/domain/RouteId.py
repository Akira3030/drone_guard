#!/usr/bin/env python
# -*- coding: utf-8 -*-

class RouteId():


    def __init__(self, route_id):

        self.valid_route_id(route_id)

        self.id = route_id

    def get_id(self):

        return self.id

    def valid_route_id(self, route_id):

        pass