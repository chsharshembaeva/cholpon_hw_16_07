from . import views
from . import app


app.add_url_rule('/', view_func=views.index, methods=['GET'], endpoint='index')
