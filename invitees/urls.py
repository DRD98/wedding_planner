from django.urls import path
from . import views

urlpatterns = [
    path("", views.invitees_list, name="invitees_list"),
    path("add/", views.invitee_create, name="invitee_create"),
    path("<int:pk>/edit/", views.invitee_update, name="invitee_update"),
    path("<int:pk>/delete/", views.invitee_delete, name="invitee_delete"),
    path("budget/", views.budget_view, name="budget_view"),
]
