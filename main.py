import discum
import requests

# NjA0MDkyODU0MTU0OTUyNzI1.GDBqXg.U6eY4us3VoO6U8A2I58iDaPTm6ZJBQYMWPe2cQ
bot = discum.Client(token='NjA0MDkyODU0MTU0OTUyNzI1.GDBqXg.U6eY4us3VoO6U8A2I58iDaPTm6ZJBQYMWPe2cQ', log=False)
print('start')


@bot.gateway.command
def helloworld(resp):
    if resp.event.ready_supplemental:  # ready_supplemental is sent after ready
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
    if resp.event.message:
        m = resp.parsed.auto()
        channelID = m['channel_id']
        username = m['author']['global_name']
        content = m['content']

        auth = "7091412712:AAHjB0wo5YUVtO1WqO4YZ1JfVu6xIiXfAsY"
        chatID = "-1002002524193"
        chatID2 = '-1002124240271'

        if channelID == '924670321674567760':
            msg = "LT by cryptomannn: #announcements \n User: {} \n Msg: {}".format(username, content)
            res = requests.post(f"https://api.telegram.org/bot{auth}/sendMessage?chat_id={chatID}&text={msg}")
            print(res.status_code, res.text)
            print(msg)

        elif channelID == '952634257493340180':
            msg = "LT by cryptomannn: #cryptomannn \n User: {} \n Msg: {}".format(username, content)
            res = requests.post(f"https://api.telegram.org/bot{auth}/sendMessage?chat_id={chatID}&text={msg}")
            print(res.status_code, res.text)
            print(msg)

        elif channelID == '1153350410908741732':
            msg = "LT by cryptomannn: #patrick \n User: {} \n Msg: {}".format(username, content)
            res = requests.post(f"https://api.telegram.org/bot{auth}/sendMessage?chat_id={chatID}&text={msg}")
            print(res.status_code, res.text)
            print(msg)

        elif channelID == '1143443558607626241':
            msg = "LT by cryptomannn: #decipher \n User: {} \n Msg: {}".format(username, content)
            res = requests.post(f"https://api.telegram.org/bot{auth}/sendMessage?chat_id={chatID}&text={msg}")
            print(res.status_code, res.text)
            print(msg)

        elif channelID == '1204730189821775912':
            msg = "Ken Discord: #bertra-analysis \n User: {} \n Msg: {}".format(username, content)
            res = requests.post(f"https://api.telegram.org/bot{auth}/sendMessage?chat_id={chatID2}&text={msg}")
            print(res.status_code, res.text)
            print(msg)

        elif channelID == '974715255223648306':
            msg = "Ken Discord: #bertra-trades \n User: {} \n Msg: {}".format(username, content)
            res = requests.post(f"https://api.telegram.org/bot{auth}/sendMessage?chat_id={chatID2}&text={msg}")
            print(res.status_code, res.text)
            print(msg)

        elif channelID == '1195004358102888560':
            msg = "Ken Discord: #ken-analysis \n User: {} \n Msg: {}".format(username, content)
            res = requests.post(f"https://api.telegram.org/bot{auth}/sendMessage?chat_id={chatID2}&text={msg}")
            print(res.status_code, res.text)
            print(msg)

        elif channelID == '1194403432640032809':
            msg = "Ken Discord: #ken-trades \n User: {} \n Msg: {}".format(username, content)
            res = requests.post(f"https://api.telegram.org/bot{auth}/sendMessage?chat_id={chatID2}&text={msg}")
            print(res.status_code, res.text)
            print(msg)

        else:
            print('wrong channel')

        # msg = "Channel: {} \n User: {} \n Msg: {}".format(channelID, username,  content)
        # res = requests.post(f"https://api.telegram.org/bot{auth}/sendMessage?chat_id={chatID}&text={msg}")
        # print(res.status_code, res.text)
        # print(msg)


bot.gateway.run(auto_reconnect=True)

# Authorization: NzMyMjkxNTE1MzY3NDI0MDMx.GSfP_T.H3zHoDd0LfgKtMOWiAw2iLtLlQPFXtpqPpX5Xk
# bot.run("MTIzMTk2MTQ3MTk4NzIyMDU2MQ.GBRKmY.YA7DIBZdq4bZWGXSfNNatn1PdsUCTpszxTnB3o")
# auth = "7091412712:AAHjB0wo5YUVtO1WqO4YZ1JfVu6xIiXfAsY"  # the token that you received from BotFather.
# chatID = "-1002002524193"  # id of the telegram channel to forward the message to.
