from django.shortcuts import render
from django.utils import timezone
from datetime import datetime


def landing_page(request):
    """Render the public digital wedding invitation landing page."""
    context = {
        "couple": {
            "partner_one": "Alexius",
            "partner_two": "Divya",
            "partner_one_full": "Alexius Varghese Bennette",
            "partner_two_full": "Divya Rose Davis",
            "monogram": "A & D",
            "tagline": "We are getting married",
            "hero_phrase": "Two lives, two hearts, joined together in friendship, united forever in love.",
            "invitation_text": "Request the honor of your presence as we celebrate our love and exchange vows.",
        },
        "event": {
            "date": "Saturday, January 02, 2027",
            "iso_date": "2027-01-02T10:00:00",
            "time": "10:00 AM",
            "venue_name": "St. Francis Xavier Forane Church",
            "venue_address": "Karukutty, Angamaly",
            "calendar_title": "Alexius & Divya's Wedding",
            "calendar_description": "Join Alexius and Divya in celebrating their engagement and wedding ceremonies.",
        },
        "story": [
            {
                "year": "2019",
                "title": "Meeting for the first time",
                "description": "We met for the first time, and then we got to know each other.",
                "badge": "First Meet",
                "multi_year": False,
            },
            {
                "year1": "2020",
                "year2": "2024",
                "title": "Exploring Together",
                "description": "Travelling, going on dates, and falling more in love with each other.",
                "badge": "Dating",
                "multi_year": True,
            },
            {
                "year1": "2025",
                "year2": "2026",
                "title": "Introducing each other to our families",
                "description": "Finally telling our parents and meeting the families.",
                "badge": "Introducing Family",
                "multi_year": True,
            },
            {
                "year": "2027",
                "title": "Engagement and Wedding",
                "description": "We will be getting engaged and married.",
                "badge": "Together Forever",
                "multi_year": False,
            },
        ],
        "schedule": [
            {
                "date": "Saturday, January 02, 2027",
                "time": "10:00 AM",
                "title": "Engagement Service",
                "subtitle": "St. Francis Xavier Forane Church, Karukutty",
                "description": "Exchange of engagement rings and blessings in the presence of close family and friends.",
                "icon": "ring",
            },
            {
                "date": "Saturday, January 02, 2027",
                "time": "11:00 AM",
                "title": "Engagement Lunch",
                "subtitle": "La Mirage Convention Center, Koratty",
                "description": "A delightful afternoon banquet, refreshments, and family felicitations.",
                "icon": "dining",
            },
            {
                "date": "Sunday, January 24, 2027",
                "time": "3:30 PM",
                "title": "The Holy Matrimony Ceremony",
                "subtitle": "St. Mary's Cathedral",
                "description": "The sacred nuptial vows and exchange of marital rings.",
                "icon": "heart",
            },
            {
                "date": "Sunday, January 24, 2027",
                "time": "6:30 PM",
                "title": "Wedding Reception",
                "subtitle": "The Grand Starlight Pavilion",
                "description": "Cocktails, a lavish four-course dinner banquet, cake cutting, live music, and dancing.",
                "icon": "sparkles",
            },
        ],
        "events_venues": [
            {
                "badge": "The Engagement Ceremony & Lunch",
                "title": "Engagement Day",
                "date": "Saturday, January 02, 2027",
                "church": {
                    "role": "Engagement Service",
                    "name": "St. Francis Xavier Forane Church",
                    "time": "10:00 AM",
                    "address": "Karukutty Mookkannoor Rd, Karukutty 683576",
                    "google_maps_url": "https://maps.app.goo.gl/SsB7xeb33xr4xajb8",
                },
                "hall": {
                    "role": "Engagement Luncheon",
                    "name": "La Mirage Convention Center",
                    "time": "11:00 AM",
                    "address": "Koratty Bazar Rd, Manjalykettu, Koratty 680308",
                    "google_maps_url": "https://maps.app.goo.gl/Lwu3WfKjvQiStEgb9",
                },
            },
            {
                "badge": "The Holy Matrimony & Reception",
                "title": "Wedding Day",
                "date": "Saturday, October 24, 2026",
                "church": {
                    "role": "Holy Matrimony Service",
                    "name": "St. Mary's Cathedral",
                    "time": "3:30 PM",
                    "address": "480 Cathedral Crest Road, Napa Valley, CA 94558",
                    "google_maps_url": "https://maps.google.com/?q=St+Marys+Cathedral+Napa+Valley+CA",
                },
                "hall": {
                    "role": "Grand Dinner Reception",
                    "name": "The Grand Starlight Pavilion",
                    "time": "6:30 PM",
                    "address": "520 Estate Boulevard, Napa Valley, CA 94558",
                    "google_maps_url": "https://maps.google.com/?q=Grand+Pavilion+Napa+Valley+CA",
                },
            },
        ],
    }
    return render(request, "landing/index.html", context)
