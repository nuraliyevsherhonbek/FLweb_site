from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, Http404
from telebot import TeleBot
from telebot.types import Update, Message
from django.conf import settings
from .forms import ApplicationForm
from .models import Application, Course, Event, Result, SocialNetwork, StudentNumber
from .helper import get_results_3, get_popular_courses


bot = TeleBot(settings.BOT_TOKEN)



class HomeView(View):
    def get(self, request):

        number_of_courses = len(Course.objects.all())
        number_of_events = len(Event.objects.all())
        number_of_results = len(Result.objects.all())
        a = StudentNumber.objects.all()[0]
        number_of_students = a.number
        p_course = get_popular_courses()
        print(p_course[0])

        return render(request, 'main/home.html', context={
            'number_of_students': number_of_students,
            'number_of_courses': number_of_courses,
            'number_of_events': number_of_events,
            'popular_courses': Course.objects.all()[:3],
            'number_of_results': number_of_results,

            'results': get_results_3(),
            'courses_': Course.objects.all()[:5],
            'networks': SocialNetwork.objects.all(),
        })


class CourseListView(View):
    def get(self, request):

        return render(request, 'main/courses.html', context={
            'courses': Course.objects.all(),
            'networks': SocialNetwork.objects.all(),
            'courses_': Course.objects.all()[:5]

        })


class ContactView(View):
    def get(self, request):
        return render(request, 'main/contact.html', context={
            'networks': SocialNetwork.objects.all(),
            'courses_': Course.objects.all()[:5]

        })






class ApplicationView(View):
    def get(self, request):
        return render(request, 'main/application.html', context={
            'networks': SocialNetwork.objects.all(),
            'courses_': Course.objects.all()[:5]

        })

    def post(self, request):
        form = ApplicationForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data.get('subject', None)
            try:
                course = Course.objects.get(name=subject)
                at = Application.objects.create(**form.cleaned_data, course=course)
                print(at)
            except Exception:
                pass

            return render(request, 'main/application.html', context={
                'message': "A'riza yuborildi,",
                'networks': SocialNetwork.objects.all(),
                'courses_': Course.objects.all()[:5]

            })
        print(form.errors)
        return render(request, 'main/application.html', context={
            'form': form,
            'networks': SocialNetwork.objects.all(),
            'courses_': Course.objects.all()[:5]

        })


class EventsView(View):
    def get(self, request):
        return render(request, 'main/events.html', context={
            'networks': SocialNetwork.objects.all(),
            'events': Event.objects.all(),
            'courses_': Course.objects.all()[:5]

        })



class EventDetailView(View):
    def get(self, request, pk):
        try:
            event = Event.objects.get(pk)
            print(event)
            print(pk)
            return render(request, 'main/event-details.html', context={
                'networks': SocialNetwork.objects.all(),
                'event': event,
                'courses_': Course.objects.all()[:5]

            })
        except Course.DoesNotExist:
            return Http404()


class ResultListView(View):
    def get(self, request):
        return render(request, 'main/results.html', context={
            'networks': SocialNetwork.objects.all(),
            'results': Result.objects.all(),
            'courses_': Course.objects.all()[:5]

        })



class WebHookView(View):
    def post(self, request):
        bot.process_new_updates([Update.de_json(request.body.decode("utf-8"))])
        return HttpResponse('ok')


@bot.message_handler(commands=['start'])
def hello(message: Message):
    print(message.chat.id)
    bot.send_message(message.chat.id, 'Assalom Alaykum, Xush kelibsiz!')

@bot.message_handler(func=lambda m: True)
def start(message: Message):
    bot.send_message()