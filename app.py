from currency import get_details
from currency import convert
from trip import Details
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from currency import get_all_details
from trip import Error
import time
__author__ = 'Dassa'


class CurrencyConverter(App):

    """ class variables """
    current_state = StringProperty()
    home_state = StringProperty()
    country_names = ListProperty()
    status_text = StringProperty()
    update_button_disabled = StringProperty()

    def __init__(self, **kwargs):
        super(CurrencyConverter, self).__init__(**kwargs)
        # Retrieve today's date using time builtin in format YYYY/MM/DD
        self.todays_date = time.strftime("%Y/%m/%d")
        # Retrieve current time using time builtin
        self.time = time.strftime('%H:%M:%S')
        self.forward_conversion_rate = -1
        self.backward_conversion_rate = -1
        self.details = Details()
        self.country_list = []
        self.home_country = ""
        self.load_config()
        self.update_button_disabled = ""
        try:
            self.current_country = self.details.current_country(self.todays_date)
            self.home_currency = get_details(self.home_country)[1]  # to retrieve code
            self.target_currency = get_details(self.current_country)[1]
        except Error:
            self.current_country = "Could not be found"
            self.target_country = self.current_country
            self.update_button_disabled = "True"

    def build(self):
        self.title = "GUI"
        self.root = Builder.load_file('gui.kv')
        Window.size = (350, 700)
        # Set current state to current country (currently 1st country in list)
        self.current_state = ""
        # add values to the spinner
        self.root.ids.home_country_label.text = self.home_country
        return self.root

    """ load the config file and store the data """
    def load_config(self):
        try:
            config_data = open("config.txt", mode='r', encoding="utf-8")
            self.home_country = config_data.readline().strip("\n")
            # Retrieve locations from config.txt file format: location,start_date,end_date
            self.details.locations = []
            self.country_list = []
            for line in config_data.readlines():
                parts = line.strip().split(",")
                # add all details to locations
                self.details.locations.append(tuple(parts))
                # checks country exists
                for key in get_all_details():
                    if parts[0] == key:
                        # add only country names to country_list
                        self.country_list.append(parts[0])
                    else:
                        self.status_text = "Invalid trip details"
            config_data.close()
            self.status_text = "Config loaded\nsuccessfully"
        except FileNotFoundError:
            self.status_text = "Config could not\nbe loaded"

    # processing input from app separately
    """ takes location value and converts to value in home currency """
    def convert_forward(self):
        try:
            amount = float(self.root.ids.current_country_input.text)
            end_amount = float(float(self.forward_conversion_rate)*amount)
            self.root.ids.home_country_input.text = str("%.3f" % end_amount)
            self.status_text = "{} ({}) to {} ({})".format(self.target_currency, self.get_symbol(self.target_country), self.home_currency, self.get_symbol(self.home_country))
            return end_amount
        except ValueError:
            self.status_text = "Invalid Input"

    """ takes home value and converts to value in location  """
    def convert_backward(self):
        try:
            amount = float(self.root.ids.home_country_input.text)
            end_amount = float(float(self.backward_conversion_rate)*amount)
            self.root.ids.current_country_input.text = str("%.3f" % end_amount)
            self.status_text = "{} ({}) to {} ({})".format(self.home_currency, self.get_symbol(self.home_country), self.target_currency, self.get_symbol(self.target_country))
            return end_amount
        except ValueError:
            self.status_text = "Invalid Input"

    """ retrieves the symbol for the currency from the currency_details file using the get_all_details() function """
    def get_symbol(self, country):
        if country in get_all_details().keys():
            symbol = get_all_details()[country][0][2]
            return symbol
        else:
            return None

    """ takes a country name and returns it's currency code using get_all_details """
    def change_state(self, target_country):
        self.root.ids.current_country_input.readonly = False
        self.root.ids.home_country_input.readonly = False
        self.target_country = self.root.ids.country_spinner.text
        all_details = get_all_details()
        for country in all_details:
            if target_country == country:
                details = all_details[country]
                target_country_details = details[0]
                target_currency_new = target_country_details[1]
                # If the currency code has not changed, do not update
                if not target_currency_new == self.target_currency:
                    self.target_currency = target_currency_new
                    self.get_conversion_rate()
                return [self.target_currency, target_country_details[2]]

    """ retrieves the conversion rate from the internet """
    def get_conversion_rate(self):
        self.forward_conversion_rate = convert(1, self.home_currency, self.target_currency)
        self.backward_conversion_rate = convert(1, self.target_currency, self.home_currency)

    def update_button_press(self):
        # activates the text input fields
        self.root.ids.current_country_input.readonly = False
        self.root.ids.home_country_input.readonly = False
        # On press of the update button retrieve fresh data from webpage
        self.get_conversion_rate()
        self.status_text = "Updated at\n" + self.time
        if self.root.ids.country_spinner.text == "":
            self.root.ids.country_spinner.text = self.current_country

    def current_trip_location(self):
        return "Current trip Location: \n" + self.current_country

    def todays_date_label(self):
        label = "Today is:" + "\n" + self.todays_date
        # format today's date for the gui
        return label

CurrencyConverter().run()
