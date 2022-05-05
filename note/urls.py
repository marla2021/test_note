from django.urls import path

from note import views

urlpatterns = [
    path("create/", views.NoteCreateView.as_view()),
    path("", views.NoteListView.as_view()),
    path("<int:pk>/", views.NoteView.as_view()),
    path('<int:pk>/upload_image/', views.AdImageView.as_view()),

]