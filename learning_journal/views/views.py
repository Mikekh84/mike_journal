from pyramid.view import view_config
from pyramid.security import remember, forget
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from sqlalchemy.exc import DBAPIError
from ..models import Entry
from ..security import check_cred


@view_config(route_name="home", renderer="../templates/index.jinja2")
def list_view(request):
    """View home and list of journals."""
    entries = request.dbsession.query(Entry).order_by(Entry.id.desc()) # order by date
    return {"entries": entries}


@view_config(route_name="edit", renderer="../templates/edit.jinja2")
def edit_view(request):
    """View the edit view."""
    get_id = request.matchdict['id']
    entry = request.dbsession.query(Entry).filter(Entry.id == get_id).first()
    if request.method == "POST":
        entry.title = request.params.get('title')
        entry.body = request.params.get('body')
        request.dbsession.add(entry)
        request.dbsession.flush()
        return HTTPFound(location=request.route_url('home'))
    return {"entry": entry}
    # Handle an error


@view_config(route_name="create", renderer="../templates/create.jinja2", permission="secured")
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


@view_config(route_name="login", renderer='../templates/login.jinja2')
def login(request):
    """The login view."""
    if request.method == 'POST':
        username = request.params.get('username', '')
        password = request.params.get('password', '')
        if check_cred(username, password):
            return HTTPFound(
                location=request.route_url('home'),
                headers=remember(request, username))
        else:
            return {'error': "Username or password is not correct."}
    return {'error': "An error happened."}
