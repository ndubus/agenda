#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#agenda.py
import appModuleHandler
import controlTypes
import api
import textInfos
import speech

fieldHeader = {
9:u"Jour du rendez-vous",
10:u"Mois",
11:u"Année",
12:u"Heure",
13:u"Minute",
14:u"Durée en minutes ou en heures",
15:u"Motif"
}

class AppModule(appModuleHandler.AppModule):

    def event_gainFocus(self, obj, nextHandler):
        controlID = obj.windowControlID
        if controlID in [9, 10, 11, 12, 13, 14, 15]:
            speech.speakMessage(fieldHeader[controlID])
            speech.speakObject(obj, reason=controlTypes.REASON_CHANGE)
        else:
            speech.speakObject(obj, reason=controlTypes.REASON_CARET)
        nextHandler

