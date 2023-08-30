from pyramid.view import view_config


@view_config(route_name='home', renderer='pyramidProject:templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'pyramidProject'}
