__author__ = 'sivvaidyanathan'

in_file = "/Users/sivvaidyanathan/Documents/dictionary_content"

import matplotlib.pyplot as plt, pandas as pd, numpy as np, ijson
from bokeh.charts import Bar, Histogram, output_file, show


rdr = open(in_file, 'r')
leafCatIds  = list()
leafCatGuideCounts = list()

table = dict()

for line in rdr:
    line = line.strip()
    parts = line.split("\t")
    if len(parts) == 2:
        table[parts[0]] = parts[1]
        # leafCatIds.append(parts[0])
        # leafCatGuideCounts.append(int(parts[1]))

output_file("/Users/sivvaidyanathan/Documents/bar.html")
hist = Bar(pd.DataFrame({"categories":table.keys(), "counts": table.values()}), title="guide_histogram", xlabel='categories', ylabel='values', width=400, height=400)
show(hist)

#df.iplot(kind='histogram', subplots=True, shape=(3, 1), filename='histogram-subplots')

