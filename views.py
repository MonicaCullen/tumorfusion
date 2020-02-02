#!/usr/local/env python
# *-* coding:utf-8 *-*
#author:wuling
#date:2020/1/3
import os
import json
from datetime import datetime
from collections import OrderedDict

from sqlalchemy import or_,and_
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request,jsonify,render_template,redirect,url_for,make_response

from model import app,db,userInfo,groupInfo,sampleInfo,userId_groupId,userId_sampleId,groupId_sampleId

def filterBasic(unit):

    remain_keys = [
    "FusionName",
    "JunctionReadCount",
    "SpanningFragCount",
    "SpliceType",
    "RightBreakpoint",
    "LargeAnchorSupport",
    "annots",
    "dataset",
    "Run",
    "Phenotype",
    "chromtype",
    "fusion_type",
    "known_fusion"
    ]

    new_unit = dict()

    for key,val in unit.items():
        if key in remain_keys:
            new_unit[key] = val
    
    return new_unit

@app.route("/")
def home():
    response = make_response(render_template("home.html"),200)
    return response

@app.route("/login/")
def login():
    response = make_response(render_template("login.html"),200)
    return response

@app.route("/logout/")
def logout():
    return redirect("/")

@app.route("/search/")
def search():
    response = make_response(render_template("search.html"),200)
    return response

@app.route("/statics/")
def statics():
    response = make_response(render_template("statics.html"),200)
    return response

@app.route("/download/")
def download():
    response = make_response(render_template("download.html"),200)
    return response

@app.route("/submit/")
def submit():
    response = make_response(render_template("submit.html"),200)
    return response


@app.route("/gene/<gene_symbol>")
def searchByGeneSymbol(gene_symbol="IL1RAP"):
    records = sampleInfo.query.filter(or_(
        sampleInfo.leftgene_symbol==gene_symbol,
        sampleInfo.rightgene_symbol==gene_symbol)).all()

    responses = list()

    for record in records:

        res = dict()
        for key,val in record.__dict__.items():
            if not key.startswith('_') and not key.startswith('InstanceState') and val:
                res[key] = val

        responses.append(res)

    result = {
            "status": 200,
            "msg": "success",
            "data": responses
        }

    return jsonify(result)

@app.route("/fusion/<fusion_name>")
def searchByFusion(fusion_name="IL1RAP--FGF12"):
    records = sampleInfo.query.filter_by(FusionName=fusion_name).all()

    responses = list()

    for record in records:

        res = dict()
        for key,val in record.__dict__.items():
            if not key.startswith('_') and not key.startswith('InstanceState') and val:
                res[key] = val

        responses.append(res)

    result = {
            "status": 200,
            "msg": "success",
            "data": responses
        }

    return jsonify(result)

@app.route("/tumor/<tumor_type>")
def searchByTumorType(tumor_type="AML"):
    records = sampleInfo.query.filter(sampleInfo.known_fusion_disease.like("%" + tumor_type + "%")).all()

    responses = list()

    for record in records:

        res = dict()
        for key,val in record.__dict__.items():
            if not key.startswith('_') and not key.startswith('InstanceState') and val:
                res[key] = val

        responses.append(res)

    result = {
            "status": 200,
            "msg": "success",
            "data": responses
        }

    return jsonify(result)

@app.route("/run/<run_id>")
def searchByRun(run_id=""):

    records = sampleInfo.query.filter_by(Run=run_id).all()

    responses = list()

    for record in records:

        res = dict()
        for key,val in record.__dict__.items():
            if not key.startswith('_') and not key.startswith('InstanceState') and val:
                res[key] = val

        responses.append(res)

    result = {
            "status": 200,
            "msg": "success",
            "data": responses
        }

    return jsonify(result)

