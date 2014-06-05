# -*- coding: utf-8 -*-
# Copyright (c) 2011-2014 Polyconseil SAS. All rights reserved.f

from pyramid.config import Configurator

from dokang.utils import load_doc_sets


def make_app(global_settings, **settings):
    """Set up and return the WSGI application."""
    settings = load_doc_sets(settings)
    config = Configurator(settings=settings)

    # Third-party includes
    config.include('pyramid_chameleon')

    # Routes and views for static and home page
    config.add_static_view('static', 'static')
    config.add_route('search', '/')
    config.add_view('.views.search', route_name='search',
                    renderer='templates/search.pt')

    return config.make_wsgi_app()
