#!/usr/bin/env python
# -*- coding: utf-8 -*-

# In command line execute --> python -m unittest discover tests

import unittest
import requests

from drone_guard_api.application.module_routes.user_cases.abort_route_use_case import AbortRouteUseCase
from drone_guard_api.application.module_routes.commands_and_queys.commands.abort_route_command import AbortRouteCommand

class EndToEndGelAllRoutesTest(unittest.TestCase):

    URL = 'http://localhost:5002/routes'

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_get_all_routes(self):

        pass

    def test_get_all_routes_validate_json_format(self):
        
        pass


    