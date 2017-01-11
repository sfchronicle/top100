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

@app.route('/guide/2017-contenders/')
def contenders():
	restaurants = [
  {
    "restaurant": "Original Joe's Westlake",
    "link": "http://www.sfchronicle.com/restaurants/diningout/article/Original-Joe-s-Westlake-brings-back-the-past-7296147.php",
    "img": "9847007"
  },
  {
    "restaurant": "Leo's Oyster Bar",
    "link": "http://www.sfchronicle.com/restaurants/diningout/article/Michael-Bauer-Leo-s-Oyster-Bar-s-refined-7397699.php",
    "img": "9937518"
  },
  {
    "restaurant": "Aster",
    "link": "http://www.sfchronicle.com/restaurants/article/Aster-now-a-shining-star-in-the-Mission-7945247.php",
    "img": "12168935"
  },
  {
    "restaurant": "Rintaro",
    "link": "http://www.sfchronicle.com/restaurants/article/Rintaro-evolves-into-loving-expression-of-7955450.php",
    "img": "10168331"
  },
  {
    "restaurant": "Picco in Larkspur",
    "link": "http://www.sfchronicle.com/restaurants/article/Alluring-Picco-doesn-t-miss-a-beat-with-new-chef-8319082.php",
    "img": "12168943"
  },
  {
    "restaurant": "Ju-ni",
    "link": "http://www.sfchronicle.com/restaurants/diningout/article/Ju-ni-is-a-sushi-star-for-a-new-generation-8323351.php",
    "img": "10410073"
  },
  {
    "restaurant": "Miminishi in Napa",
    "link": "http://www.sfchronicle.com/restaurants/diningout/article/Inspired-by-visit-to-Japan-chef-s-Miminashi-8348094.php",
    "img": "10479970"
  },
  {
    "restaurant": "Bellota",
    "link": "http://www.sfchronicle.com/food/article/Bellota-is-the-Absinthe-Group-s-biggest-and-8403303.php",
    "img": "10558365"
  },
  {
    "restaurant": "Cockscomb",
    "link": "http://www.sfchronicle.com/restaurants/article/Chris-Cosentino-s-Cockscomb-boldly-earns-three-7266082.php",
    "img": "9835968"
  },
  {
    "restaurant": "In Situ",
    "link": "http://www.sfchronicle.com/restaurants/diningout/article/Corey-Lee-s-culinary-artistry-at-In-Situ-the-9173165.php",
    "img": "10752105"
  },
  {
    "restaurant": "Bluestem",
    "link": "http://www.sfchronicle.com/restaurants/article/S-F-s-Bluestem-Brasserie-soars-to-three-stars-9208030.php",
    "img": "12169053"
  },
  {
    "restaurant": "Corridor",
    "link": "http://www.sfchronicle.com/restaurants/diningout/article/Mid-Market-s-new-Corridor-reinvents-and-rewards-9213223.php",
    "img": "10865492"
  },
  {
    "restaurant": "Playa in Mill Valley",
    "link": "http://www.sfchronicle.com/restaurants/diningout/article/Vamos-a-la-Playa-Inspired-Mexican-cuisine-in-9517222.php",
    "img": "10935201"
  },
  {
    "restaurant": "Seven Hills",
    "link": "http://www.sfchronicle.com/restaurants/article/Neighborhood-restaurant-Seven-Hills-is-seeing-9967035.php",
    "img": "11378379"
  },
  {
    "restaurant": "Nightbird",
    "link": "http://www.sfchronicle.com/restaurants/diningout/article/Nightbird-flies-high-in-Hayes-Valley-10035557.php",
    "img": "11487838"
  },
  {
    "restaurant": "Saratoga",
    "link": "http://www.sfchronicle.com/restaurants/diningout/article/The-Saratoga-Cuisine-designed-for-cocktails-in-10840351.php",
    "img": "12123354"
  }
]
	return render_template('2017_contenders.html', restaurants=restaurants)

@freezer.register_generator
def restaurant_view():
	for restaurant in Restaurant.query.all():
		yield { 'slug': restaurant.slug }

