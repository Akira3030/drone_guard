#!/usr/bin/env python
# -*- coding: utf-8 -*-

# In command line execute --> python -m unittest discover tests

import unittest

from drone_guard_api.application.module_routes.user_cases.abort_route_use_case import AbortRouteUseCase
from drone_guard_api.application.module_routes.commands_and_queys.commands.abort_route_command import AbortRouteCommand

class AbortRouteUseCaseTest(unittest.TestCase):

    def setUp(self):

        pass


    def tearDown(self):
        
        pass


    def test_abort_route_when_id_route_not_exist(self):
        """
        GIVEN a ...
        WHEN a ...
        THEN check the ...
        """

        pass

    def test_abort_route_when_id_route_exist(self):

        pass

    def test_abort_route_when_route_not_in_course(self):

        pass

    def test_abort_route_when_route_is_in_course(self):

        pass



    