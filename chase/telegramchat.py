import sys
import time
import telepot
import os
TOKEN = '236674506:AAE5x3lGw0VRSY0Let2EdO9-ZLIVZYqQnzY'

bot = telepot.Bot(TOKEN)


def query_video(query):
    os.system('sudo python /home/saurav/gyanvani/chase/video_maker.py ' + query) 
    query = query.replace (" ", "_")
    return "/home/saurav/gyanvani/chase/oven/" + query + "/0final.mp4"
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg['text']
    text = text.lower()
    if len(text) > 7 and text[0:6] == "/video":
	query = text[7:]
        bot.sendMessage(chat_id, 'Retrieving your video for {}'.format(query))
        bot.sendChatAction(chat_id, 'upload_video')
        video_file = query_video(query)
	try:
            f = open(video_file, 'rb')
            print 'Chat Message: {}'.format(text)
            bot.sendVideo(chat_id, f, caption=query)
            print 'video sent'
        except IOError:
	    bot.sendMessage(chat_id, 'Oops, no videos of {} found'.format(query))
    else:
	bot.sendMessage(chat_id, 'Type "/video <query>" to generate a video clip!')

bot.message_loop({'chat': on_chat_message})
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
