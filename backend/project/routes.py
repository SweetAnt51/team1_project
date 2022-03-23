from flask import Blueprint, render_template, jsonify, request
import json

# from classes import genPolyPoints
from .classes import genPolyPoints
from .classes import FullPolygon

bp = Blueprint('team1', __name__)


@bp.route("/")
def index():
    """ the main end point the web application will access by default """


    ''' The bleow is only for testing/demo and will be deleted in production
        Just putting some points here so you can see the output in the console
    '''

    polygon = [(31.56643791473137, -95.6473440685322), (27.72186717708344, -92.80031634629975), (27.57023677231448, -92.67043602981329), (27.23877938199186, -92.38406187179204), (25.86514957107443, -88.1039285649021), (23.6863378831994, -79.62231426940097), (23.63589848251528, -79.3099406086436), (23.47228787115569, -77.13354914237215), (23.82272947850308, -73.59959296893587), (24.69173551578442, -71.83414991609621), (24.77423842464465, -71.70321989153989), (24.84070906204188, -71.62396945091942), (26.30709227206436, -70.49537021150113), (27.24374150116319, -70.32739675197554), (29.486121709704, -70.07529629912764), (30.79434301411118, -70.18903457666468), (33.91573275175608, -71.21585763488865), (37.38635059758756, -73.72654732394005), (37.59455235957057, -73.99481647414193), (38.1918253302461, -76.56346692450587), (38.86559398344152, -80.81035975201156), (39.06767446742989, -83.10720553980757), (39.08444134611751, -83.54946847706033), (37.07426597092839, -93.15824568761943), (35.2855229814549, -96.94778120393802), (35.13183128609756, -97.2105868431351), (34.9630500678956, -97.37456749446653)]
    inputs = genPolyPoints.generateRandomPointsInPoly(polygon, 10000) #generates a random set of points inside a polygon.  Only used for testing

    ''' END SETUP BLOCK'''

    outerPoly = FullPolygon.Polygon(inputs)
    convexHull = outerPoly.convexHull()
    
    print(outerPoly.number_of_points)  #length of original polygon
    print(len(convexHull)) #length of convex hull
    print(convexHull) #points making up the convex hull

    return render_template("index.html")