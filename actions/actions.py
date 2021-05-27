# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


import requests
import random
from typing import Any, Text, Dict, List
import time
from datetime import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



#GOOD TO GO : Get Country By IP
#Test : 196.70.128.96 (MA) / 2.4.6.8(FR) / 5.6.7.8(GE)
class ActionGetCountyByIp(Action):

    def name(self) -> Text:
        return "action_search_country"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        ip = tracker.latest_message['text'].split()[-1]
        
        api_country = 'https://api.ip2country.info/ip?' + ip
        
        n = random.randint(0, 2)
        l = ["This country ", "Look what I found! It ", "The country you ask "]
        
        try:
            json_data = requests.get(api_country).json()
            if json_data['countryCode'] == "":
                raise ValueError("Sorry, I didn't find the country with this ip :" + ip)
            
            message = l[n] + "is {0}\nThe country code is {1}\nThe flag is {2}".format(
                    json_data['countryName'], json_data['countryCode'], json_data['countryEmoji'])

            print("Country and Ip Action OK")
            dispatcher.utter_message(text=message)

        except ValueError:
            dispatcher.utter_message(
                text="Sorry, I didn't find the country with this ip :" + ip)

        except KeyError:
            dispatcher.utter_message(
                text="Sorry, I didn't find the country with this ip :" + ip)
       
        return []


#GOOD TO GO : Bitcoin
class ActionBitcoin(Action):

    def name(self) -> Text:
        return "action_search_bitcoin"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        n = random.randint(0, 2)
        l = ["That's quit expensive! ", "Look what I found! ", "Can you imagine the price? "]

        try:
              
            api_bitcoin = 'https://api.coindesk.com/v1/bpi/currentprice/eur.json'
            # print("api_bitcoin=", api_bitcoin)

            json_data = requests.get(api_bitcoin).json()

            message = l[n]+"On {1}. The price is ${0} or €{2} per 1 Bitcoin\n".format(
                        json_data['bpi']['USD']['rate_float'],
                        json_data['time']['updated'],
                        json_data['bpi']['EUR']['rate_float'])

            print("Bitcoin Action OK")
            dispatcher.utter_message(text=message)

            return []

        except KeyError:
            dispatcher.utter_message(text="Sorry, I didn't find the price you ask for")


#GOOD TO GO : Weather
class ActionWeather(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #tracker : catch all the conversation / message
        name = tracker.latest_message['text'].split()[-1] #get last word
        if name == '?':
            name = tracker.latest_message['text'].split()[-2]
        
        try:    
            api_weather = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=' + name
            # print("api_weather=", api_weather)

            json_data = requests.get(api_weather).json()
            format_add = json_data['main']

            #calculer temprature in celcius -273
            message = "Weather is {0} - {5}\nTemprature is min {2}/ max {1} degree celsius\nHumidity is {3}%\nPressure is {4} hpa\nSunrise : {6}(CET)\nSunset : {7}(CET)".format(json_data['weather'][0]['main'],
                                int(format_add['temp_max']-273), 
                                int(format_add['temp_min']-273), 
                                int(format_add['humidity']), 
                                int(format_add['pressure']), 
                                json_data['weather'][0]['description'],
                                datetime.fromtimestamp(json_data['sys']['sunrise']),
                                datetime.fromtimestamp(json_data['sys']['sunset']),
                                )
            
            print("Weather Action OK")
            dispatcher.utter_message(text=message)

            return []

        except KeyError:
            # name = tracker.latest_message['text'].split()[-1]
            dispatcher.utter_message(text="Cannot find the city " + name)
            # print ("Cannot find the city")


#GOOD TO GO : GET TIME
#san%20francisco
class ActionShowTime(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        n = random.randint(0, 2)
        ts = time.time()
        l = ["Let me check. ", "I am happy to tell you. ",
             "It's quite far. "]

        try:
            userAsk = tracker.latest_message['text'].split()
            getLocation = tracker.latest_message['text'].split()[-1]
            api_time = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=' + getLocation

            json_data = requests.get(api_time).json()
            timezone = json_data['timezone']

            if "time" in userAsk:
                # print("user ask : ", userAsk, " timezone= ", timezone)

                #convert to local time
                gettime = l[n] + "The Time is {0}".format(
                    datetime.fromtimestamp(ts + timezone - 7200)
                )

                dispatcher.utter_message(text=gettime)
                print("Show Time Action OK")

        except KeyError:
            dispatcher.utter_message(
                text="Sorry I didn't understand your question")

        return []

#GOOD TO GO : GET UNIVERSITY
#descartes/ harvard / yale/ diderot / abc ...etc
class ActionUniversity(Action):

    def name(self) -> Text:
        return "action_search_university"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            university = tracker.latest_message['text'].split()[-1]
            if university == '?':
                university = tracker.latest_message['text'].split()[-2]
            

            n = random.randint(0, 2)
            l = ["Let me check, it ", "The university which you search for ", "Look likes a wonderful university, it "]
            
            api_universities = 'http://universities.hipolabs.com/search?name=' + university
            # print("api_universities= ", api_universities)

            
            json_data = requests.get(api_universities).json()
            # print("json_data= ", json_data)

            if json_data != []:       
                format_add = json_data[0]
                #calculer temprature in celcius -273
                message = l[n] + "is in {0}. The full name is {1}\nCheck on the site : {2}".format(format_add['country'], format_add['name'], format_add['web_pages'])
                
                print("University Action OK")
                dispatcher.utter_message(text=message)
            else:
                print("University Action Not Ok")
                dispatcher.utter_message(
                    text="Sorry I didn't find any info of this university " + university)
                
            return []

        except KeyError:
            dispatcher.utter_message(
                text="Sorry I didn't find any info of this university" + university)
                  
                 
                  
#GOOD TO GO : GET JOKE
class ActionJoke(Action):

    def name(self) -> Text:
        return "action_tell_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        n = random.randint(0, 2)
        l = ["Check this one lol\n\n", "I hope this one will make you laugh :D\n\n",
                     "LOL, I love this one!\n\n"]

        try:
            i = 10
            while(i > 0):
                i = i-1
                api_joke = 'https://v2.jokeapi.dev/joke/Any'
                # print("api_joke= ", api_joke)

                json_data = requests.get(api_joke).json()
                # print("json_data= ", json_data)

                if json_data != "":
                    if json_data['category'] == "Programming":
                        format_add = json_data['setup'] + "\n" + json_data['delivery']

                        message = l[n] + "{0}".format(format_add)

                        dispatcher.utter_message(text=message)
                        print("Joke Action OK")
                        break

                else: 
                    dispatcher.utter_message(text="Sorry, I ran out all my jokes ;(")
            # print("Joke Action Not Ok")

            return []

        except KeyError:
            dispatcher.utter_message(text="Sorry, I ran out all my jokes ;(")
