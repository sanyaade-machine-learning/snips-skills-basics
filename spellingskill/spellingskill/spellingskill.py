class SpellingSkill:
	
	 def __init__(self,tts_service=None):
        """ Initialisation.
        :param db: the json database.
        :param tts_service: A TTS service, i.e. an object which has a
                            `speak(text)` method for speaking the result.
        """
        self.tts_service = tts_service

	def spell(wordToSpell):
		
		if self.tts_service:
			self.tts_service.speak(_("{} is spelled {}").format(wordToSpell," ".join(list(wordToSpell))))
		
