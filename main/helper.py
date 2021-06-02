from .models import Result, Application, Course
from random import choice


def get_results_3():
    my_list = []
    results = Result.objects.all()
    if len(results) > 3:
        while len(my_list) < 4:
            my_list.append(choice(results))

        return my_list
    else:
        return results


def get_popular_courses():
    courses = Course.objects.all(),
    if len(Application.objects.all()) > 100:
        popular_courses = sorted(courses, key=lambda a: len(a.applications), reverse=True)[:3]

        return popular_courses
    return courses[:3]
