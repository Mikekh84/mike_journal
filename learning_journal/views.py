from pyramid.view import view_config


@view_config(route_name="home", renderer="templates/index.jinja2")
def list_view(request):
    """View home and list of journals."""
    return {}


@view_config(route_name="edit", renderer="templates/edit.jinja2")
def edit_view(request):
    """View the edit view."""
    return {}


@view_config(route_name="create", renderer="templates/create.jinja2")
def create_view(request):
    """View the create view."""
    return {}


@view_config(route_name="detail", renderer="templates/journal.jinja2")
def detail_view(request):
    """View the detail view."""
    return {}
