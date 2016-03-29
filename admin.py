import flask_admin as admin
from flask_admin.contrib.sqla import ModelView

from app import app, db
from models import Restaurant

# Admin
admin = admin.Admin(app)


class RestaurantView(ModelView):
	inline_models = ()

admin.add_view(RestaurantView(Restaurant, db.session))
