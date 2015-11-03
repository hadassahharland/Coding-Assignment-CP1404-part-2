__author__ = 'Dassa'

from currency import convert
from trip import Details
from kivy.app import App
from kivy.lang import Builder


home_country = "Australia"
todays_date = "2002/09/08"
# retrieve today's date
details = Details()
details.add("Japan", "2002/09/07", "2002/09/09")
# add to details inside app


class BoxLayoutDemo(App):
    def build(self):
        self.title = "GUI"
        self.root = Builder.load_file('gui.kv')
        # setting the size of window to 350 x 700
        self. =
        # self.root = Builder.__sizeof__()
        self.root.ids.home_country_label.text = home_country
        return self.root

    def update_button_press(self):
        pass
        # On press of the update button retrieve fresh data from webpage

    def status_label(self):
        return "status label"
        # If invalid country name return "Invalid Country: 'country_name'"
        # If invalid trip dates return "Invalid Dates: 'dates'"
        # On update_button_press if no change return "Refreshed 'time'"
        # On update_button_press if change return "'from id''($)' to 'to id''($)'"
        # If the config file loaded successfully return "Trip Details Accepted"
        # If the config file could not be loaded return "Trip Details not found"
        # If the config file loaded but contains invalid trip details return "Invalid Trip Details"



    def current_trip_location(self):
        if False: # location chosen on spinner
            current_country = "spinner input" # location from spinner
        else: # no location chosen on spinner
            current_country = details.current_country(todays_date)
        return "Current trip Location: \n" + current_country
        #
        # Centralize this label

    def todays_date(self):
        # retrieve today's date
        return "Today is: \n" + todays_date
        # Centralize this label

BoxLayoutDemo().run()

# Currency retrieval processing
# debugging
# home_country = "Japan"
# home_currency = get_details(home_country)[1]
# print(home_currency)          returns: JPY

# home_currency = currency.get_details(home_country)[1] # to retrieve code
# finding target_country
# if spinner == None or spinner == current_trip_location:
#   target_country = current_trip_location
# else:
#   target_country = spinner
# target_currency = currency.get_details(target_country)[1]

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