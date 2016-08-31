from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from sqlalchemy.exc import DBAPIError
from ..models import Entry


@view_config(route_name="home", renderer="../templates/index.jinja2")
def list_view(request):
    """View home and list of journals."""
    entries = request.dbsession.query(Entry).order_by(Entry.id.desc())
    return {"entries": entries}


@view_config(route_name="edit", renderer="../templates/edit.jinja2")
def edit_view(request):
    """View the edit view."""
    get_id = request.matchdict['id']
    entry = request.dbsession.query(Entry).filter(Entry.id == get_id).first()  # order by date.
    return {"entry": entry}
    # Handle an error


@view_config(route_name="create", renderer="../templates/create.jinja2")
def create_view(request):
    """View the create view."""
    if request.method == 'POST':
        new_title = request.params.get('title')
        new_body = request.params.get('body')
        new = Entry(title=new_title, body=new_body, date='8/16/204')
        request.dbsession.add(new)
        request.dbsession.flush()
        return HTTPFound(location=request.route_url('home'))
    return {}


@view_config(route_name="detail", renderer="../templates/journal.jinja2")
def detail_view(request):
    """View the detail view."""
    try:
        get_id = request.matchdict['id']
        entry = request.dbsession.query(Entry).filter(Entry.id == get_id).first()
        return {"entry": entry}
    except DBAPIError:
        return HTTPNotFound


# if request.method == POST
    # title = request.params.get('title', '')
    # httpFound modeule
    # return HTTFound(location=request.route_ur('home'))
    # db.flush
