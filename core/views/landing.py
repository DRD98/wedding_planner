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
            "iso_date": "2027-01-02T11:00:00",
            "time": "11:00 AM",
            "venue_name": "St. Xavier's Forane Church",
            "venue_address": "Karukoutty, Angamaly",
            "calendar_title": "Alexius & Divya's Wedding",
            "calendar_description": "Join Alexius and Divya in celebrating their engagement and wedding ceremonies.",
        },
        "story": [
            {
                "year": "2019",
                "title": "A Chance Encounter in Paris",
                "description": "A shared table at a quaint bookstore cafe near the Seine turned a 10-minute coffee into a four-hour conversation about art, travel, and dreams.",
                "badge": "The Spark",
            },
            {
                "year": "2021",
                "title": "The First Grand Adventure",
                "description": "Road-tripping along the Amalfi Coast, navigating steep cliffside roads, discovering hidden coves, and realizing we made the greatest travel team.",
                "badge": "The Journey",
            },
            {
                "year": "2024",
                "title": "Sunset Under the Olive Grove",
                "description": "Against a backdrop of golden hour in Tuscany, Liam dropped to one knee. Through tears of joy, Sophia said the easiest 'Yes' of her life.",
                "badge": "The Proposal",
            },
        ],
        "schedule": [
            {
                "time": "10:30 AM",
                "title": "Engagement & Betrothal Service",
                "subtitle": "St. Jude's Chapel",
                "description": "Exchange of engagement rings and blessings in the presence of close family and friends.",
                "icon": "ring",
            },
            {
                "time": "1:00 PM",
                "title": "Celebratory Engagement Lunch",
                "subtitle": "The Rosewood Banquet Hall",
                "description": "A delightful afternoon banquet, refreshments, and family felicitations.",
                "icon": "dining",
            },
            {
                "time": "3:30 PM",
                "title": "The Holy Matrimony Ceremony",
                "subtitle": "St. Mary's Cathedral",
                "description": "The sacred nuptial vows and exchange of marital rings.",
                "icon": "heart",
            },
            {
                "time": "6:30 PM",
                "title": "Grand Wedding Reception & Dinner",
                "subtitle": "The Grand Starlight Pavilion",
                "description": "Cocktails, a lavish four-course dinner banquet, cake cutting, live music, and dancing.",
                "icon": "sparkles",
            },
        ],
        "events_venues": [
            {
                "badge": "The Engagement Ceremony & Lunch",
                "title": "Engagement Day",
                "date": "Friday, October 23, 2026",
                "church": {
                    "role": "Engagement Service",
                    "name": "St. Jude's Chapel",
                    "time": "10:30 AM",
                    "address": "120 Chapel Way, St. Helena, CA 94574",
                    "google_maps_url": "https://maps.google.com/?q=St+Jude+Chapel+St+Helena+CA",
                },
                "hall": {
                    "role": "Engagement Luncheon",
                    "name": "The Rosewood Banquet Hall",
                    "time": "1:00 PM",
                    "address": "250 Vineyard Lane, St. Helena, CA 94574",
                    "google_maps_url": "https://maps.google.com/?q=Rosewood+Hall+St+Helena+CA",
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
        "dress_code": {
            "title": "Formal Elegance / Traditional Grandeur",
            "description": "We cordially invite our guests to celebrate with us in rich shades of champagne, maroon, burgundy, and classic formal attire.",
            "colors": [
                {"name": "Royal Maroon", "hex": "#681A24"},
                {"name": "Deep Burgundy", "hex": "#4A0E17"},
                {"name": "Warm Champagne", "hex": "#F7E7CE"},
                {"name": "Champagne Gold", "hex": "#C5A059"},
                {"name": "Pearl Ivory", "hex": "#FAF6F0"},
            ],
        },
        "notes": [
            {
                "title": "Unplugged Ceremony",
                "content": "We kindly ask you to turn off all phones and cameras during the church ceremony so you can be fully present with us in prayer and celebration. Our professional photographers will capture every precious moment.",
            },
            {
                "title": "Wishing Well & Blessings",
                "content": "Your presence, love, and blessings are the greatest gifts of all. If you wish to honor us with a gift, a contribution towards our new beginning together will be warmly cherished.",
            },
        ],
    }
    return render(request, "landing/index.html", context)
