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
 
    
    results = session.query(combine).all()

    all_info = []
    for all_info in results:
        info_dict = {}
        info_dict["position"] = combine.position
        info_dict["Height"] = combine.Height
        info_dict["weight"] = combine.weight
        info_dict["fortyyd"] = combine.fortyyd
        info_dict["vertical"] = combine.vertical
        info_dict["college"] = combine.college
        info_dict["nflgrade"] = combine.nflgrade
        info_dict["pick"] = combine.pick
        all_info.append(info_dict)

        return jsonify(all_info)

if __name__ == '__main__':
    app.run(debug=False)
