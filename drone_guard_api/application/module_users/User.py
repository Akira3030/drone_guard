#!/usr/bin/env python
# -*- coding: utf-8 -*-

class User():


    def __init__(self, name, primer_apellido, segundo_apelllido, localidad, email, movil):

        self.__validate_email(email)

        self.__name = name
        self.__primer_apellido = primer_apellido
        self.__segundo_apelllido = segundo_apelllido
        self.__localidad = localidad
        self.__email =  email
        self.__movil = movil

    def get_name(self):

        return self.__name

    def get_primer_apellido(self):

        return self.__primer_apellido

    def get_segundo_apelllido(self):

        return self.__segundo_apelllido

    def get_localidad(self):

        return self.__localidad

    def get_email(self):

        return self.__email

    def get_movil(self):

        return self.__movil

    def __validate_email(self, email):

        pass

    