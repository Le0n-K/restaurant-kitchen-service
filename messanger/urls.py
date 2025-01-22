from django.urls import path

from . import views

app_name = "messanger"

urlpatterns = [
    path("", views.message_list, name="message_list"),
    path("delete/<int:message_id>/", views.delete_message, name="delete_message"),
]
