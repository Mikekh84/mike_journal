from pyramid.response import Response
import os

HERE = os.path.dirname(__file__)


def my_view(request):
    """View first view."""
    imported_text = open(os.path.join(HERE, 'mock.html')).read()
    return Response(imported_text)


def includeme(config):
    """Include me for views."""
    config.add_view(my_view, route_name='home')
