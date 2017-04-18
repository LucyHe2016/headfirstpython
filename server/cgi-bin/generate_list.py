#!/usr/local/bin/python3

import athletemodel
import htmlutil

athletes = athletemodel.get_namesID_from_store()
print(htmlutil.start_response())
print(htmlutil.include_header("NUAC's List of Athletes"))
print(htmlutil.start_form("generate_timing_data.py"))
print(htmlutil.para("Select an athlete from the list to work with:"))
for each_athlete in athletes:
    print(htmlutil.radio_button_id("which_athlete", each_athlete[0], each_athlete[1]))
print(htmlutil.end_form("Select"))
print(htmlutil.include_footer({'Home':'/index.html'}))

