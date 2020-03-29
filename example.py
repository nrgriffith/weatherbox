#!/usr/bin/env python

import pywapi
import pprint
pp = pprint.PrettyPrinter(indent=4)

results = pywapi.get_weather_from_noaa("KIOW")
pp.pprint(results)
