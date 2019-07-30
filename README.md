# TensorBoardNumpyToTSV

Class to flatten Numpy arrays and convert them into TSV or CSV

This was designed initially to take numpy arrays of embeddings and turn them into
a format that Tensorflow Projector (https://projector.tensorflow.org/) could understand

Usage:

```
#################################################

import numpy as np

array = np.random.rand(5, 3, 10)
labels = ["squirtle", "pikachu", "eevee", "mr.mime", "nidorina"]

#################################################

array_outpath = "C:/array.tsv"
labels_outpath = "C:/labels.tsv"

convert = ConvertNumpy()
convert.to_tsv(array, array_outpath)
convert.labels_to_tsv(labels, labels_outpath)

#################################################

array_outpath = "C:/array.csv"
labels_outpath = "C:/labels.csv"

convert = ConvertNumpy()
convert.to_csv(array, array_outpath)
convert.labels_to_csv(labels, labels_outpath)

#################################################

convert = ConvertNumpy()
convert.to_tsv(array, array_outpath)
convert.labels_to_csv(labels, labels_outpath)

#################################################
```
