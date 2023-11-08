
import googlemaps
from django.shortcuts import render
from .models import Restaurant
from django.http import JsonResponse
from io import BytesIO
from PIL import Image
import requests
from django.core.files import File
from datetime import datetime
from django.conf import settings



gmaps = googlemaps.Client(key=settings.API_KEY)


# To download the photo from photo url
def download_and_save_image(photo_url, restaurant_name):
    try:
        response = requests.get(photo_url)
        if response.status_code == 200:
            image_content = response.content
            image = Image.open(BytesIO(image_content))
            image_io = BytesIO()

            # Save the image with the restaurant name
            image_name = f"{restaurant_name}.jpg"
            image.save(image_io, format='JPEG')
            return File(image_io, name=image_name)
    except Exception as e:
        print("Error downloading and saving image:", e)
    return None



def index(request):
    radius = 40000  # Default radius
    if request.method == 'POST':
        radius = int(request.POST.get('radius', 40000))  # Get the radius from the form

    # Perform a nearby search using Google Maps API
    places_result = gmaps.places_nearby(location='23.7699272,90.3858256', radius=radius, open_now=False, type='restaurant')
    
    restaurants = []
    for place in places_result['results']:
        name = place.get('name', 'N/A')
        rating = place.get('rating', 'N/A')
        address = place.get('vicinity', 'N/A')
        latitude = place['geometry']['location']['lat']
        longitude = place['geometry']['location']['lng']

        # Retrieve the photo
        photo_url = ''
        if 'photos' in place:
            photo_reference = place['photos'][0]['photo_reference']
            photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={settings.API_KEY}"

        # Download and save the photo to the database 
        photo = download_and_save_image(photo_url, name)


        # Retrieve the opening hours 
        opening_hours = []
        if 'opening_hours' in place and 'weekday_text' in place['opening_hours']:
            opening_hours = place['opening_hours']['weekday_text']


        

        # Create a restaurant object with fields
        restaurant = Restaurant(name=name, address=address, rating=rating, latitude=latitude, longitude=longitude, opening_hour=opening_hours, photo=photo)
        restaurants.append(restaurant)

    # Save restaurants to the database 
    Restaurant.objects.bulk_create(restaurants)

    # Fetch the data from the database
    rest_db = Restaurant.objects.all()

    
    return render(request, 'index.html', {'restaurants': rest_db, 'radius': radius})



