#!/usr/bin/env python
# -*- coding: utf-8 -*-

from application.services.module_alert.DeleteAlertUseCase import DeleteAlertUseCase
from application.services.module_alert.GetAlertsUseCase import GetAlertsUseCase


class AlertController:

    def delete_alert(self):
        
        deleteAlertUseCase = DeleteAlertUseCase()
        deleteAlertUseCase.deleteAlert()


    def get_alerts(self):

        getAlertsUseCase = GetAlertsUseCase()
        getAlertsUseCase.getAlerts()

