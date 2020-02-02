#!/usr/bin/env python
# -*- coding: utf-8 -*-


#[DEMO] Route es una clase de dominio --> modela nuestra aplicación 
# Atributos privados --> se les asigna valor usando un constructor
# Cuidado de no crear "clases anémicas", clases sin comportamiento (serian como DTOs)
# No usar el patron MVC

class Route():

    def __init__(self, route_author, route_id, route_points):

        if self.__validate_arguments(route_author, route_id, route_points):
            self.route_author = route_author
            self.route_id = route_id
            self.route_points = route_points
        else:
            raise Exception('Error to validate arguments in Route entity')

    def __validate_arguments(self, route_author, route_id, route_points):

        return True

    def calculate_route_size_in_meters(self):

        return 1200

