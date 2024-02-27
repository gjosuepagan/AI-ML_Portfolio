from bs4 import BeautifulSoup
import json
import urllib.request
# url = 'http://nbviewer.jupyter.org/url/jakevdp.github.com/downloads/notebooks/XKCD_plots.ipynb'
# response = urllib.request.urlopen(url)
#  for local html file
response = open("./REGRESSION/Cars4U_GelsonJPaganDiaz_AIML.html", encoding='utf-8')
text = response.read()

soup = BeautifulSoup(text, 'lxml')
# see some of the html
print(soup.div)
dictionary = {'nbformat': 4, 'nbformat_minor': 1, 'cells': [], 'metadata': {}}
for d in soup.findAll("div"):
    if 'class' in d.attrs.keys():
        for clas in d.attrs["class"]:
            if clas in ["jp-Cell-inputWrapper", "jp-Cell jp-CodeCell jp-Notebook-cell"]:
                if clas == "input_area":
                    cell = {}
                    cell['metadata'] = {}
                    cell['outputs'] = []
                    cell['source'] = [d.get_text()]
                    cell['execution_count'] = None
                    cell['cell_type'] = 'type'
                    print(f"Code Cell: {cell['source']}")
                    dictionary['cells'].append(cell)
                else:
                    cell = {}
                    cell['metadata'] = {}
                    cell['source'] = [d.decode_contents()]
                    cell['cell_type'] = 'markdown'
                    print(f"Markdown Cell: {cell['source']}")
                    dictionary['cells'].append(cell)
open('CarPricing_Regression.ipynb', 'w').write(json.dumps(dictionary))