@app.route("/chr/<chromtype>/pos/<pos>/range/<range>")
def searchByBreakPoint(chromtype="chr3",pos=53043946,range=1000):

    query_condition = {
    or_(
        and_(
            sampleInfo.LeftBreakpointChr==chromtype,
            sampleInfo.LeftBreakpointPos>int(pos)-10,
            sampleInfo.LeftBreakpointPos<int(pos)+10
            ),
        and_(
            sampleInfo.RightBreakpointChr==chromtype,
            sampleInfo.RightBreakpointPos>int(pos)-10,
            sampleInfo.RightBreakpointPos<int(pos)+10
            )
        )
    }

    records = sampleInfo.query.filter(*query_condition).all()

    responses = list()

    for record in records:

        res = dict()
        for key,val in record.__dict__.items():
            if not key.startswith('_') and not key.startswith('InstanceState') and val:
                res[key] = val

        responses.append(res)

    result = {
            "status": 200,
            "msg": "success",
            "data": responses
        }

    return jsonify(result)

@app.route("/sample",methods=["POST"])
def searchSample():


    query_condition = {and_()}
        # or_(
        #     sampleInfo.leftgene_symbol==param["geneSymbol"],
        #     sampleInfo.rightgene_symbol==param["geneSymbol"],
        #     ),
        # sampleInfo.FusionName==param["fusionName"],
        # sampleInfo.known_fusion_disease.like("%" + param["tumorType"] + "%"),
        # sampleInfo.Run==request.form["runId"],
        # or_(
        # and_(
        #     sampleInfo.LeftBreakpointChr==request.form["tumorType"],
        #     sampleInfo.LeftBreakpointPos>int(pos)-int(rangelength),
        #     sampleInfo.LeftBreakpointPos<int(pos)-int(rangelength)
        #     ),
        # and_(
        #     sampleInfo.RightBreakpointChr==request.form["chr"],
        #     sampleInfo.RightBreakpointPos>int(pos)-int(rangelength),
        #     sampleInfo.RightBreakpointPos<int(pos)-int(rangelength),
        #     )
        # )

    geneSymbol = request.form["geneSymbol"]
    if geneSymbol:
        query_condition.add(or_(
            sampleInfo.leftgene_symbol==geneSymbol,
            sampleInfo.rightgene_symbol==geneSymbol,
            ))

    fusionName = request.form["fusionName"]
    if fusionName:
        query_condition.add(sampleInfo.FusionName==fusionName)

    tumorType = request.form["tumorType"]
    if tumorType:
        query_condition.add(sampleInfo.known_fusion_disease.like("%" + tumorType + "%"))


    runId = request.form["runId"]
    if runId:
        query_condition.add(sampleInfo.Run==runId)


    runId = request.form["runId"]
    if runId:
        query_condition.add(sampleInfo.Run==runId)


    chromtype = request.form["chr"]
    pos = request.form["pos"]
    rangelength = request.form["range"]

    if chromtype:

        if pos and rangelength:

            print("in",int(pos)-int(rangelength),int(pos)+int(rangelength))
            query_condition.add(or_(
                and_(
                    sampleInfo.LeftBreakpointChr==chromtype,
                    sampleInfo.LeftBreakpointPos>int(pos)-int(rangelength),
                    sampleInfo.LeftBreakpointPos<int(pos)+int(rangelength)
                    ),
                and_(
                    sampleInfo.RightBreakpointChr==chromtype,
                    sampleInfo.RightBreakpointPos>int(pos)-int(rangelength),
                    sampleInfo.RightBreakpointPos<int(pos)+int(rangelength),
                    )
                ))

        elif pos and not rangelength:
            query_condition.add(or_(
                  and_(
                    sampleInfo.LeftBreakpointChr==chromtype,
                    sampleInfo.LeftBreakpointPos==int(pos)
                    ),
                    and_(
                    sampleInfo.RightBreakpointChr==chromtype,
                    sampleInfo.RightBreakpointPos==int(pos)
                    )
                ))
        else:
            query_condition.add(or_(sampleInfo.LeftBreakpointChr==chromtype,sampleInfo.RightBreakpointChr==chromtype))


    records = sampleInfo.query.filter(*query_condition).all()
    print ('records',len(records))

    responses = list()

    for record in records:

        res = dict()
        for key,val in record.__dict__.items():
            if not key.startswith('_') and not key.startswith('InstanceState') and val:
                res[key] = val

        responses.append(res)

    result = {
            "status": 200,
            "msg": "success",
            "data": responses
        }

    return jsonify(result)

def main():
    app.run(host="0.0.0.0",port='80',threaded=True,debug=True)
    # app.run(host="0.0.0.0",port='80',threaded=True)

if __name__ == "__main__":
    main()

