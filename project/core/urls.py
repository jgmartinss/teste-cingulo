from django.urls import path

from project.core.views import (
    UserActivitiView,
    UsersActivitiesByDateView,
    UsersActivitiesByMonthView,
)


app_name = 'core'


urlpatterns = [
    path('user-activiti/<int:pk>', UserActivitiView.as_view()),
    path('users-activities-by-date/<str:date>', UsersActivitiesByDateView.as_view()),
    path(
        'users-activities-by-month/<str:year>/<str:month>',
        UsersActivitiesByMonthView.as_view(),
    ),
]
