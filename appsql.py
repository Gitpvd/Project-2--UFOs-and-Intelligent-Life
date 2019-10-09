import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine
listofshapes=[]
listofstates=[]
def SetupTables(csvFileUFO,csvFileUSCities):
    engine =create_engine('sqlite:///UFO_db' )
    df = pd.read_csv('nuforc_reports.csv')
    df.to_sql("UFO_DB",con=engine)
    df1 = pd.read_csv('uscitiesv1.5.csv')
    df1.to_sql("US_Cities",con=engine)
    listofshapes = df['shape'].unique()
    listofstates = df['state'].unique()

def GetSample(df,n):
    df1 = df.sample(n)
    return df1

listofCSVs=['nuforc_reports.csv','uscitiesv1.5.csv']
def CreateUFOSql(listofCSVs):
    for  f in listofCSVs:


         

    