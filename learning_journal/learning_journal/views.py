from pyramid.response import Response
import os

HERE = os.path.dirname(__file__)


def list_view(request):
    """Home page/index of learning journal."""
    index = open(os.path.join(HERE, 'index.html')).read()
    return Response(index)


def create_view(request):
    """View for create."""
    created = open(os.path.join(HERE, 'create.html')).read()
    return Response(created)


def update_view(request):
    """Edit view."""
    edit = open(os.path.join(HERE, 'editone.html')).read()
    return Response(edit)


def detail_view(request):
    """Journal Entry view."""
    journal = open(os.path.join(HERE, 'journalentryone.html')).read()
    return Response(journal)


def includeme(config):
    """Include me for views."""
    config.add_view(list_view, route_name='home')
    config.add_view(create_view, route_name='create')
    config.add_view(update_view, route_name='update')
    config.add_view(detail_view, route_name='detail')
