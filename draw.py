from caffe2.python import net_drawer
from IPython import display
graph = net_drawer.GetPydotGraph(train_model.net.Proto().op,"mnist",rankdir="LR")
display.Image(graph.create_png(), width=800)
graph.write_png('graph.png')

