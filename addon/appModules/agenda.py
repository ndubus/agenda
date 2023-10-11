# -*- coding: utf-8 -*-
# agenda.py
import appModuleHandler

fieldHeader = {
	10: "Mois",
	11: u"Année",
	12: "Heure",
	13: "Minute",
	14: u"Durée en minutes ou en heures",
	15: "Motif"
}


class AppModule(appModuleHandler.AppModule):
	notSearch = 0

	def event_gainFocus(self, obj, nextHandler):
		controlID = obj.windowControlID
		if controlID in [9, 10, 11, 12, 13, 14, 15]:
			if controlID == 9:
				if obj.simplePrevious and\
				   obj.simplePrevious.simplePrevious and\
				   obj.simplePrevious.simplePrevious.name == "SUIVANT":
					fieldHeader[9] = u"Jour de début"
					self.notSearch = 1
				elif obj.simpleNext and\
				     obj.simpleNext.simpleNext and\
				     obj.simpleNext.simpleNext.windowControlID == 11 and (
				         not obj.simpleNext.simpleNext.simpleNext
				         or obj.simpleNext.simpleNext.simpleNext.simpleNext
				         and not obj.simpleNext.simpleNext.simpleNext.simpleNext.simpleNext):
					fieldHeader[9] = "Jour de fin" if self.notSearch else "Jour de recherche"
				else:
					fieldHeader[9] = u"Jour du pense-bête" if (obj.simpleNext
					                                           and obj.simpleNext.simpleNext
					                                           and obj.simpleNext.simpleNext.simpleNext
					                                           and not obj.simpleNext.simpleNext.simpleNext.simpleNext) or (
					    obj.simpleNext
					    and obj.simpleNext.simpleNext
					    and obj.simpleNext.simpleNext.simpleNext
					    and obj.simpleNext.simpleNext.simpleNext.simpleNext
					    and obj.simpleNext.simpleNext.simpleNext.simpleNext.simpleNext
					    and not obj.simpleNext.simpleNext.simpleNext.simpleNext.simpleNext.simpleNext
					) else "Jour du rendez-vous"
			obj.name = fieldHeader[controlID]
		nextHandler()

	def script_searchDate(self, gesture):
		gesture.send()
		self.notSearch = 0

	__gestures = {
		"kb:control+j": "searchDate"
	}
