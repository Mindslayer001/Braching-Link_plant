from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profile, Link


class LinkListView(ListView):
    model = Link


class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy("link_list")


class LinkUpdateView(UpdateView):
    model = Link
    fields = ["text", "url"]
    success_url = reverse_lazy("link_list")


class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy("link_list")


def profile_view(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    links = profile.links.all()
    context = {
        "profile": profile,
        "links": links,
    }

    return render(request, "link_plant/profile_detail.html", context)