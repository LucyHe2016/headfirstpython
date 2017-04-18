#!/usr/local/bin/python3

import cgi
import athletemodel
import htmlutil

form_data = cgi.FieldStorage()
athlete_id = form_data['which_athlete'].value
athlete = athletemodel.get_athlete_from_id(athlete_id)

print(htmlutil.start_response())
print(htmlutil.include_header("NUAC's Timing Data"))
print(htmlutil.header("Athlete:" + athlete['Name'] + ", DOB:" + athlete['DOB'] + "."))
print(htmlutil.para("The top times for this athlete are:"))
print(htmlutil.u_list(athlete['top3']))
print(htmlutil.para("The entire set of timing data is: " + str(athlete['data']) + " (duplicates removed)."))
links = { 'Home':'/index.html', 'Select Another Athlete':'generate_list.py' }
print(htmlutil.include_footer(links))

