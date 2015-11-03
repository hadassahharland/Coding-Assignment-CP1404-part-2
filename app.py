__author__ = 'Dassa'

from currency import get_details
# from currency import convert
from trip import Details
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.properties import ListProperty
# from currency import get_all_details
import time

# Retrieve home_country from first line of config.txt assume no dates
config_data = open("config.txt", mode='r', encoding="utf-8")
home_country = config_data.readline()

# Retrieve locations from config.txt file format: location,start_date,end_date
details = Details()
details.locations = []
country_list = []
for line in config_data.readlines():
    parts = line.strip().split(",")
    # add all details to locations
    details.locations.append(tuple(parts))
    # add only country names to country_list
    country_list.append(parts[0])
config_data.close()
# debugging
# print(details.locations)
# print(country_list)

# Retrieve today's date using time builtin in format YYYY/MM/DD
todays_date = time.strftime("%Y/%m/%d")

# Relevant to spinner


class CurrencyConverter(App):

    # class variables
    current_state = StringProperty()
    home_state = StringProperty()
    country_names = ListProperty()
    current_country = details.current_country(todays_date)


    def __init__(self, **kwargs):
        super(CurrencyConverter, self).__init__(**kwargs)

    def build(self):
        self.title = "GUI"
        self.root = Builder.load_file('gui.kv')
        Window.size = (350, 700)
        # Set current state to current country (currently 1st country in list)
        self.current_state = self.current_country
        # add values to the spinner
        self.country_names = country_list
        self.root.ids.home_country_label.text = home_country
        return self.root

    def change_state(self, text):
        # self.root.ids.test_label.text = text
        return "change state"

    def update_button_press(self):
        pass
        # On press of the update button retrieve fresh data from webpage

    @staticmethod
    def status_label():
        return "status label"
        # If invalid country name return "Invalid Country: 'country_name'"
        # If invalid trip dates return "Invalid Dates: 'dates'"
        # On update_button_press if no change return "Refreshed 'time'"
        # On update_button_press if change return "'from id''($)' to 'to id''($)'"
        # If the config file loaded successfully return "Trip Details Accepted"
        # If the config file could not be loaded return "Trip Details not found"
        # If the config file loaded but contains invalid trip details return "Invalid Trip Details"

    @staticmethod
    def current_trip_location():
        # if False: # location chosen on spinner
        #     current_country = "spinner input" # location from spinner
        # else: # no location chosen on spinner
        return "Current trip Location: \n" + CurrencyConverter.current_country
        # Centralize this label

    @staticmethod
    def todays_date():
        label = "  Today is:" + "\n" + todays_date
        # retrieve today's date
        return label
        # Centralize this label

CurrencyConverter().run()

# Currency retrieval processing
# debugging
# home_country = "Japan"
home_currency = get_details(home_country)[1]
# print(home_currency)          returns: JPY

home_currency = get_details(home_country)[1] # to retrieve code
# finding target_country
spinner = "spinner"
if spinner == current_trip_location:
  target_country = current_trip_location
else:
  target_country = spinner
target_currency = get_details(target_country)[1]

# Input processing
# On update_button_press
# if True: # something is input to home_country_input
#     amount = BoxLayoutDemo.root.ids.home_country_input
# elif True: #something is input to current_country_input
#     amount = BoxLayoutDemo.root.ids.current_country_input
# else:
#     pass
    # do nothing
# end_amount = currency.convert(amount, home_currency, target_currency)
# currency not recognised


#