#!/usr/bin/env python
# -*- coding: utf-8 -*-

class RouteAuthor():


    def __init__(self, name, primer_apellido, segundo_apellido, movil, email):

        self.__valid_movil(movil)
        self.__valid_email(email)

        self.name = name
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.movil = movil
        self.email = email

    def __valid_movil(self, movil):

        pass

    def __valid_email(self, email):

        pass