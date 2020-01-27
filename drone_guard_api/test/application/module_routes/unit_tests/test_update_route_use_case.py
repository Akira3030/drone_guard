#!/usr/bin/env python
# -*- coding: utf-8 -*-

# In command line execute --> python -m unittest discover tests

import unittest

from drone_guard_api.application.module_routes.user_cases.update_route_use_case import UpdateRouteUseCase
from drone_guard_api.application.module_routes.commands_and_queys.commands.update_route_command import UpdateRouteCommand


class UpdateRouteUseCaseTest(unittest.TestCase):

    route_id_mock = 12123213

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_update_route_when_id_route_not_exist(self):

        command = UpdateRouteCommand()
        updateRouteUseCase = UpdateRouteUseCase(command)
        updateRouteUseCase.execute(self.route_id_mock)

        self.assertEqual('foo'.upper(), 'FOO')

    def test_update_route_when_id_route_exist(self):

        command = UpdateRouteCommand()
        updateRouteUseCase = UpdateRouteUseCase(command)
        updateRouteUseCase.execute(self.route_id_mock)

        self.assertEqual('foo'.upper(), 'FOO')