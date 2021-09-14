# -*- coding: UTF-8 -*-

# installTasks.py.

import config

def onInstall():
	if not config.conf["presentation"]["reportObjectDescriptions"]:
		config.conf["presentation"]["reportObjectDescriptions"] = True
	config.conf.save()
