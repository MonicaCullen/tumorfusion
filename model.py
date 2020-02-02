#!/usr/local/env python
# *-* coding:utf-8 *-*
#author:wuling
#date:2020/1/19
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://debian-sys-maint:Ob1gqURuuLAFZrwi@localhost:3306/tumor_candidate_fusion_gene'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gongyh:gongyh@ln01@192.168.1.199:33306/tumor_candidate_fusion_gene'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app)
current_path = os.path.dirname(os.path.abspath(__name__))

class userInfo(db.Model):

    userId = db.Column(db.String(50),primary_key=True,unique=True)
    userName = db.Column(db.String(50))
    userPassword = db.Column(db.String(50))
    userGender = db.Column(db.String(50))
    userEmail = db.Column(db.String(100))
    userCompany = db.Column(db.String(200))
    userDesc = db.Column(db.String(500))

    __tablename__ = 'userInfo'

    def __init__(self,userId,userName,userPassword,userGender,userEmail,userCompany,userDesc):

        self.userId = userId
        self.userName = userName
        self.userPassword = userPassword
        self.userGender = userGender
        self.userEmail = userEmail
        self.userCompany = userCompany
        self.userDesc = userDesc

class groupInfo(db.Model):

    groupId = db.Column(db.String(50),primary_key=True,unique=True)
    groupName = db.Column(db.String(50))
    groupDescribtion = db.Column(db.String(500))

    __tablename__ = 'groupInfo'

    def __init__(self,groupId,groupName,groupDescribtion):
        
        self.groupId = groupId
        self.groupName = groupName
        self.groupDescribtion = groupDescribtion

class sampleInfo(db.Model):
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    sampleId = db.Column(db.String(50))
    FusionName = db.Column(db.String(100))
    JunctionReadCount = db.Column(db.String(10))
    SpanningFragCount = db.Column(db.String(10))
    SpliceType = db.Column(db.String(100))
    LeftGene = db.Column(db.String(100))
    LeftBreakpoint = db.Column(db.String(100))
    RightGene = db.Column(db.String(100))
    RightBreakpoint = db.Column(db.String(100))
    JunctionReads = db.Column(db.String(100000))
    SpanningFrags = db.Column(db.String(100000))
    LargeAnchorSupport = db.Column(db.String(10))
    FFPM = db.Column(db.String(10))
    LeftBreakDinuc = db.Column(db.String(10))
    LeftBreakEntropy = db.Column(db.String(10))
    RightBreakDinuc = db.Column(db.String(10))
    RightBreakEntropy = db.Column(db.String(10))
    annots = db.Column(db.String(1000))
    dataset = db.Column(db.String(10))
    Run = db.Column(db.String(10))
    Phenotype = db.Column(db.String(10))
    chromtype = db.Column(db.String(100))
    leftgene_symbol = db.Column(db.String(10))
    rightgene_symbol = db.Column(db.String(100))
    left_gene = db.Column(db.String(100))
    right_gene = db.Column(db.String(100))
    fusion_type = db.Column(db.String(100))
    known_fusion = db.Column(db.String(1000))
    source = db.Column(db.String(1000))
    known_fusion_disease = db.Column(db.String(1000))
    LeftBreakpointChr = db.Column(db.String(10))
    LeftBreakpointPos = db.Column(db.Integer)
    LeftBreakpointSymbol = db.Column(db.String(10))
    RightBreakpointChr = db.Column(db.String(10))
    RightBreakpointPos = db.Column(db.Integer)
    RightBreakpointSymbol = db.Column(db.String(10))

    __tablename__ = 'sampleInfo'

    def __init__(self,sampleId,FusionName, JunctionReadCount, SpanningFragCount, 
        SpliceType, LeftGene, LeftBreakpoint, RightGene, RightBreakpoint, 
        JunctionReads, SpanningFrags, LargeAnchorSupport, FFPM, LeftBreakDinuc, 
        LeftBreakEntropy, RightBreakDinuc, RightBreakEntropy, annots, dataset, 
        Run, Phenotype, chromtype, leftgene_symbol, rightgene_symbol, left_gene, 
        right_gene, fusion_type, known_fusion, source, known_fusion_disease,
        LeftBreakpointChr,LeftBreakpointPos,LeftBreakpointSymbol,
        RightBreakpointChr,RightBreakpointPos,RightBreakpointSymbol):

                self.sampleId = sampleId
                self.FusionName = FusionName
                self.JunctionReadCount = JunctionReadCount
                self.SpanningFragCount = SpanningFragCount
                self.SpliceType = SpliceType
                self.LeftGene = LeftGene
                self.LeftBreakpoint = LeftBreakpoint
                self.RightGene = RightGene
                self.RightBreakpoint = RightBreakpoint
                self.JunctionReads = JunctionReads
                self.SpanningFrags = SpanningFrags
                self.LargeAnchorSupport = LargeAnchorSupport
                self.FFPM = FFPM
                self.LeftBreakDinuc = LeftBreakDinuc
                self.LeftBreakEntropy = LeftBreakEntropy
                self.RightBreakDinuc = RightBreakDinuc
                self.RightBreakEntropy = RightBreakEntropy
                self.annots = annots
                self.dataset = dataset
                self.Run = Run
                self.Phenotype = Phenotype
                self.chromtype = chromtype
                self.leftgene_symbol = leftgene_symbol
                self.rightgene_symbol = rightgene_symbol
                self.left_gene = left_gene
                self.right_gene = right_gene
                self.fusion_type = fusion_type
                self.known_fusion = known_fusion
                self.source = source
                self.known_fusion_disease = known_fusion_disease
                self.LeftBreakpointChr = LeftBreakpointChr
                self.LeftBreakpointPos = LeftBreakpointPos
                self.LeftBreakpointSymbol = LeftBreakpointSymbol
                self.RightBreakpointChr = RightBreakpointChr
                self.RightBreakpointPos = RightBreakpointPos
                self.RightBreakpointSymbol = RightBreakpointSymbol

