from speech.snow_lib.snowboydecoder import HotwordDetector
from speech_to_text import SphinxDecoder
from text_to_speech import synthesize_speech
from com_port import open_serial

from logic import answer
from oled import update_disp

snow_decoder = None
sphinx_decoder = None


def main():
	global snow_decoder
	setup()
	while True:
		print('[WARNING] SNOWBOY STARTING')
		snow_decoder.start(detected_hotword)
		execute_cmd()


def setup():
	global snow_decoder, sphinx_decoder

	snow_decoder = HotwordDetector('speech/hotword.pmdl', sensitivity=0.5, audio_gain=1)
	sphinx_decoder = SphinxDecoder()

	try:
		open_serial()
	except:
		print('[WARNING] PORT IS NOT OPEN')


def detected_hotword():
	global snow_decoder

	print('[WARNING] SNOWBOY TERMINATED')
	snow_decoder.terminate()


def execute_cmd():
	global sphinx_decoder

	cmd = sphinx_decoder.get_from_audio()
	print(f"[YOU SAID] {cmd}")
	if cmd != None:
		ans = answer(cmd)
		print(f"[ANSWER] {ans[1]}")
		if ans != None:
			update_disp(ans[0])
			synthesize_speech(ans[1])


if __name__ == '__main__':
	main()
