from django.shortcuts import render
from .models import Image
from random import randint
import time

prev = [Image.objects.get(id=1).image, Image.objects.get(id=2).image]
bigger_value = ""
counter = 0
finish_time = 0


def mainpage(request):
    global prev   # Global variables declaration
    global bigger_value
    global finish_time

    z = request.GET
    if "status" in z.keys():   # This is the case when previous answer was incorrect
        finish_time = time.time()
        return render(request, "mainpage.html", {"first": prev[0], "second": prev[1],
                                                 "bigger": bigger_value, "answer_incorrect": True})

    length = len(Image.objects.all())   # This is the case when previous answer was correct
    object1 = Image.objects.get(id=randint(1, length))
    object2 = Image.objects.get(id=randint(1, length))

    while object1.result == object2.result:   # This loop's goal is to avoid situation when there are
        object1 = Image.objects.get(id=randint(1, length))   # two images with the same result
        object2 = Image.objects.get(id=randint(1, length))

    bigger_value = "left" if object1.result > object2.result else "right"

    prev = [object1.image, object2.image]   # This variable saves last images every time for correct processing
                                            # of the situation when we need to display last images in first case
    if time.time() - finish_time < 5:
        finish_time = time.time()
        return render(request, "mainpage.html", {"first": object1.image, "second": object2.image,
                                                 "bigger": bigger_value, "goahead": True})
    finish_time = time.time()
    return render(request, "mainpage.html", {"first": object1.image, "second": object2.image, "bigger": bigger_value})
