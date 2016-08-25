from pyramid.response import Response
import os

HERE = os.path.dirname(__file__)


def list_view(request):
    """View the lists."""
    imported_list = open(os.path.join(HERE, 'index.html')).read()
    return Response(imported_list)


def edit_view(request):
    """View the edit view."""
    edit = open(os.path.join(HERE, 'editone.html')).read()
    return Response(edit)


def create_view(request):
    """View the create view."""
    create = open(os.path.join(HERE, 'create.html')).read()
    return Response(create)


def detail_view(request):
    """View the detail view."""
    detail = open(os.path.join(HERE, 'journalentryone.html')).read()
    return Response(detail)


def includeme(config):
    """Include Me!."""
    config.add_view(list_view, route_name="home")
    config.add_view(edit_view, route_name='edit')
    config.add_view(create_view, route_name='create')
    config.add_view(detail_view, route_name='detail')
