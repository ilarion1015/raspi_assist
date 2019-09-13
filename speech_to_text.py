from pocketsphinx.pocketsphinx import Decoder
from sphinxbase.sphinxbase import Jsgf

from speech_recognition import Recognizer, Microphone
from pydub import AudioSegment

from os import system


class SphinxDecoder():

	def __init__(self):
		self.MODELDIR = 'speech/'
		self.wav_name = 'media/temp.wav'
		self.raw_name = 'media/temp.raw'

		config = Decoder.default_config()
		config.set_string('-hmm', self.MODELDIR + 'ru_ru/')
		config.set_string('-dict', self.MODELDIR + 'ru.dic')
		self.decoder = Decoder(config)

		jsgf = Jsgf(self.MODELDIR + 'gr.gram')
		rule = jsgf.get_rule('gr.rule')
		fsg = jsgf.build_fsg(rule, self.decoder.get_logmath(), 7.5)
		fsg.writefile('gr.fsg')

		self.decoder.set_fsg('gr', fsg)
		self.decoder.set_search('gr')

		self.rec = Recognizer()
		self.mic = Microphone()


	def wav_to_raw(self):
		audio_file = AudioSegment.from_wav(self.wav_name)
		audio_file = audio_file.set_frame_rate(16000)
		audio_file.export(self.raw_name, format = 'raw')


	def record_audio(self):
		with self.mic as source:
			self.rec.adjust_for_ambient_noise(source)
			
			system('aplay media/beep.wav')
			audio = self.rec.listen(source)
			with open(self.wav_name, 'wb') as new_audio:
				new_audio.write(audio.get_wav_data())

		self.wav_to_raw()


	def get_from_audio(self):
		self.record_audio()

		self.decoder.start_utt()
		stream = open(self.raw_name, 'rb')
		while True:
			buf = stream.read(1024)
			if buf:
				self.decoder.process_raw(buf, False, False)
			else:
				break
		self.decoder.end_utt()
		stream.close()
		try:
			return self.decoder.hyp().hypstr
		except:
			return None
