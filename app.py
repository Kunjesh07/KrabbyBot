#Copyright (c) 2020 kunjesh07

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from flask import Flask, request
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse
from googletrans import Translator

app = Flask(__name__)

@app.route("/")
def hello():
    return "Status Online"

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    #print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'about' in incoming_msg or 'About' in incoming_msg:
        text = f' 🎯🎯Developed and created by *KUNJESH PATEL* 📌📌\n*✉️© 2020 KUNJESH PATEL.  All rights reserved.*📝 '
        msg.body(text)
        responded = True

    
    if 'start' in incoming_msg or 'Start' in incoming_msg:
        text = f'🤖 _Hello I Am a Krabby Bot, how Can I Help You?_\n\n*Admin :*\n\n📞 : +917041436016\n📱 : _fb.me/kunjesh.patel.37_ \n\n🚀 *Features* \n\n✅ _Youtube Downloader_ \n✅ _Facebook Downloader_ \n✅ _Instagram Downloader_ \n✅ _Google Search_ \n✅ _Text To Speech_ \n✅ _Stalking Profil Instagram_ \n✅ _Translate_ \n\n\n _To Display Command Type_ *Menu*'
        msg.body(text)
        responded = True
    if 'info-covid' in incoming_msg or 'Info-covid' in incoming_msg:
        import requests as r, json
        req = r.get('https://coronavirus-19-api.herokuapp.com/countries/india')
        reqq = r.get('https://coronavirus-19-api.herokuapp.com/countries/world')
        jss = reqq.json()
        js = req.json()
        text = f'*Info Coronavirus India*\n\n\n*Positive* : {js["cases"]} \n*Recovred* : {js["recovered"]} \n*Died* : {js["deaths"]}  \n\n\n*Global* \n\n\n*Positive* : {jss["cases"]} \n*Recovered* : {jss["recovered"]} \n*Died* : {jss["deaths"]}'
        msg.body(text)
        responded = True
    
    if 'Menu' in incoming_msg or 'menu' in incoming_msg:
        text = f'⌨️ *List Of Command :*  \n\n🔥 *info-covid* (Information of COVID-19) \n\n🔥 */JS* _<kota>_ Prayer time  \n\n🔥 *Schedule* _Display Schedule_ \n\n🔥 */SY* _<url>_ : Youtube Search\n\n🔥 */YT* _<url>_ : Youtube Downloader\n\n🔥 */FB* _<url>_ : Facebook Downloader\n\n🔥 */IG* _<url>_ : Instagram Downloader\n\n🔥 */FL* _<url>_ : Download Big Size Fb Videos\n\n🔥 */GL* _<query>_ : Google Search\n\n🔥 */SG* _<usrname>_ : Get Info Instagram\n\n🔥 */TTS* <Text> : Text To Speech\n\n🔥 */TR-id-en* _<text>_ : Translate ID > ENG\n\n🔥 */TR-en-id* _<text>_ : Translate ENG > ID\n\n🔥 */TR-id-kor* _<text>_ : Translate ID > Korea\n\n🔥 */TR-kor-id* _<text>_ : Translate Korea > ID\n\n🔥 *help* : How to use the command'
        msg.body(text)
        responded = True
        
    if '/FB' in incoming_msg:
        import requests as r
        import re
        par = incoming_msg[3:]
        html = r.get(par)
        video_url = re.search('sd_src:"(.+?)"', html.text).group(1)
        msg.media(video_url)
        responded = True
    
    if '/IG' in incoming_msg:
        import requests as r
        par = incoming_msg[3:]
        a = r.get(par+'?__a=1')
        b = a.json()
        c = b['graphql']['shortcode_media']
        d = (c['video_url']) 
        msg.media(d)
        responded = True  
        
    if '/GL' in incoming_msg:
        from googlesearch import search
        query = incoming_msg[3:]
        for i in search(query, tld="com", num=10, stop=10, pause=2):
            text = f'==========Results==========\n\n *Chorus* : '+i
            msg.body(text)
            responded = True
            
    if '/TR-en-id' in incoming_msg:
        par = incoming_msg[9:]
        translator = Translator()
        result = translator.translate(par, src='en', dest='id')
        msg.body(result.text)
        responded = True

    if '/TR-id-en' in incoming_msg:
        par = incoming_msg[9:]
        translator = Translator()
        result = translator.translate(par, src='id', dest='en')
        msg.body(result.text)
        responded = True

    if '/TR-id-kor' in incoming_msg:
        par = incoming_msg[10:]
        translator = Translator()
        result = translator.translate(par, src='id', dest='ko')
        msg.body(result.text)
        responded = True

    if '/TR-kor-id' in incoming_msg:
        par = incoming_msg[10:]
        translator = Translator()
        result = translator.translate(par, src='ko', dest='id')
        msg.body(result.text)
        responded = True

    if '/FL' in incoming_msg:
        import requests as r
        import re
        par = incoming_msg[3:]
        html = r.get(par)
        video_url = re.search('sd_src:"(.+?)"', html.text).group(1)
        reqq = r.get('http://tinyurl.com/api-create.php?url='+video_url)
        msg.body('*Video works on Convert...*\n\nLINK : ')
        responded = True
        
    if '/TTS' in incoming_msg:
        par = incoming_msg[5:]
        msg.media('https://api.farzain.com/tts.php?id='+par+'&apikey=JsaChFteVJakyjBa0M5syf64z&')
        responded = True

    if '/SG' in incoming_msg:
        import requests 
        import json
        par = incoming_msg[4:]
        p = requests.get('https://farzain.com/api/ig_profile.php?id='+par+'&apikey=IGQVJVRFNHY0ZAsU3M0akx5ckFfRFZAVcUk0THlWV2RaT21WcnNhVXpZAa1lUNGs3R1ZAxSWpRR0p2TTY2X1FYbEpRS2pDb21jUU9DOFR0ZAGdzeDgzMkhfcUhzejZA3ci1HbHJpdW5QNG01M01vVzgzVUhnMgZDZD')
        js = p.json()['info']
        ms = (js['profile_pict'])
        jp = p.json()['count']
        text = f'Name : *{js["full_name"]}* \nUsername : {js["username"]} \nBio : *{js["bio"]}* \nWebsite : *{js["url_bio"]}* \nFollowers : *{jp["followers"]}* \nFollowing : *{jp["following"]}* \nTotal Posts : *{jp["post"]}* '
        msg.body(text)
        msg.media(ms)
        responded = True

    if '/YT' in incoming_msg:
        import pafy
        import requests as r
        par = incoming_msg[4:]
        audio = pafy.new(par)
        gen = audio.getbestaudio(preftype='m4a')
        genn = audio.getbestvideo(preftype='mp4')
        req = r.get('http://tinyurl.com/api-create.php?url='+gen.url)
        popo = r.get('http://tinyurl.com/api-create.php?url='+genn.url)
        msg.body('_=========================_\n\n     _Video Converted Successfully_\n\n_=========================_\n\n''*'+gen.title+'*''\n\n*Link Download Music* :' +req.text+'\n\n*Link Download Video* :' +popo.text)
        responded = True
        
    if '/SY' in incoming_msg:
        import requests as r
        par = incoming_msg[3:]
        req = r.get('http://api.farzain.com/yt_search.php?id='+par+'&apikey=JsaChFteVJakyjBa0M5syf64z&')
        js = req.json()[1]
        text = f'*Title* :  _{js["title"]}_ \n\n*Url Video* : _{js["url"]}_\n\n*Video ID* : _{js["videoId"]}\n\n_Note : if you want to Download this video or convert it to music, copy the link above and use the command./YT_'
        msg.body(text)
        msg.media((js['videoThumbs']))
        responded = True
  
    if '/JS' in incoming_msg:
       import requests as r
       par = incoming_msg[3:]
       req = r.get('http://api.farzain.com/shalat.php?id='+par+'&apikey=JsaChFteVJakyjBa0M5syf64z&')
       js = req.json()['respon']
       text = f'*Prayer times* \n\n*Dawn*  : {js["shubuh"]} \n*Dzuhur* : {js["dzuhur"]} \n*Ashar*   : {js["ashar"]} \n*Magrib*  : {js["maghrib"]} \n*Isya*    : {js["isya"]}'
       msg.body(text)
       responded = True

    if 'Schedule' in incoming_msg:
       msg.media('https://user-images.githubusercontent.com/74760068/102241016-82258d80-3f1e-11eb-8c71-6e0176c2739c.png')

       responded = True

    if 'help' in incoming_msg:
       text = f'💻 *Help For Instagram*\n\n/IG <Link Video> Example : \n/IG https://www.instagram.com/p/BWhyIhRDBCw/\n\n\n*Note* : Link Must Look Like In Example If the Link Suffix Is There? Utm_source = ig_web_copy_link remove that part\n\n 💻 *Help For Facebook*\n\n/FB _link video_ Ecample :\n\n/FB https://www.facebook.com/100010246050928/posts/1143182719366586/?app=fbl \n\n💻 *Help For Google Search* \n\n /GL <Query> Example :  \n\n/GL CHARUSAT \n\n💻 *Help For Instagram Stalking \n\n/SG <username> Example : \n\n/SG kunj \n\n💻 *Help For Translate* \n\nTR-id-en Translate Indonesian to English\n\n/TR-en-id Translate English to Indonesian\n\n/TR-id-kor Translate Indonesian to Korean \n\n/TR-kor-id Translate Korean to Indonesian \n\n💻 *Help For Text To Speech* \n\n/TTS WhatsappBotKrabby\n\nIf you want to use space, replace it with% 20\n\nExample : /TTS Whatsapp%20Bot%Krabby'
       msg.body(text)
       responded = True
    
    if '!' in incoming_msg:
       import requests as r
       us = incoming_msg[2:]
       import requests
       import json
       url = 'https://wsapi.simsimi.com/190410/talk/'
       body = {
         'utext': us, 
         'lang': 'id',
         'country': ['ID'],
         'atext_bad_prob_max': '0.7'

        }
       headers = {
         'content-type': 'application/json', 
         'x-api-key': 'LKgWy5I-HoG8K0CmpWl.SNncus1UOpwBiA1XAZzA'
         }
       r = requests.post(url, data=json.dumps(body), headers=headers)
       js = r.json()
       msg.body(js['atext'])
       responded = True

       

    if responded == False:
        msg.body('Sorry, I just bots don\'t recognize that command :), please send start to go to the menu')

    return str(resp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
