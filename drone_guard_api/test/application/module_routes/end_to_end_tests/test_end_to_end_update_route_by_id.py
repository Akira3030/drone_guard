#!/usr/bin/env python
# -*- coding: utf-8 -*-

# In command line execute --> python -m unittest discover tests

import unittest
import requests

from drone_guard_api.application.module_routes.user_cases.abort_route_use_case import AbortRouteUseCase
from drone_guard_api.application.module_routes.commands_and_queys.commands.abort_route_command import AbortRouteCommand

class EndToEndUpdateRouteByIdTest(unittest.TestCase):

    URL = 'http://localhost:5002/routes/9'

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_update_route_when_id_route_exist(self):

        pass

    def test_update_route_when_id_route_not_exist(self):
        
        pass


    