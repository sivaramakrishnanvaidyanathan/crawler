__author__ = 'sivvaidyanathan'

import matplotlib.pyplot as plt, pandas as pd, numpy as np, ijson
from bokeh.charts import Histogram, output_file, show


file_name = "/Users/sivvaidyanathan/Documents/guides_dump_all_fields"
out_file = "/Users/sivvaidyanathan/Documents/dictionary_content"

leafCatTable = dict()
allCatTable = dict()

with open(file_name,'rb') as guide_rdr:
    for leafCats in ijson.items(guide_rdr, "response.docs.item.leafCats.item"):
        leafCatList = leafCats.split(" ")
        for leafCat in leafCatList:
            if leafCat in leafCatTable:
                leafCatTable[leafCat] += 1
            else:
                leafCatTable[leafCat] = 1

wtr = open(out_file, 'w+')

for key in leafCatTable:
    wtr.write(str(key) + "\t" + str(leafCatTable[key]) + "\n")



    # for allCats in ijson.items(guide_rdr, "response.docs.item.allCats.item"):
    #     allCatList = allCats.split(" ")
    #     for allCat in allCatList:
    #         if allCat in allCatTable:
    #             allCatTable[allCat] += 1
    #         else:
    #             allCatTable[allCat] = 1

# plt.bar(range(len(leafCatTable)), leafCatTable.values(), align='center')
# plt.xticks(range(len(leafCatTable)), leafCatTable.keys(), rotation=25)
# plt.show()

# plt.figure()
# df = pd.DataFrame(leafCatTable)
# df.plot.hist(alpha=0.5)
# plt.show()

# plt.figure()
# df = pd.DataFrame()
# df.plot.hist(df)
# plt.show()

p = Histogram(leafCatTable, label='CategoryDistribution', color='blue')
output_file("histogram.html",)
show(p)








