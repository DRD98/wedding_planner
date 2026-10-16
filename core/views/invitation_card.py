from django.shortcuts import render


def invitation_card_view(request):
    """Render the digital wedding invitation card."""
    context = {
        "parents": {
            "title": "Mr. Davis Mavely & Mrs. Daisy Davis",
            "house": "Mavely House",
            "address": "Karukutty, Ernakulam District",
        },
        "invitation_lines": {
            "cordial": "CORDIALLY INVITE YOU",
            "grace": "to grace the auspicious occasion of the",
            "ceremony": "Betrothal Ceremony of our Daughter",
        },
        "bride": {
            "name": "Divya Rose Davis",
        },
        "groom": {
            "name": "Alexius Varghese Bennette",
            "relation": "(S/o. Mr. Joseph Bennette C V &",
            "mother": "Mrs. Victoria Carol M J",
            "house": "Cocheril House",
            "location": "Palarivattom, Ernakulam District)",
        },
        "event": {
            "year": "2027",
            "month": "January",
            "day": "2",
            "day_name": "Saturday",
            "time": "10:00 AM",
            "church_name": "St. Francis Xavier's Forane Church",
            "church_place": "Karukutty",
            "church_maps_url": "https://maps.google.com/?q=St+Marys+Forane+Church+Puthenchira",
            "reception_title": "Reception at",
            "reception_hall": "La Mirage,",
            "reception_place": "Koratty",
            "reception_maps_url": "https://maps.google.com/?q=Jubilee+Hall+Puthenchira",
        },
        "marriage": {
            "line1": "Marriage will be solemnized at",
            "line2": "St. Francis Xavier's Roman Catholic Church, Kaloor, Ernakulam",
            "line3": "on Sunday 24th January 2027 at 4.00 pm",
        },
        "sharing": {
            "heading": "Sharing the Happiness:",
            "names": "Diya Mary Davis",
        },
    }
    return render(request, "invitation/card.html", context)
