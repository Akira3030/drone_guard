#!/usr/bin/env python
# -*- coding: utf-8 -*-

class GeoPoint():

    def __init__(self, latitude, longitude):

        self.validateCoordenada(latitude, longitude)

        self.latitude = latitude
        self.longitude = longitude

    def get_latitude(self):

        return self.latitude

    def get_longitude(self):

        return self.longitude

    def validateCoordenada(self, latitude, longitude):

        pass