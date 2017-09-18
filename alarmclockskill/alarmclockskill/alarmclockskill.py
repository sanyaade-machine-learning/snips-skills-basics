import datetime
import threading
import sys
import itertools
import json
import pygame
import random

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



def ring_ring():
    sys.stdout.write('ring ring\n')
    # start audio player beeps
    self.tts_service.speak('ring ring\n')
    sys.stdout.flush()



class Clock:

    def __init__(self):
        self.alarm_time = None
        self._alarm_thread = None
        self.update_interval = 1
        self.event = threading.Event()

    def run(self):
        while True:
            self.event.wait(self.update_interval)
            if self.event.isSet():
                break
            now = datetime.datetime.now()
            if self._alarm_thread and self._alarm_thread.is_alive():
                alarm_symbol = '+'
            else:
                alarm_symbol = ' '
            sys.stdout.write("\r%02d:%02d:%02d %s" 
                % (now.hour, now.minute, now.second, alarm_symbol))
            sys.stdout.flush()

    def set_alarm(self, hour, minute):
        now = datetime.datetime.now()
        alarm = now.replace(hour=int(hour), minute=int(minute))
        delta = int((alarm - now).total_seconds())
        if delta <= 0:
            alarm = alarm.replace(day=alarm.day + 1)
            delta = int((alarm - now).total_seconds())
        if self._alarm_thread:
            self._alarm_thread.cancel()
        self._alarm_thread = threading.Timer(delta, ring_ring)
        self._alarm_thread.daemon = True
        self._alarm_thread.start()



class AudioPlayer:
    """ A simple audio player."""

    @staticmethod
    def play(filename, on_done):
        """ Play a file.

        :param filename: the path to the audio file to play.
        :param on_done: callback to execute when playing is done.
        """
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        if on_done:
            on_done()

    @staticmethod
    def stop():
        """ Stop the player. """
        pygame.mixer.init()
        pygame.mixer.music.stop()

    @staticmethod
    def pause():
        """ Pause the player. """
        pygame.mixer.init()
        pygame.mixer.music.pause()

    @staticmethod
    def resume():
        """ Resume the player. """
        pygame.mixer.init()
        pygame.mixer.music.unpause()


#clock = Clock()
#clock.set_alarm(sys.argv[1], sys.argv[2])
#clock.run()



