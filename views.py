from flask import render_template, redirect, url_for

from app import app, db, freezer
from models import Restaurant

@app.route('/')
def index():
	restaurants = Restaurant.query.all()
	return render_template('index.html', title='index', restaurants=restaurants)

@app.route('/<slug>/')
def restaurant_view(slug):
	restaurant = Restaurant.query.filter_by(slug=slug)[0]
	restaurants = Restaurant.query.filter(Restaurant.slug != slug)

	return render_template(
		'restaurant.html',
		title='restaurant',
		restaurant=restaurant,
		restaurants=restaurants
	)

@freezer.register_generator
def restaurant_view():	
	for restaurant in Restaurant.query.all():
		yield { 'slug': restaurant.slug }
