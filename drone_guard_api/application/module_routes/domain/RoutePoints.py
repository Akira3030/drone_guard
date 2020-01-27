#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


class RoutePoints():

    def __init__(self, list_geo_points):

        self.valid_geo_points(list_geo_points)

        self.geo_points = list_geo_points

    def get_geo_points(self):

        return self.geo_points

    def valid_geo_points(self, list_geo_points):

        pass

