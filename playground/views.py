from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse

def siema_json(request: HttpRequest):
    if "user" in request.GET:
        return JsonResponse({"user": request.GET["user"]})
    else:
        return JsonResponse({"empty": "empty"})

class Lesson:
    def __init__(self, name, lecturer):
        self.name = name
        self.lecturer = lecturer

def zsl(request):
    lessons = [{"name": "polish",
                "lecturer": "Sienkiewicz"},
               {"name": "maths",
                "lecturer": "Niewulis"},
               {"name": "english",
                "lecturer": "Wengrzyn"}]

    betterLessons = [Lesson("polish", "Sienkiewicz"),
                     Lesson("maths", "Niewulis"),
                     Lesson("english", "Wengrzyn")]

    greeting = "Witam"
    if 'welcome' in request.GET:
        greeting = request.GET['welcome']

    context = {
        'welcome_message': greeting,
        'lessons': betterLessons,
    }

    return render(request, 'index.html', context)


