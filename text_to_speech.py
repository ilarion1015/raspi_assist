from os import system


def synthesize_speech(text):
	system(f"spd-say -o rhvoice -y Aleksandr -r 20 -w \"{text}\"")
