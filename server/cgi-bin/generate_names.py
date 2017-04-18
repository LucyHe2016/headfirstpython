#!/usr/local/bin/python3

import athletemodel
import htmlutil
import json

names = athletemodel.get_namesID_from_store()
print(htmlutil.start_response("application/json"))
print(json.dumps(sorted(names)))

