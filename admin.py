import flask_admin as admin
from flask_admin.contrib.sqla import ModelView

from app import app, db
from models import Restaurant, Guide

# Admin
admin = admin.Admin(app)


class RestaurantView(ModelView):
	inline_models = (Guide,)

admin.add_view(RestaurantView(Restaurant, db.session))
admin.add_view(ModelView(Guide, db.session))

