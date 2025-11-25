from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("status/", views.status, name="status"),
    path("reviews/", views.reviews, name="reviews"),
    path("reviews/add/", views.add_review, name="add_review"),
    path("reviews/form/", views.review_form, name="review_form"),
]
