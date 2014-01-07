from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_GET, require_POST

from rhetoric import view_config


def phony_decorator(view):
    """ Decorator for testing Rhetoric's decorator predicate.
    """
    def decorated(request, *args, **kwargs):
        return view(request, *args, **kwargs)
    return decorated


@view_config(route_name='index.dashboard', request_method='GET', renderer='index.html')
def dashboard(request):
    return {'method': 'GET'}


# request method restrictions using django decorators (for testing Rhetoric's "decorator" option)

@view_config(route_name='index.dashboard', request_method='POST', renderer='index.html',
             # only POST method will be handled, since the request_method param
             # is explicitly set
             decorator=require_http_methods(["GET", "POST"]))
def post_on_dashboard(request):
    return {'method': 'POST'}


@view_config(route_name='index.dashboard', request_method='PUT', renderer='index.html',
             # test multiple decorators combined
             decorator=(phony_decorator, phony_decorator))
def put_on_dashboard(request):
    return {'method': 'PUT'}


# Versioned views
# --------------------------------
@view_config(route_name='index.versions', request_method='GET', api_version='1.0', renderer='json')
def get_version_1(request):
    return {
        'version': '1.0'
    }

@view_config(route_name='index.versions', request_method='GET', api_version='>1.0, <2.0', renderer='json')
def get_version_1_range(request):
    return {
        'method': 'GET',
        'version': '>1.0, <2.0'
    }

@view_config(route_name='index.versions', request_method='POST', api_version='>1.0, <2.0', renderer='json')
def post_version_1_range(request):
    return {
        'method': 'POST',
        'version': '>1.0, <2.0'
    }

@view_config(route_name='index.versions', request_method='POST', api_version='>=2.0', renderer='json')
def post_version_2_range(request):
    return {
        'version': '>=2.0'
    }