#!/usr/bin/env python
# -*- coding: utf-8 -*-

# In command line execute --> python -m unittest discover tests

import unittest
import requests

from entrypoint import create_app
from flask_api import status

from drone_guard_api.application.module_routes.user_cases.delete_route_user_case import DeleteRouteUserCase
from drone_guard_api.application.module_routes.commands_and_queys.commands.delete_route_command import DeleteRouteCommand

HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json'}
CONTENT_TYPE_JSON = 'application/json'

class EndToEndDeleteRouteByIdTest(unittest.TestCase):


    def setUp(self):

        self.app = create_app(config='test')
        self.client = self.app.test_client()


    def tearDown(self):
        pass


    def test_delete_routes(self):

        respuesta = self.client.delete(
            "/routes/9",
            headers=HEADERS
        )

        self.assertEqual(status.HTTP_200_OK, respuesta.status_code)
        self.assertEqual(CONTENT_TYPE_JSON, respuesta.content_type)



    