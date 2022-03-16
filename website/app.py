from flask import flash
from django.shortcuts import render
from Bio import Entrez 
from Bio.Entrez import efetch, read 

Entrez.email = "queenedelmarva@mail.ugm.ac.id"

#Get MeSH Terms
def button_search(pmid):
    return render(pmid, "home.html")

def get_mesh(pmid):
    handle = efetch(db='pubmed', id=str(pmid), retmode='xml')
    xml_data = read(handle)[0]

    if u'MeshHeadingList' in xml_data['MedlineCitation']:
        for mesh in xml_data['MedlineCitation'][u'MeshHeadingList']:
            major = 'N'
            qualifiers = mesh[u'QualifierName']
            if len(qualifiers) > 0:
                major = str(qualifiers[0].attributes.items()[0][1])
                descr = mesh[u'DescriptorName']
                name = descr.title()

                yield(name, major)

                print ('{}, {}'.format(name, major))
                data = '{}, {}'.format(name, major)

                return(pmid, "home.html", {'data':data})

# #Display Abstract 
# def get_abstract(pmid):
#     handle = Entrez.esearch(db='pubmed')
#     record = Entrez.read(handle)
#     print(record["absract"])