from django.urls import path
from .views import LinkListView, LinkCreateView, LinkUpdateView, LinkDeleteView, profile_view
urlpatterns = [
    path("", LinkListView.as_view(), name = 'link_list'),
    path("link/create/", LinkCreateView.as_view(), name = 'create_list'),
    path("link/<int:pk>/update/", LinkUpdateView.as_view(), name = 'update_list'),
    path("link/<int:pk>/delete/", LinkDeleteView.as_view(), name = 'delete_list'),
    path('profile/<slug:slug>/', profile_view, name = 'profile_list'),
]