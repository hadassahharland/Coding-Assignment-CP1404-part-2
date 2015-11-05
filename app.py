__author__ = 'Dassa'

from currency import get_details
from currency import convert
from currency import get_all_details
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
home_country = config_data.readline().strip("\n")

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
    home_currency = get_details(home_country)[1]  # to retrieve code
    target_currency = None


    def build(self):
        self.title = "GUI"
        self.root = Builder.load_file('gui.kv')
        Window.size = (350, 700)
        # Set current state to current country (currently 1st country in list)
        self.current_state = ""
        # add values to the spinner
        self.country_names = country_list
        self.root.ids.home_country_label.text = home_country
        return self.root

    # processing input from app separately
    # takes location value and converts to value in home currency
    def convert_forward(self):
        amount = self.root.ids.current_country_input.text
        end_amount = str(convert(amount, CurrencyConverter.home_currency, CurrencyConverter.target_currency))
        self.root.ids.home_country_input.text = end_amount
        return end_amount

    # takes home value and converts to value in location currency
    def convert_backward(self):
        amount = self.root.ids.home_country_input.text
        end_amount = str(convert(amount, CurrencyConverter.target_currency, CurrencyConverter.home_currency))
        self.root.ids.current_country_input.text = end_amount
        return end_amount


# takes a country name and returns it's currency code using get_all_details
    def change_state(self, target_country):
        self.root.ids.current_country_input.readonly = False
        self.root.ids.home_country_input.readonly = False
        all_details = get_all_details()
        for country in all_details:
            if target_country == country:
                details = all_details[country]
                target_country_details = details[0]
                CurrencyConverter.target_currency = target_country_details[1]
        # self.root.ids.current_country_input.
        # self.root.ids.test_label.text = text
        return CurrencyConverter.target_currency

    def update_button_press(self):
        self.root.ids.country_spinner.readonly = False
        end_amount = convert(amount, home_currency, target_currency)
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
        return "Current trip Location: \n" + CurrencyConverter.current_country

    @staticmethod
    def todays_date():
        label = "  Today is:" + "\n" + todays_date
        # format today's date for the gui
        return label

CurrencyConverter().run()


# Currency retrieval processing
# debugging
# home_country = "Japan"
# home_currency = g. et_details(home_country)[1]
# print(home_currency)          returns: JPY

# home_currency = get_details(home_country)[1]  # to retrieve code
# # If the spinner is what it was before, don't change it
# if get_details(CurrencyConverter.current_state)[1] == CurrencyConverter.current_country_target_currency:
#     target_currency = CurrencyConverter.current_country_target_currency
# else:
#     target_currency = get_details(CurrencyConverter.current_state)[1]
# debugging
# print(target_currency)

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


#