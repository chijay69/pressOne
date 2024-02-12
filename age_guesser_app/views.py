from datetime import datetime

import requests
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Person
from .serializer import PersonSerializer


@api_view(['POST'])
@csrf_exempt
@cache_page(86400)  # Cache for 24 hours (86400 seconds)
def get_human_age(request):
    if request.method == 'POST':
        name = request.data.get('name', '').lower()

        person = get_person_from_cache(name)
        if person:
            return Response(serialize_person_data(person))

        age = fetch_age_from_agify_api(name)
        if age is not None:
            person = create_person_in_cache(name, age)
            return Response(serialize_person_data(person))
        else:
            return Response({"error": "Age not found in response from Agify API"}, status=500)
    else:
        return Response({"error": "Only POST method allowed"}, status=405)


def get_person_from_cache(name):
    person = Person.objects.filter(name=name).first()
    return person


def serialize_person_data(person):
    serializer = PersonSerializer(person)
    data = serializer.data
    age = data['age']
    current_year = datetime.now().year
    data['date_of_birth'] = current_year - age
    return data


def fetch_age_from_agify_api(name):
    response = requests.get(f"https://api.agify.io/?name={name}")
    if response.status_code == 200:
        data = response.json()
        age = data.get("age")
        return age
    else:
        return None


def create_person_in_cache(name, age):
    person = Person.objects.create(name=name, age=age)
    return person
