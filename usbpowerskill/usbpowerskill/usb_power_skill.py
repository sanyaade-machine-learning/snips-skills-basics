class UsbPowerSkill:
	
	 def __init__(self,tts_service=None):
        """ Initialisation.
        :param db: the json database.
        :param tts_service: A TTS service, i.e. an object which has a
                            `speak(text)` method for speaking the result.
        """
        self.tts_service = tts_service

	def turn_on(usbPortIdentifier):
		if self.tts_service:
			self.tts_service.speak(_("Turned on {}").format(usbPortIdentifier))
		
	def turn_off(usbPortIdentifier):
		if self.tts_service:
			self.tts_service.speak(_("Turned off {}").format(usbPortIdentifier))
		
