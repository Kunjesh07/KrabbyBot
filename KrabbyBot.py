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

#LICENSE   = MIT GutHub
#__author__= KUNJESH PATEL
#__email___= kunjesh137@gmail.com
#__Year____= 2020
#Version___= 1.1.0

from flask import Flask, request, jsonify
import json
import requests
from twilio.twiml.messaging_response import MessagingResponse
from googletrans import Translator
import wikipedia
import datetime



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
        text = f' 🎯🎯Created and Developed by *KUNJESH PATEL* 📌📌\n*✉️© 2020 KUNJESH PATEL.  All rights reserved.*📝 '
        msg.body(text)
        responded = True

    
    if 'start' in incoming_msg or 'Start' in incoming_msg:
        text = f'🤖 _Hello I Am a Krabby Bot, how Can I Help You?_\n\n*Admin :*\n\n📞 : +917041436016\n📱 : _fb.me/kunjesh.patel.37_ \n\n🚀 *Features*\n\n✅ _Covid-19 info_\n✅ _Youtube Downloader_ \n✅ _Facebook Downloader_ \n✅ _Google Search_ \n✅ _Text To Speech_ \n✅ _wiki Search_\n✅ _weather Information_\n✅ _Quote_\n\n--------------------------------------------------------------------\n\n🎯 *Upcoming features* 🎯\n\n✅ _Stackoverflow query finder_\n✅ _Translator_\n✅ _Voice based query_\n✅ _Torrent link to Google drive link or normal link_\n✅ _Device based location in longitude and latitude_\n✅ _Instagram video Downloader_\n✅ _stocking instagram profile_\n✅ _News_\n\n--------------------------------------------------------------------\n\n_To Display Command Type_ *Menu*\n\n_To help for Command Type_ *Help or help*' 
        msg.body(text)
        responded = True
    if 'info-covid' in incoming_msg or 'Info-covid' in incoming_msg:
        import requests as r, json
        req = r.get('https://coronavirus-19-api.herokuapp.com/countries/india')
        res = r.get('https://coronavirus-19-api.herokuapp.com/countries/Russia')
        reu = r.get('https://coronavirus-19-api.herokuapp.com/countries/USA')
        reqq = r.get('https://coronavirus-19-api.herokuapp.com/countries/world')
        jss = reqq.json()
        js= req.json()
        jsr = res.json()
        jsu = reu.json()
        text = f'*Info Coronavirus India 🇮🇳*\n\n*Positive* : {js["cases"]} \n*Recovred* : {js["recovered"]} \n*Died* : {js["deaths"]} \n*Today cases* : {js["todayCases"]} \n*Today died* : {js["todayDeaths"]} \n*critical* : {js["critical"]} \n*casesPerOneMillion* : {js["casesPerOneMillion"]} \n*deathsPerOneMillion* : {js["deathsPerOneMillion"]} \n*totalTests* : {js["totalTests"]} \n*TestsPerMillion*: {js["testsPerOneMillion"]}\n\n\n*Info Coronavirus USA 🇺🇸*\n\n*Positive* : {jsu["cases"]} \n*Recovred* : {jsu["recovered"]} \n*Died* : {jsu["deaths"]} \n*Today cases* : {jsu["todayCases"]} \n*Today died* : {jsu["todayDeaths"]} \n*critical* : {jsu["critical"]} \n*casesPerOneMillion* : {jsu["casesPerOneMillion"]} \n*deathsPerOneMillion* : {jsu["deathsPerOneMillion"]} \n*totalTests* : {jsu["totalTests"]} \n*TestsPerMillion*: {jsu["testsPerOneMillion"]} \n\n\n*Info Coronavirus Russia 🇷🇺*\n\n*Positive* : {jsr["cases"]} \n*Recovred* : {jsr["recovered"]} \n*Died* : {jsr["deaths"]} \n*Today cases* : {jsr["todayCases"]} \n*Today died* : {jsr["todayDeaths"]} \n*critical* : {jsr["critical"]} \n*casesPerOneMillion* : {jsr["casesPerOneMillion"]} \n*deathsPerOneMillion* : {jsr["deathsPerOneMillion"]} \n*totalTests* : {jsr["totalTests"]} \n*TestsPerMillion*: {jsr["testsPerOneMillion"]} \n\n\n*Global* \n\n*Positive* : {jss["cases"]} \n*Recovered* : {jss["recovered"]} \n*Died* : {jss["deaths"]}'
        msg.body(text)
        responded = True
    
    if 'Menu' in incoming_msg or 'menu' in incoming_msg:
        text = f'⌨️ *List Of Command :*  \n\n🔥 *info-covid* (Information of COVID-19) \n\n🔥 *Schedule* _Display Schedule_\n\n🔥 */YT* _<url>_ : Youtube Downloader\n\n🔥 */Quote* : Generate Quote\n\n🔥 */wiki* : Information form wikipedia\n\n🔥 */FL* _<url>_ : Download Big Size Fb Videos\n\n🔥 */GL* _<query>_ : Google Search\n\n🔥 */weather* : weather Information \n\n🔥 */TTS* <Text> : Text To Speech\n\n🔥 *help* : How to use the command'
        msg.body(text)
        responded = True
    
    if '/GL' in incoming_msg:
        from googlesearch import search
        query = incoming_msg[3:]
        for i in search(query, tld="com", num=10, stop=10, pause=2):
            text = f'\n\n============Results============\n\n *Result* : '+i
            msg.body(text)
            responded = True

    if '/quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True

    if '/weather' in incoming_msg or '/Weather' in incoming_msg:
        api_key = "8ef61edcf1c576d65d836254e11ea420"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        city_name= ("Ahmedabad")    
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
        text = f'Current weather in Ahmedabad city\n\n================================\nTemperature in kelvin unit :' +str(current_temperature)
        text2 = f'\n\nHumidity percentage :' +str(current_humidiy)
        text3 = f'\n\n\n\n*Weather description* :' +str(weather_description)
        msg.body(text)
        msg.body(text2)
        msg.body(text3)
        responded = True

    if '/location' in incoming_msg:
        def index():
            url = 'http://freegeoip.net/json'
            r = requests.get(url)
            j = json.loads(r.text)
            city = j['city']
            text = f'Your City is :' + city
            msg.body(text)
            responded = True
        # from flask_simple_geoip import SimpleGeoIP
        #app.config.update(GEOIPIFY_API_KEY='')
        #simple_geoip = SimpleGeoIP(app)
        #geoip_data = simple_geoip.get_geoip_data()
        #jsonify=jsonify(data=geoip_data)
        #text = f'Current location :' + jsonify
       
        
    if '/wiki' in incoming_msg:
        query = incoming_msg[10:]
        incoming_msg = incoming_msg.replace("wiki", "")
       	result = wikipedia.summary(incoming_msg, sentences=3)
        text = f'\n\n This is according to wikipedia\n\n=============*Result*==============\n\n: '+result
        msg.body(text)
        responded = True

    if 'Time' in incoming_msg or 'time' in incoming_msg:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        text = f'\n\n Current time is\n: '+ strTime
        msg.body(text)
        responded = True
            
    if '/FL' in incoming_msg:
        import requests as r
        import re
        par = incoming_msg[3:]
        html = r.get(par)
        video_url = re.search('sd_src:"(.+?)"', html.text).group(1)
        reqq = r.get('http://tinyurl.com/api-create.php?url='+video_url)
        msg.body('*Video works on Convert...*\n\nLINK : '+reqq.text)
        responded = True
        
    if '/TTS' in incoming_msg:
        par = incoming_msg[5:]
        msg.media('https://api.farzain.com/tts.php?id='+par+'&apikey=JsaChFteVJakyjBa0M5syf64z&')
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
        
    if 'Schedule' in incoming_msg:
       msg.media('https://user-images.githubusercontent.com/74760068/102241016-82258d80-3f1e-11eb-8c71-6e0176c2739c.png')
       responded = True

    if 'help' in incoming_msg or 'Help' in incoming_msg:
       text = f'💻 *Help For Facebook*\n\n/FB _link video_ Ecample :\n\n/FB https://fb.watch/2uY9On1xkw/ \n\n💻 *Help For Google Search* \n\n /GL <Query> Example :  \n\n/GL CHARUSAT \n\n/TTS WhatsappBotKrabby\n\nIf you want to use space, replace it with% 20\n\nExample : /TTS Whatsapp%20Bot%Krabby'
       msg.body(text)
       responded = True
    
    if responded == False:
        msg.body('Sorry, I Am just bot didn\'t recognized that command :), please send start to go to the menu')

    return str(resp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
