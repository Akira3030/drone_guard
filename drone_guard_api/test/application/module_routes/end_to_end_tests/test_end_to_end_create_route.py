#!/usr/bin/env python
# -*- coding: utf-8 -*-

# In command line execute --> python -m unittest -v

import unittest
import HtmlTestRunner
import requests

from entrypoint import create_app
from flask_api import status


from drone_guard_api.application.module_routes.user_cases.abort_route_use_case import AbortRouteUseCase
from drone_guard_api.application.module_routes.commands_and_queys.commands.abort_route_command import AbortRouteCommand

HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json'}
CONTENT_TYPE_JSON = 'application/json'

class EndToEndCreateRouteTest(unittest.TestCase):

    def setUp(self):
        
        self.app = create_app(config='test')
        self.client = self.app.test_client()
        

    def tearDown(self):
        pass


    def test_create_route(self):

        respuesta = self.client.put(
            "/routes/abort", 
            headers=HEADERS
        )

        self.assertEqual(status.HTTP_200_OK, respuesta.status_code)
        self.assertEqual(CONTENT_TYPE_JSON, respuesta.content_type)






    