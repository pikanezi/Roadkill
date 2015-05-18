import logging
from google.appengine.ext import ndb

__author__ = 'Vincent'

light_map = ['broad daylight', 'twilight or dawn', 'night without street lights', 'night with unlit street lights',
             'night with lit street lights']


class AccidentModel(ndb.Model):
    numac = ndb.StringProperty()
    organization = ndb.StringProperty()
    light = ndb.StringProperty()
    agglomeration = ndb.StringProperty()
    intersection = ndb.StringProperty()
    atmosphere = ndb.StringProperty()
    crash_type = ndb.StringProperty()
    address = ndb.StringProperty()
    department = ndb.StringProperty()
    town = ndb.StringProperty()
    gps = ndb.StringProperty()
    latitude = ndb.FloatProperty()
    longitude = ndb.FloatProperty()
    road_type = ndb.StringProperty()
    road_number = ndb.StringProperty()
    v1 = ndb.StringProperty()
    v2 = ndb.StringProperty()
    pr = ndb.IntegerProperty()
    pr1 = ndb.IntegerProperty
    infrastructure = ndb.StringProperty()
    situation = ndb.StringProperty()
    circulation = ndb.StringProperty()
    nbv = ndb.StringProperty()
    vosp = ndb.StringProperty()
    prof = ndb.StringProperty()
    plan = ndb.StringProperty()
    killed = ndb.IntegerProperty()
    seriously_injured = ndb.IntegerProperty()
    slightly_injured = ndb.IntegerProperty()
    unscathed = ndb.IntegerProperty()
    numero_type = ndb.StringProperty()
    numero = ndb.StringProperty()
    distance_metre = ndb.IntegerProperty()
    libelle_voie = ndb.StringProperty()
    code_rivoli = ndb.StringProperty()
    grav = ndb.StringProperty()

    @staticmethod
    def accident_from_csv(csv_row):
        latitude = csv_row[32]
        longitude = csv_row[33]
        if latitude == '' or longitude == '':
            return None
        logging.info(latitude + " " + longitude)
        logging.info(csv_row)
        logging.info(len(csv_row))
        latitude = float(latitude[1:] + '.' + latitude[:1])
        longitude = float(longitude[1:] + '.' + longitude[:1])
        return AccidentModel(
            organization=csv_row[0],
            light=light_map[int(csv_row[1])-1],
            killed=csv_row[21],
            seriously_injured=csv_row[22],
            slightly_injured=csv_row[23],
            unscathed=csv_row[24],
            latitude=latitude,
            longitude=longitude,
        )