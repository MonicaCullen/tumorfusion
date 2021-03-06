create table userInfo(
userId VARCHAR(50) NOT NULL UNIQUE,
userName VARCHAR(50) NOT NULL,
userPassword VARCHAR(50) NOT NULL,
userGender VARCHAR(50),
userEmail VARCHAR(100),
userCompany VARCHAR(200),
userDesc VARCHAR(500)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table groupInfo(
groupId VARCHAR(50) NOT NULL UNIQUE,
groupName VARCHAR(50) NOT NULL,
groupDescribtion VARCHAR(500)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table sampleInfo(
_id INT AUTO_INCREMENT PRIMARY KEY,
sampleId VARCHAR(50) NOT NULL,
FusionName VARCHAR(100),
JunctionReadCount VARCHAR(10),
SpanningFragCount VARCHAR(10),
SpliceType VARCHAR(100),
LeftGene VARCHAR(100),
LeftBreakpoint VARCHAR(100),
RightGene VARCHAR(100),
RightBreakpoint VARCHAR(100),
JunctionReads TEXT(100000),
SpanningFrags TEXT(100000),
LargeAnchorSupport VARCHAR(10),
FFPM VARCHAR(10),
LeftBreakDinuc VARCHAR(10),
LeftBreakEntropy VARCHAR(10),
RightBreakDinuc VARCHAR(10),
RightBreakEntropy VARCHAR(10),
annots VARCHAR(1000),
dataset VARCHAR(10),
Run VARCHAR(10),
Phenotype VARCHAR(10),
chromtype VARCHAR(100),
leftgene_symbol VARCHAR(10),
rightgene_symbol VARCHAR(100),
left_gene VARCHAR(100),
right_gene VARCHAR(100),
fusion_type VARCHAR(100),
known_fusion VARCHAR(1000),
source VARCHAR(1000),
known_fusion_disease VARCHAR(1000),
LeftBreakpointChr VARCHAR(10),
LeftBreakpointPos INT,
LeftBreakpointSymbol VARCHAR(10),
RightBreakpointChr VARCHAR(10),
RightBreakpointPos INT,
RightBreakpointSymbol VARCHAR(10)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table userId_groupId(
_id INT AUTO_INCREMENT PRIMARY KEY,
userId VARCHAR(50) NOT NULL,
groupId VARCHAR(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table groupId_sampleId(
_id INT AUTO_INCREMENT PRIMARY KEY,
groupId VARCHAR(50) NOT NULL,
sampleId VARCHAR(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table userId_sampleId(
_id INT AUTO_INCREMENT PRIMARY KEY,
userId VARCHAR(50) NOT NULL,
sampleId VARCHAR(50) NOT NULL,
sampleStatus VARCHAR(20) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table cosmic_gene_census_allTue(
_id INT AUTO_INCREMENT PRIMARY KEY,
gene_symbol VARCHAR(10) NOT NULL,
name VARCHAR(1000),
entrez_geneid VARCHAR(10),
genome_location VARCHAR(100),
tier VARCHAR(10),
hallmark VARCHAR(10),
chr_band VARCHAR(10),
somatic VARCHAR(10),
germline VARCHAR(10),
tumour_types_somatic VARCHAR(1000),
tumour_types_germline VARCHAR(100),
cancer_syndrome VARCHAR(100),
tissue_type VARCHAR(100),
molecular_genetics VARCHAR(10),
role_in_cancer VARCHAR(100),
mutation_types VARCHAR(100),
translocation_partner VARCHAR(1000),
other_germline_mut VARCHAR(10),
other_syndrome VARCHAR(1000),
synonyms VARCHAR(1000)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;