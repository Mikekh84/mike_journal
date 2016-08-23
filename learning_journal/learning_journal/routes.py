def includeme(config):
    """Include Me config thingy."""
    config.add_route('home', '/')
    config.add_route('detail', '/detail/')
    config.add_route('edit', '/edit/' )
    config.add_static_view('static', 'static', cache_max_age=3600)