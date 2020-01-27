#!/usr/bin/env python
# -*- coding: utf-8 -*-

# In command line execute --> python -m unittest discover tests

import unittest
import HtmlTestRunner
import requests

from entrypoint import create_app


from drone_guard_api.application.module_routes.user_cases.abort_route_use_case import AbortRouteUseCase
from drone_guard_api.application.module_routes.commands_and_queys.commands.abort_route_command import AbortRouteCommand

class EndToEndGelAllRoutesTest(unittest.TestCase):

    URL = 'http://localhost:5002/routes'

    def setUp(self):
        
        self.app = create_app(config='test')
        self.client = self.app.test_client()
        

    def tearDown(self):
        pass


    def test_get_all_routes(self):
        r1 = self.client.get("/routes", headers={
            'Accept': 'application/json', 'Content-Type': 'application/json'
        })

        self.assertEqual(200, r1.status_code)
        self.assertEqual('application/json', r1.content_type)

        pass

    def test_get_all_routes_validate_json_format(self):
        r1 = self.client.get("/routes", headers={
            'Accept': 'application/json', 'Content-Type': 'application/json'
        })

        self.assertEqual(200, r1.status_code)
        self.assertEqual('application/json', r1.content_type)

        pass

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass

    if __name__ == '__main__':

        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())


        


    