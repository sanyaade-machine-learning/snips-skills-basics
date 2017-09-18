import datetime
import threading
import sys
import itertools
import json
import pygame
import random
import clock
import audioplayer

alarms = None;

"""
api to support alarm clock intents with file based persistence of alarms between requests
"""
class AlarmClock:
	
	 def __init__(self, db_file_path,tts_service=None):
        """ Initialisation.
        :param db: the json database.
        :param tts_service: A TTS service, i.e. an object which has a
                            `speak(text)` method for speaking the result.
        """
        self.tts_service = tts_service
        with open(db_file_path, 'r') as f:
            db = json.loads(f.read().replace('\n', ''))
            if db:
                self.alarms = db["alarms"]
	
	def: write_alarms()
		with open(db_file_path, 'r+') as f:
			f.write(json.dumps(self.alarms))

	
	def: add_alarm(time,description='',duration=0):
		sys.stdout.write('add alarm\n')
		self.tts_service.speak('add alarm\n')
		sys.stdout.write(time)
		sys.stdout.write(description)
		sys.stdout.flush()
		self.alarms.append([time,description])
		write_alarms()
	
	def: what_is_the_time(time,description=''):
		sys.stdout.write('what is the time\n')
		sys.stdout.write(time.strftime('%X %x'))
		self.tts_service.speak(time.strftime('%X %x'))
		sys.stdout.flush()
	
	def: cancel_alarm(time,description=''):
		sys.stdout.write('cancel alarm\n')
		self.tts_service.speak('cancel alarm\n')
		sys.stdout.write(time)
		sys.stdout.write(description)
		sys.stdout.flush()
		write_alarms()
	
	def: cancel_all_alarms():
		sys.stdout.write('cancel all alarm\n')
		self.tts_service.speak('cancel all alarm\n')
		sys.stdout.flush()
		write_alarms()
	
	def: list_alarms():
		sys.stdout.write('list alarms\n')
		sys.stdout.write(self.alarms);
		self.tts_service.speak('list alarms\n')
		sys.stdout.flush()







