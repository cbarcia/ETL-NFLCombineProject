from flask import Flask, render_template, jsonify

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func, MetaData
from sqlalchemy.pool import StaticPool



engine= create_engine('mysql://root:deceptic0n@localhost:3306/combine_db', encoding='utf-8')


base = automap_base()

base.prepare(engine, reflect=True)

combine = base.classes.cleancombine

session = Session(engine)


#Flask Setup
app = Flask(__name__)

#Set Route
@app.route('/')
def welcome():
    """NFL COMBINE DATA `99-2015"""
    return render_template("NFL.html")

@app.route("/api/v1.0/fullname")
def names():
    "Return a list of all player names"
    results = session.query(combine.fullname).all()

    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/info")
def info():   
position = session.query(combine.position).all()
positions = list(np.ravel(position))
height = session.query(combine.height).all()
heights= list(np.ravel(height))
weight = session.query(combine.weight).all()
weights= list(np.ravel(weight))
fortyyd= session.query(combine.fortyyd).all()
fortyyds= list(np.ravel(fortyyd))
vertical= session.query(combine.vertical).all()
verticals=list(np.ravel(vertical))
college= session.query(combine.college).all()
colleges=list(np.ravel(college))
nflgrade= session.query(combine.nflgrade).all()
nflgrades=list(np.ravel(nflgrade))
pick= session.query(combine.pick).all()
picks=list(np.ravel(pick))   
        info_dict = {}
        info_dict["position"] = positions
        info_dict["Height"] = heights
        info_dict["weight"] = weights
        info_dict["fortyyd"] = fortyyds
        info_dict["vertical"] = verticals
        info_dict["college"] = colleges
        info_dict["nflgrade"] = nflgrades
        info_dict["pick"] = picks
        

        return jsonify(info_dict)

if __name__ == '__main__':
    app.run(debug=False)
