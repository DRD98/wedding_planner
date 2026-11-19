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
            "monogram": "D & A",
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
                "image": "images/first-meet.png",
                "title": "Meeting for the First Time",
                "description": "Every love story has a beginning. Ours started when we met in May 2019 and began discovering a little more about each other.",
                "badge": "The Beginning",
                "multi_year": False,
                "last_event": False,
            },
            {
                "year1": "2020",
                "year2": "2024",
                "image": "images/travel.png",
                "title": "Exploring Together",
                "description": "From little adventures to unforgettable memories, we spent these years learning about each other and growing closer.",
                "badge": "Growing Together",
                "multi_year": True,
                "last_event": False,
            },
            {
                "year1": "2025",
                "year2": "2026",
                "image": "images/fam.png",
                "title": "Introducing Each Other to Our Families",
                "description": "Our story grew beyond the two of us as we introduced our families and took another meaningful step towards our future.",
                "badge": "Two Families, One Story",
                "multi_year": True,
                "last_event": False,
            },
            {
                "year1": "2027",
                "year2": "∞",
                "image": "images/forever.png",
                "title": "Our Forever Begins",
                "description": "With our families' blessings and hearts full of love, we begin our next chapter together.",
                "badge": "Forever Begins",
                "multi_year": True,
                "last_event": True,
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
                "date": "Sunday, January 24, 2027",
                "church": {
                    "role": "Holy Matrimony Service",
                    "name": "St. Francis Xavier's Roman Catholic Church",
                    "time": "4:00 PM",
                    "address": "Kathrikadavu, Kaloor 682017",
                    "google_maps_url": "https://maps.app.goo.gl/YrTGNepFspPGxyuq5",
                },
                "hall": {
                    "role": "Grand Dinner Reception",
                    "name": "Anugraha Auditorium",
                    "time": "6:30 PM",
                    "address": "Kathrikadavu, Kaloor 682017",
                    "google_maps_url": "https://maps.app.goo.gl/TRv9LWzNUtxfmx8z8",
                },
            },
        ],
    }
    return render(request, "landing/index.html", context)
