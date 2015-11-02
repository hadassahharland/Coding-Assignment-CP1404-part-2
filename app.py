__author__ = 'Dassa'

# from currency.py import convert
from trip import Details
from kivy.app import App
from kivy.lang import Builder


home_country = "Australia"
todays_date = "2002/09/08"
details = Details()
details.add("Japan", "2002/09/07", "2002/09/09")

class BoxLayoutDemo(App):
    def build(self):
        self.title = "GUI"
        self.root = Builder.load_file('gui.kv')
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
        # On update_button_press if change return "'from''($)' to 'to''($)'"
        # If trip details changed return "Trip Details Accepted"

    def current_trip_location(self):
        label = "Current trip Location: \n" + details.current_country(todays_date)
        return label
        # Centralize this label


BoxLayoutDemo().run()