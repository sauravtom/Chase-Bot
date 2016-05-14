

import wikipedia
import os
import pyvona
import re

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
NUMBER_OF_IMAGES = 3
UNDERCOLOR = 'rgba(0,0,0,0.3)'
FILLCOLOR = 'rgba(251,251,255)'
FONT_LOC = '%s/design_assets/TisaPro.otf'%DIR_PATH

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
	
	download_images(query,NUMBER_OF_IMAGES)

	generate_voice(summary)

	#bake the oven


def bake():
	for counter in range(NUMBER_OF_IMAGES):
		title = 'food chamber'
		#normalize the dimensions of the png files
		os.system("convert %s/oven/slide_%s.png \( -clone 0 -blur 0x15 -resize 480x480\! \) \( -clone 0 -resize 480x480 \) -delete 0 \
		    -gravity center -compose over -composite %s/oven/slide_%s.png"%(DIR_PATH,counter,DIR_PATH,counter))

		#generate caption files
		os.system("convert -size %sx%s -background 'rgba(154,78,225,0.4)' -font %s \
		    -fill '%s' -gravity West  \
		    -bordercolor 'rgba(154,78,225,0.4)' -border 25x25 \
		 caption:'%s' -flatten %s/oven/caption_%s.png"%(375,HEIGHT/3-70,FONT_LOC,FILLCOLOR,title.upper(),DIR_PATH,counter))

		os.system("composite -gravity South %s/oven/caption_%s.png %s/oven/insta/slide_%s.png %s/oven/insta/slide_%s.png"%(DIR_PATH,counter,DIR_PATH,counter,DIR_PATH,counter))

		os.system("./newsmeme_asset/transitions -m dissolve -f 21 -d 10 -p 10 \
		    -e %s/oven/slide_%s.png %s/oven/slide_%s.png %s/design_assets/maskfile.png \
		    %s/oven/trans_%s.gif"%(DIR_PATH,counter,DIR_PATH,counter+1,DIR_PATH,DIR_PATH,counter))

		#insta strech 
		os.system('convert -delay %sx1 %s/oven/tempgif_%s.gif \
		    %s/oven/strech_%s.gif'%(item['time']-1,DIR_PATH,counter,DIR_PATH,counter))

	  
		#insta: add transition to strenched(slow) gif
		os.system('convert %s/oven/strech_%s.gif %s/oven/trans_%s.gif \
		    %s/oven/strech_%s.gif'%(DIR_PATH,counter,DIR_PATH,counter,DIR_PATH,counter))
		

	#out of the loop

	os.system('convert %s/oven/strech_*.gif %s/oven/final.gif'%(DIR_PATH,DIR_PATH))

	os.system("ffmpeg -i %s/oven/final.gif -vcodec libx264 -vf 'scale=trunc(iw/2)*2:trunc(ih/2)*2' \
	    -pix_fmt yuv420p -movflags +faststart %s/oven/final.mp4"%(DIR_PATH,DIR_PATH))
		



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