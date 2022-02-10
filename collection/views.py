from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from typing import List
from django.db.models import Count
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.views.generic.base import View

from .models import ItemCollection
from .models import Item
from user.models import CustomUser


def get_five_newest_items() -> List[Item]:
    five_newest_items = Item.objects.order_by('-created')[:6]
    return five_newest_items


def get_five_biggest_collections() -> List[ItemCollection]:
    five_biggest_collections = ItemCollection.objects.annotate(items_count=Count('item')).filter(items_count__gt=0).order_by('-items_count')[:6]
    return five_biggest_collections


def get_home_page_data(request: HttpRequest) -> HttpResponse:
    newest_items = get_five_newest_items()
    biggest_collections = get_five_biggest_collections()
    return render(
        request,
        "main/home.html",
        {
            "biggest_collections": biggest_collections,
            "newest_items": newest_items,
            "title": _("Home page"),
        }
    )


def get_personal_page_data(
        request: HttpRequest,
        username: str
) -> HttpResponse:
    owner_object = CustomUser.objects.get(username=username)
    owner_id = owner_object.id
    owner_username = owner_object.username
    collections = owner_object.itemcollection_set.all()
    return render(
        request,
        "collection/personal_page.html",
        {
            "owner_id": owner_id,
            "owner_username": owner_username,
            "collections": collections,
            "title": _("Personal page"),
        }
    )





