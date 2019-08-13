import discord
from translate import translate
import random

TOKEN = ''

client = discord.Client()

translator = translate.Translator()


def duke(message):
    print ('message from the duke{0}'.format(message))
    _message = ''
    for word in str.split(message, ' '):
        replace_pos = random.randint(0, len(word)-1)
        replace_val = chr(random.randint(96, 122))
        word_list = list(word)
        word_list[replace_pos] = replace_val
        _message += "".join(word_list) + ' '
    return _message

    '''elif 'shades' in str(message.author):
        original_message = ' '.join(str.split(message.content, ' '))
        final_message = duke(original_message)
        response = ('Original: {0}\n Translated for Duke: {1}'.format(original_message,
                    final_message))
        await client.send_message(message.channel, response)'''

@client.event
async def on_message(message):
    response = ""
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
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
