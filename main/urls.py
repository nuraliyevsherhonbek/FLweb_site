from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    HomeView,
    CourseListView,
    ContactView,
    ApplicationView,
    EventDetailView,
    EventsView,
    ResultListView

)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('courses/', CourseListView.as_view(), name='courses_list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('application/', ApplicationView.as_view(), name='application'),
    path('events/', EventsView.as_view(), name='events'),
    path('events/<int:pk>', EventDetailView.as_view(), name='events_detail'),
    path('results', ResultListView.as_view(), name='results'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)