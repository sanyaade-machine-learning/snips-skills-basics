class ArithmeticSkill:
	
	 def __init__(self,tts_service=None):
        """ Initialisation.
        :param db: the json database.
        :param tts_service: A TTS service, i.e. an object which has a
                            `speak(text)` method for speaking the result.
        """
        self.tts_service = tts_service

	def solve(numberA,numberB,operator):
		
		result=None
		
		if numberA != None and numberB != None:
			if operator == 'plus':
				result = numberA + numberB
			elif operator == 'minus':
				result = numberA - numberB
			elif operator == 'multiplied by':
				result = numberA * numberB
			elif operator == 'divided by':
				result = numberA / numberB
		
		return result;
		
	def solve_and_say(numberA,numberB,operator):
		result = solve(numberA,numberB,operator)
		if result != None:
			if self.tts_service:
				self.tts_service.speak(_("The answer is {}").format(result))
		
