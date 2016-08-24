def includeme(config):
    """Include Me config thingy."""
    config.add_route('home', '/')
    config.add_route('create', '/journal/new-entry/')
    config.add_route('update', r'/journal/{id:\d+}/edit-entry/')
    config.add_route('detail', r'/journal/{id:\d+}/')
    config.add_static_view('static', 'static', cache_max_age=3600)
