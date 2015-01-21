#!/usr/bin/env python

from icalendar import Calendar, Event
from datetime import datetime, timedelta
import requests

country_calendars_map = {
    "US": "en.usa",
    "GB": "en.uk",
    "JP": "en.japanese",
    "CN": "en.china",
    "LT": "en.lithuanian",
    "VT": "en.vietnamese"
}

for country, calendar_id in country_calendars_map.items():
    url = "https://www.google.com/calendar/ical/" + calendar_id + "%23holiday%40group.v.calendar.google.com/public/basic.ics?start-min=2013-06-30T00%3A00%3A00%2B08%3A00&start-max=2014-12-27T00%3A00%3A00%2B08%3A00&max-results=26160"
    r = requests.get(url)
    cal = Calendar.from_ical(r.content)

    for event in cal.walk('vevent'):
        start = event.get('dtstart').dt
        end = event.get('dtend').dt
        diff = end - start
        summary = event.get('summary').encode("utf8")

        for i in xrange(diff.days):
            print country + "\t" + str(start + timedelta(days=i)) + "\t" + summary
