from docx import Document
import json
from os import listdir
from os.path import isfile, join

rootdir = "/Users/adambarker/case_scrape/"
docdir = rootdir+"documents/"
outdir = rootdir+"documents_to_text/"
onlyfiles = [f for f in listdir(docdir) if isfile(join(docdir, f))]

for file in onlyfiles:
    try:
        document = Document(docdir+file)
        lines = [para.text for para in document.paragraphs]
        lines = " ".join(lines)
        with open(outdir+file.split(".")[0]+'.txt', 'w') as outfile:
            print("Processing ",file)
            outfile.write(lines)
    except:
        print("Issue with "+ file)
