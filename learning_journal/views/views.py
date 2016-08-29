from pyramid.view import view_config
from pyramid.response import Response
from .journal import JOURNAL_ENTRIES as JOURNAL_ENTRIES
from pyramid.exceptions import HTTPNotFound
from sqlalchemy.exc import DBAPIError
from ..models import MyModel


@view_config(route_name="home", renderer="../templates/index.jinja2")
def list_view(request):
    """View home and list of journals."""
    return {"entries": JOURNAL_ENTRIES}


@view_config(route_name="edit", renderer="../templates/edit.jinja2")
def edit_view(request):
    """View the edit view."""
    for entry in JOURNAL_ENTRIES:
        if entry['id'] == request.matchdict["id"]:
            return {"entry": entry}
    return HTTPNotFound


@view_config(route_name="create", renderer="../templates/create.jinja2")
def create_view(request):
    """View the create view."""
    return {}


@view_config(route_name="detail", renderer="../templates/journal.jinja2")
def detail_view(request):
    """View the detail view."""
    for entry in JOURNAL_ENTRIES:
        if entry['id'] == request.matchdict["id"]:
            return {"entry": entry}
    return HTTPNotFound
