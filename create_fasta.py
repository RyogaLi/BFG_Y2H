import pandas as pd
import os
from param import *

def create_fasta(AD_summary, DB_summary, output_path, group_spec=False, AD="G0", DB="G0"):

    """
    Generate fasta file from summary
    See example_summary as templete
    """

    AD_summary = pd.read_table(AD_summary, sep="\t")
    DB_summary = pd.read_table(DB_summary, sep="\t")
    
    if group_spec: # make a group specific fasta file
        # select the group from AD and DB
        AD_summary = AD_summary[AD_summary.Group==AD]
        DB_summary = DB_summary[DB_summary.Group==DB]
        # fasta filename
        f_ad = "y_AD_"+AD+".fasta" 
        f_db = "y_DB_"+DB+".fasta"
    else:
        f_ad = "y_AD_all.fasta"
        f_db = "y_DB_all.fasta"

    with open(os.path.join(output_path,f_ad), "w") as ad:
            
        for index, row in AD_summary.iterrows():
            up_seq_name = ">"+row.Group+";"+row.Locus+";"+str(row.Index)+";"+"up"
            ad.write(up_seq_name+"\n")
            ad.write(AD_Up1+row.UpTag_Sequence+AD_Up2+"\n") # add padding sequences

            dn_seq_name = ">"+row.Group+";"+row.Locus+";"+str(row.Index)+";"+"dn"
            ad.write(dn_seq_name+"\n")
            ad.write(AD_Dn1+row.DnTag_Sequence+AD_Dn2+"\n")

    with open(os.path.join(output_path, f_db), "w") as db:
            
        for index, row in DB_summary.iterrows():
            up_seq_name = ">"+row.Group+";"+row.Locus+";"+str(row.Index)+";"+"up"
            db.write(up_seq_name+"\n")
            db.write(DB_Up1+row.UpTag_Sequence+DB_Up2+"\n")

            dn_seq_name = ">"+row.Group+";"+row.Locus+";"+str(row.Index)+";"+"dn"
            db.write(dn_seq_name+"\n")
            db.write(DB_Dn1+row.DnTag_Sequence+DB_Dn2+"\n")


def build_index(fasta_file):
    """
    Bowtie build for fasta_file
    """
    pass