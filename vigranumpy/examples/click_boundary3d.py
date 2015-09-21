import vigra
import vigra.graphs as vigraph
import vigra.graphs as graphs
import pylab
import numpy as np

import sys
import matplotlib
import pylab as plt
import math
from matplotlib.widgets import Slider, Button, RadioButtons






# parameter:
imPath = ('holyRegion.h5', 'im')   # input image path
labPath = ('segMaskOnly.h5', 'data')   # labeled image path

# load volume
#labels = vigra.impex.readHDF5(*labPath).astype(np.uint32)
#volume = vigra.impex.readHDF5(*imPath)

volume = np.random.rand(4,5,5)
labels = np.random.rand(4,5,5).astype('uint32')


gridGraph = graphs.gridGraph(labels.shape)
rag = graphs.regionAdjacencyGraph(gridGraph, labels)

rand = np.random.rand(rag.edgeNum)*2-1

gui = vigra.graphs.TinyEdgeLabelGui(rag=rag, img=volume, edgeLabels=None, labelMode=True)
gui.startGui()
