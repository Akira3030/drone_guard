#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Alert():

    def __init__(self, name, date, route):

        self.__validate_date(date)

        self.__name = name
        self.__route = route
        self.__date = date

    def get_name(self):

        return self.__name

    def get_route(self):

        return self.__route

    def get_date(self):

        return self.__date

    def __validate_date(self, date):

        pass

