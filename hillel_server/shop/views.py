import json

from django.http import HttpResponse, JsonResponse
from shop.models import Dog, Cat

# Create your views here.


def hello_page(request):

    return HttpResponse("Hello world!")


def dog(request):

    if request.method == "POST":  # add a new dog

        data = json.loads(request.body)

        our_dog = Dog(
            name=data["name"],
            breed=data["breed"],
            weight=data["weight"]
        )
        our_dog.save()

    elif request.method == "GET":  # get all dogs
        dogs_json = []
        dogs = Dog.objects.all()

        for d in dogs:
            dogs_json.append(
                {
                    "name": d.name,
                    "breed": d.breed,
                    "weight": d.weight
                }
            )

        return JsonResponse(
            dogs_json,
            safe=False
        )

    elif request.method == 'DELETE':  # delete all dogs
        dogs = Dog.objects.all()
        dogs.delete()

    return HttpResponse("DOG")


def cat(request):

    if request.method == "POST":  # add a new cat

        data = json.loads(request.body)

        our_cat = Cat(
            name=data["name"],
            breed=data["breed"],
            weight=data["weight"]
        )
        our_cat.save()

    elif request.method == "GET":  # get all cats
        cats_json = []
        cats = Cat.objects.all()

        for c in cats:
            cats_json.append(
                {
                    "name": c.name,
                    "breed": c.breed,
                    "weight": c.weight
                }
            )

        return JsonResponse(
            cats_json,
            safe=False
        )

    elif request.method == 'DELETE':  # delete cat
        cats = Cat.objects.all()
        cats.delete()

    return HttpResponse("CAT")