class userId_groupId(db.Model):

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.String(50))
    groupId = db.Column(db.String(50))

    __tablename__ = 'userId_groupId'

    def __init__(self,userId,groupId):
        
        self.userId = userId
        self.groupId = groupId

class userId_sampleId(db.Model):

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.String(50))
    sampleId = db.Column(db.String(50))
    sampleStatus = db.Column(db.String(20))

    __tablename__ = 'userId_sampleId'

    def __init__(self,userId,sampleId,sampleStatus):
        
        self.userId = userId
        self.sampleId = userId
        self.sampleStatus = sampleStatus

class groupId_sampleId(db.Model):

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    groupId = db.Column(db.String(50))
    sampleId = db.Column(db.String(50))

    __tablename__ = 'groupId_sampleId'

    def __init__(self,groupId,sampleId):
        
        self.groupId = groupId
        self.sampleId = sampleId

def insertUser(data):

    unit = userInfo(*data)

    db.session.add(unit)

    db.session.commit()

def insertGroup(data):

    unit = groupInfo(*data)

    db.session.add(unit)

    db.session.commit()

def insertSample():

    filepath = os.path.join(current_path,"data","original","SRP027383_known_fusion_event.txt")

    sampleId = ["94a2f18e-3a63-11ea-b387-507b9db4bad0"]

    with open(filepath) as rf:

        n = 0

        for line in rf:

            if n != 0:
                data = sampleId +[d.strip() for d in line.split('\t')]

                LeftBreakpoint = data[6]
                RightBreakpoint = data[8]

                data += LeftBreakpoint.split(":")
                data += RightBreakpoint.split(":")

                # LeftBreakpointChr,LeftBreakpointPos,LeftBreakpointSymbol = LeftBreakpoint.split(":")
                # RightBreakpointChr,RightBreakpointPos,RightBreakpointSymbol = RightBreakpoint.split(":")

                print (n)

                unit = sampleInfo(*data)

                db.session.add(unit)

                db.session.commit()

            n += 1

def insertUserGroup(data):

    unit = userId_groupId(*data)

    db.session.add(unit)

    db.session.commit()

def insertUserSample(data):

    unit = userId_sampleId(*data)

    db.session.add(unit)

    db.session.commit()

def insertGroupSample(data):

    unit = groupId_sampleId(*data)

    db.session.add(unit)

    db.session.commit()

def main():
    # data = ["bf80decc-3a70-11ea-b387-507b9db4bad0","myhealthgene","myhealthgene","","","wky",""]
    # insertUser(data)

    # data = ["a685bb6c-3a7b-11ea-b387-507b9db4bad0","myhealthgeneGroup",""]
    # insertGroup(data)

    insertSample()
    
    # data = ["bf80decc-3a70-11ea-b387-507b9db4bad0","a685bb6c-3a7b-11ea-b387-507b9db4bad0"]
    # insertUserGroup(data)

    # data = ["bf80decc-3a70-11ea-b387-507b9db4bad0","94a2f18e-3a63-11ea-b387-507b9db4bad0","public"]
    # insertUserSample(data)

    # data = ["a685bb6c-3a7b-11ea-b387-507b9db4bad0","94a2f18e-3a63-11ea-b387-507b9db4bad0"]
    # insertGroupSample(data)

if __name__ == "__main__":
    main()