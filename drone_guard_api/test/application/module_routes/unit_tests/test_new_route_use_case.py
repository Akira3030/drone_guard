#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch

from drone_guard_api.application.module_routes.user_cases.create_route_use_case import CreateRouteUseCase
from drone_guard_api.application.module_routes.commands_and_queys.commands.create_route_command import CreateRouteCommand

class CreateRouteUseCaseTest(unittest.TestCase):

    route_id_mock = 12123213

    def setUp(self):
        
        pass

    def tearDown(self):

        pass

    def test_create_route_when_id_not_exists(self):

        pass

    def test_create_route_when_id_exists(self):

        pass
