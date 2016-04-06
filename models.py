from datetime import datetime
from app import db



class Restaurant(db.Model):
    Name = db.Column(db.Text(), primary_key=True)
    GoogleAddress = db.Column(db.Text())
    SubRegion = db.Column(db.Text())
    Region = db.Column(db.Text())
    Website = db.Column(db.Text())
    slug = db.Column(db.Text())
    Cuisine = db.Column(db.Text())
    Phone = db.Column(db.Text())
    Noise = db.Column(db.Text())
    photo1 = db.Column(db.Text())
    photo2 = db.Column(db.Text())
    Specialties = db.Column(db.Text())
    Fullreviewlink = db.Column(db.Text())
    article = db.Column(db.Text())

    guides = db.relationship('Guide', backref=db.backref('restaurant', lazy='joined'), lazy='dynamic')
  
    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Restaurant: {}>'.format(self.Name)

class Guide(db.Model):
    Name = db.Column(db.Text(), db.ForeignKey('restaurant.Name'), primary_key=True)
    OneofaKind = db.Column(db.Text())
    GreatPizza = db.Column(db.Text())
    TopBurgers = db.Column(db.Text())
    OpenLate = db.Column(db.Text())
    ExceptionalBars = db.Column(db.Text())
    BestofBrunch = db.Column(db.Text())
    Outdoor = db.Column(db.Text())
    SaturdayLunch = db.Column(db.Text())
    Top100Classics = db.Column(db.Text())
    Historic = db.Column(db.Text())
    Views = db.Column(db.Text())
    New = db.Column(db.Text())
    PrivateRooms = db.Column(db.Text())
    TastingMenus = db.Column(db.Text())
    FourStars = db.Column(db.Text())
