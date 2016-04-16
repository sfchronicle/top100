from flask import render_template, redirect, url_for

from app import app, db, freezer
from models import Restaurant, Guide

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

@app.route('/guide/one-of-a-kind/')
def oneofakind_view():
	restaurants = Restaurant.query.all()
	guides = Guide.query.all()
	return render_template('guide_oneofakind.html', title='index', restaurants=restaurants, guides=guides)

@app.route('/guide/fourstars/')
def fourstars_view():
	restaurants = Restaurant.query.all()
	guides = Guide.query.all()
	return render_template('guide_fourstars.html', title='index', restaurants=restaurants, guides=guides)

@app.route('/guide/best-of-brunch/')
def brunch_view():
	restaurants = Restaurant.query.all()
	guides = Guide.query.all()
	return render_template('guide_brunch.html', title='index', restaurants=restaurants, guides=guides)

@app.route('/guide/classics/')
def classics_view():
	restaurants = Restaurant.query.all()
	guides = Guide.query.all()
	return render_template('guide_classic.html', title='index', restaurants=restaurants, guides=guides)

@app.route('/guide/exceptional-bars/')
def bars_view():
	restaurants = Restaurant.query.all()
	guides = Guide.query.all()
	return render_template('guide_bars.html', title='index', restaurants=restaurants, guides=guides)

@app.route('/guide/great-pizza/')
def pizza_view():
	restaurants = Restaurant.query.all()
	guides = Guide.query.all()
	return render_template('guide_greatpizza.html', title='index', restaurants=restaurants, guides=guides)

@app.route('/guide/historic/')
def historic_view():
	restaurants = Restaurant.query.all()
	guides = Guide.query.all()
	return render_template('guide_historic.html', title='index', restaurants=restaurants, guides=guides)


@app.route('/guide/new/')
def new_view():
	restaurants = Restaurant.query.all()
	guides = Guide.query.all()
	return render_template('guide_new.html', title='index', restaurants=restaurants, guides=guides)


@app.route('/guide/open-late/')
def late_view():
	restaurants = Restaurant.query.all()
	guides = Guide.query.all()
	return render_template('guide_openlate.html', title='index', restaurants=restaurants, guides=guides)

@app.route('/guide/outdoor/')
def outdoor_view():
	restaurants = Restaurant.query.all()
	guides = Guide.query.all()
	return render_template('guide_outdoor.html', title='index', restaurants=restaurants, guides=guides)

@app.route('/guide/private-rooms/')
def private_view():
	restaurants = Restaurant.query.all()
	guides = Guide.query.all()
	return render_template('guide_privaterooms.html', title='index', restaurants=restaurants, guides=guides)

@app.route('/guide/top-burgers/')
def burger_view():
	restaurants = Restaurant.query.all()
	guides = Guide.query.all()
	return render_template('guide_topburgers.html', title='index', restaurants=restaurants, guides=guides)

@app.route('/guide/saturday-lunch/')
def saturdaylunch_view():
	restaurants = Restaurant.query.all()
	guides = Guide.query.all()
	return render_template('guide_saturdaylunch.html', title='index', restaurants=restaurants, guides=guides)


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

