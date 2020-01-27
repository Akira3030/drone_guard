# -*- coding: utf-8 -*-

import csv
import sqlite3
import datetime
from sqlite3 import Error
import os
from io import StringIO

from drone_guard_api.mock.domain.route.route_list_mock import RouteListMock


class FindAllRoutesQuery:


    def execute(self):

        return RouteListMock().create()



