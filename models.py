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


  
    def __unicode__(self):
        return self.Name

    def __repr__(self):
        return '<Restaurant: {}>'.format(self.Name)
