from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Student, Class
from .forms import NewClassForm

def siema_json(request: HttpRequest):
    if "user" in request.GET:
        return JsonResponse({"user": request.GET["user"]})
    else:
        return JsonResponse({"empty": "empty"})

class Lesson:
    def __init__(self, name, lecturer):
        self.name = name
        self.lecturer = lecturer

def adding(request):
    context = {}
    
    if request.method == 'POST':
        context.update({'form':NewClassForm(request.POST)})
        if form.is_valid():
            rooster = Class("4C")
            rooster.save()
            print(rooster)
            #context.update({'rooster':rooster})
    else:
        form = NewClassForm()
        context.update({'form':NewClassForm()})

    return render(request, 'adding.html', context)

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

    students = Student.objects.all()
    students = Student.objects.filter(number__gte = 2, number__lt = 10)
    classes = Class.objects.filter(name = "3C")
  
  #gte - greater than equal
  #lte - less than equal
  #gt - greater than
  #lt - less than

    context = {
        'welcome_message': greeting,
        'lessons': betterLessons,
        'students': students,
        'classes': classes
    }

    return render(request, 'index.html', context)


