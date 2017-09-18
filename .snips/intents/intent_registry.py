# -*-: coding utf-8 -*-
""" Class for holding all the intent classes present in the assistant. """

# *****************************************************************************
# *****************************************************************************
# *****************************************************************************
#
# WARNING: THIS IS AN AUTO-GENERATED FILE
# DO NOT ATTEMPT TO EDIT IT, AS CHANGES WILL BE OVERWRITTEN.
#
# *****************************************************************************
# *****************************************************************************
# *****************************************************************************

# pylint: disable=line-too-long

from intents.add_alarm_intent import AddAlarmIntent
from intents.cancel_all_alarms_intent import CancelAllAlarmsIntent
from intents.cancel_alarm_intent import CancelAlarmIntent
from intents.what_is_the_time_intent import WhatIsTheTimeIntent
from intents.list_alarms_intent import ListAlarmsIntent


class IntentRegistry:
    """ Class for holding all the intent classes present in the assistant. """

    # pylint: disable=too-few-public-methods
    def __init__(self):
        """ Initialisation. """
        self.intent_classes = [
            AddAlarmIntent,
            CancelAllAlarmsIntent,
            CancelAlarmIntent,
            WhatIsTheTimeIntent,
            ListAlarmsIntent
            ]
