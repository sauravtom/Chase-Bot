

import wikipedia
import os
import pyvona
import re

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
v = pyvona.create_voice('GDNAJJ2TZFHSNAJAEYHA', 'vOgSfcz88uZxElIU2K5PLAgWfIJiajojTg81Wla1')


def summarize(text):
	text = text.split('.')[:3]
	text = ".".join(text)
	#remove text in round brackets and square brackets
	text = re.sub(r'\([^)]*\)', '', text)
	text = re.sub(r'\[[^)]*\]', '', text)
	return text

def wikivideo(query='New York'):
	ny = wikipedia.page(query)
	content = ny.content
	summary = summarize(content)
	
	download_images(query,6)

	generate_voice(summary)

	#bake the oven
	

def donwload_images(query,number='6'):
	os.system('rm %s/oven/*'%(DIR_PATH))
	os.system('node download_images.js "%s" %s'%(query,number))

def generate_voice(text='hello world'):
	v.codec = 'mp3'
	v.voice_name = 'Raveena'
	v.fetch_voice(text, '%s/oven/narration'%(DIR_PATH))



if __name__ == '__main__':
	print summarize("asdasdasdasd(123).asdas[123123]dasdasd.asdasdasd.asdasd.123142134.234234234.234234423")
	#generate_voice()
	#wikivideo()