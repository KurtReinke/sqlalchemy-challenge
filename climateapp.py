#import flask and others
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#Engine
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
#assign Vars
me = Base.classes.measurements
st = Base.classes.station
#create the app
app1 = Flask(_name_)


#Flask Routes
@app.route("/")
def intro():
    return (
        f"Available API Routes:<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"<br/>"
        f"/api/v1.0/stations<br/>"
        f"<br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"/api/v1.0/<start>"
        f"<br/>"
        f"/api/v1.0/<start>/<end><br/>"   
        f"<br/>")  

@app.route("/api/v1.0/precipitation")
def precipitation():
    date=session.query(me.date).order_by(me.date.desc()).first()
    yeartodate=dt.date(2017, 8, 23) - dt.timedelta(days=364)
    prec2=session.query(me.prcp).filter(me.date >= yeartodate).order_by(me.date.desc()).all()
    prec_df=dict(prec2)
    return jsonify(prec_df)

@app.route("/api/v1.0/stations")
def stations():
    st_df= session.query(st.date, st.station)
    st_df= pd.read_sql(st_df.statement)
    return jsonify(st_df)

@app.route("/api/v1.0/tobs")
def tobs():
    max_date = session.query(me.date).order_by(me.date.desc()).first()
    yeartodate2=dt.datetime(2017, 8, 23) - dt.timedelta(days=365)
    tobs_df = session.query(me.date, me.tobs).filter(me.date >= yeartodate).order_by(me.date.desc()).all()
    tobs_df = list(tobs_df)
    return jsonify(tobs_list)


@app.route("/api/v1.0/<start>")
def start():
    yeartodate3=dt.datetime(2017, 8, 23) - dt.timedelta(days=365)
    dates2 = session.query(me.date, func.min(me.tobs), func.max(me.tobs), func.avg(me.tobs)).filter(me.date >= yeartodate).group_by(me.date).all()
    dates2_df=list(dates2)
    return jsonify(dates2_df)

@app.route("/api/v1.0/<start>/<end>")
def start_and_end(start=None, end=None):
    dates4 = session.query(me.date, func.min(me.tobs), func.max(me.tobs), func.avg(me.tobs)).filter(me.date >= start).filter(me.date <= end).group_by(me.date).all()
    dates4_df=list(dates4)
    return jsonify(dates4_df)

if __name__ == '__main__':
    app.run(debug=True)
