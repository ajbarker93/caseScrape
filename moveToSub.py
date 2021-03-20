from docx import Document
import json
import os
import numpy as np

rootdir = "/Users/adambarker/case_scrape/"
docdir = rootdir+"documents/"
outdir = rootdir+"docToText2/"
onlyfiles = [f for f in os.listdir(docdir) if os.path.isfile(os.path.join(docdir, f))]

i=0
for file in onlyfiles:
    subf = file.split(".")[0][-2:]
    try:
        if not os.path.exists(outdir+subf):
            os.makedirs(outdir+subf)

        document = Document(docdir+file)
        lines = [para.text for para in document.paragraphs]
        lines = " ".join(lines)
        i = i+1

        with open(outdir+subf+"/"+file.split(".")[0]+'.txt', 'w') as outfile:
            print("Processing ",file)
            outfile.write(lines)

    except:
        print("Issue with "+ file)
