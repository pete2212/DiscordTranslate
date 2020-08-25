import discord
from translate import translate
import random
import urllib.request as urllib2
import json

# insert token for connecting server to your app
TOKEN = ''

client = discord.Client()

translator = translate.Translator()


def find_value(id, json_repr):
    result = []

    def _decode_dict(a_dict):
        try:
            result.append(a_dict[id])
            print('result{0}'.format(result))
        except KeyError:
            pass
        return a_dict
    json.loads(json_repr.decode('utf-8'), object_hook=_decode_dict)
    return result


def duke(message):
    print('message from Yos (in memory of Duke) {0}'.format(message))
    _message = ''
    for word in str.split(message, ' '):
        replace_pos = random.randint(0, len(word)-1)
        replace_val = chr(random.randint(96, 122))
        word_list = list(word)
        word_list[replace_pos] = replace_val
        _message += "".join(word_list) + ' '
    return _message



@client.event
async def on_message(message):
    response = ""
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
#    elif 'Yosarian' in str(message.author):
#        response = urllib2.urlopen('https://api.giphy.com/v1/gifs/random?api_key=DjUXXUryOBCEDhvp3VFRVPOwIn0WQmy8&tag=panda&rating=G')
#        html = response.read()
#        val = find_value('downsized_medium', html)
#        print(val)
#        _url = val[0]['url']
#        if _url:
#            m = discord.Embed(title='Panda', description='A panda for Yos!')
#            m.set_image(url=_url)
#        await client.send_message(message.channel, embed=m)
    elif 'Waffles' in str(message.author):
        response = urllib2.urlopen('https://api.giphy.com/v1/gifs/random?api_key=DjUXXUryOBCEDhvp3VFRVPOwIn0WQmy8&tag=dog&rating=G')
        html = response.read()
        val = find_value('downsized_medium', html)
        print(val)
        _url = val[0]['url']
        if _url:
            m = discord.Embed(title='Dog Attack!', description='Doggy')
            m.set_image(url=_url)
        await client.send_message(message.channel, embed=m)
    elif 'Stan' in str(message.author):
        response = urllib2.urlopen('https://api.giphy.com/v1/gifs/random?api_key=DjUXXUryOBCEDhvp3VFRVPOwIn0WQmy8&tag=disney&rating=G')
        html = response.read()
        val = find_value('downsized_medium', html)
        print(val)
        _url = val[0]['url']
        if _url:
            m = discord.Embed(title='Disney Fun', description='A little piece of Disney for a Disney fanatic!')
            m.set_image(url=_url)
        await client.send_message(message.channel, embed=m)

#        original_message = ' '.join(str.split(message.content, ' '))
#        final_message = duke(original_message)
#        response = ('Original: {0}\n Translated for Yos (in memory of duke): {1}'.format(original_message,
#                    final_message))
#        await client.send_message(message.channel, response)
    elif 'Hatter' in str(message.author):
        pass
        #images = ['https://i.imgur.com/vMIqEzR.jpg',
        #          'https://i.imgur.com/7J5nBQU.jpg',
        #          'https://i.imgur.com/8i4G5fu.jpg',
        #          'https://i.imgur.com/3OnXpti.jpg',
        #          'https://i.imgur.com/AgnfCDW.jpg',
        #          'https://i.imgur.com/lvus6nG.jpg',
        #          'https://i.imgur.com/vtm1OOU.jpg',
        #          'https://i.imgur.com/YL69Kfl.jpg',
         #         'https://i.imgur.com/w91M0Im.jpg',
        # #         #'https://imgur.com/rGzFguF',
        #          'https://media.giphy.com/media/b9Mh5pHmoFk88/giphy.gif',
        #          'https://i.imgur.com/HRYTFG2.jpg',
        #          'https://i.imgur.com/F4wC2rm.jpg']
        #_url = images[random.randint(0, len(images)-1)]
        #m = discord.Embed(title='Hatter', description='A hatter for hatter!')
        #m.set_image(url=_url)
        #print(_url)
        #await client.send_message(message.channel, embed=m)
    elif message.content.startswith('-t'):
        language = str.split(message.content, ' ')[1]
        if language == 'duke':
            original_message = ' '.join(str.split(message.content, ' ')[2:])
            final_message = duke(original_message)
            response = ('Original: {0}\n Translated: {1}'.format(original_message,
                        final_message))
        else:
            final_message = ' '.join(str.split(message.content, ' ')[2:])
            response = (u'Original: {0}\n Translated: {1}'.format(final_message,
                        translator.translate(final_message, language)['translatedText']))
        print('response: {0}'.format(response))

        await client.send_message(message.channel, response)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
