from flask import render_template, redirect, url_for

from app import app, db, freezer
from models import Restaurant, Guide

restaurants = Restaurant.query.all()
guides = Guide.query.all()
print(guides);

@app.route('/')
def index():
	restaurants = Restaurant.query.all()
	return render_template('index.html', title='index', restaurants=restaurants)

@app.route('/cuisines/')
def cuisines_view():
	restaurants = Restaurant.query.all()
	return render_template('cuisines.html', title='index', restaurants=restaurants)

@app.route('/regions/')
def regions_view():
	restaurants = Restaurant.query.all()
	return render_template('regions.html', title='index', restaurants=restaurants)

@app.route('/guides/')
def guides_view():
	restaurants = Restaurant.query.all()
	guides = Guide.query.all()
	return render_template('guides.html', title='index', restaurants=restaurants, guides=guides)

@app.route('/search/')
def search_view():
	restaurants = Restaurant.query.all()
	return render_template('search.html', title='index', restaurants=restaurants)

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
