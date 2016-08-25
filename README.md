# mike_journal
A Learning Journal Developed in Pyramid for CF 401 Python

Routes
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('edit', '/journal/{id:\d+}/edit')
    config.add_route('create', '/new-entry/')
    config.add_route('detail', '/journal/{id:\d+}')



#Help
Got help from Derek with heroku deployment
