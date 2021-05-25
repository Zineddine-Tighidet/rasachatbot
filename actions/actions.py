# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


import requests
import random
from typing import Any, Text, Dict, List
from datetime import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


#GOOD TO GO : Get Country By IP
#Test : 196.70.128.96 (MA) / 2.4.6.8(FR) / 5.6.7.8(GE) / 0.0.1.2(AU)
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
                raise ValueError(
                    "Sorry, I didn't find the country with this ip :" + ip)

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
        l = ["That's quit expensive! ", "Look what I found! ",
             "Can you imagine the price? "]

        try:

            api_bitcoin = 'https://api.coindesk.com/v1/bpi/currentprice/eur.json'
            print("api_bitcoin=", api_bitcoin)

            json_data = requests.get(api_bitcoin).json()

            message = l[n]+"On {1}. The price is ${0} or €{2} per 1 Bitcoin\n".format(
                json_data['bpi']['USD']['rate_float'],
                json_data['time']['updated'],
                json_data['bpi']['EUR']['rate_float'])

            print("Bitcoin Action OK")
            dispatcher.utter_message(text=message)

            return []

        except KeyError:
            dispatcher.utter_message(
                text="Sorry, I didn't find the price you ask for")

#GOOD TO GO : Weather


class ActionWeather(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #tracker : catch all the conversation / message
        name = tracker.latest_message['text'].split()[-1]  # get last word
        if name == '?':
            name = tracker.latest_message['text'].split()[-2]

        try:
            api_weather = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=' + name
            # print("api_weather=", api_weather)

            json_data = requests.get(api_weather).json()
            format_add = json_data['main']

            #calculer temprature in celcius -273
            message = "Weather is {0} - {5}\nTemprature is min {2}/ max {1} degree celsius\nHumidity is {3}%\nPressure is {4} hpa\nSunrise : {6}(CET)\nSunset : {7}(CET)".format(json_data['weather'][0]['main'],
                                                                                                                                                                                 int(
                                                                                                                                                                                     format_add['temp_max']-273),
                                                                                                                                                                                 int(
                                                                                                                                                                                     format_add['temp_min']-273),
                                                                                                                                                                                 int(
                                                                                                                                                                                     format_add['humidity']),
                                                                                                                                                                                 int(
                                                                                                                                                                                     format_add['pressure']),
                                                                                                                                                                                 json_data['weather'][
                                                                                                                                                                                     0]['description'],
                                                                                                                                                                                 datetime.fromtimestamp(
                                                                                                                                                                                     json_data['sys']['sunrise']),
                                                                                                                                                                                 datetime.fromtimestamp(
                                                                                                                                                                                     json_data['sys']['sunset'])
                                                                                                                                                                                 )

            print("Weather Action OK")
            dispatcher.utter_message(text=message)

            return []

        except KeyError:
            # name = tracker.latest_message['text'].split()[-1]
            dispatcher.utter_message(text="Cannot find the city " + name)
            # print ("Cannot find the city")

#THIS IS A TEST
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         print("Hello World Action OK")
#         dispatcher.utter_message(text="Hello World!")

#         return []
