#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Video():

    def __init__(self, id, name, url, creation_date):

        self.__id = id
        self.__name = name
        self.__url = url 
        self.__date = creation_date

    def get_id(self):

        return self.__id

    def get_name(self):

        return self.__name

    def get_url(self):

        return self.__url

    def get_creation_date(self):

        return self.__date
