print "Loading Configuration"

# Simple test
# self.graphWidget.scene.addNode(ScreenOutputNode("screen1"), QtCore.QPointF(300,100))
# self.graphWidget.scene.addNode(VideoTestGenNode("video1"), QtCore.QPointF(100,100))
# self.graphWidget.scene.addWire('video1.out', 'screen1.in')

# Switcher control panel test
self.graphWidget.scene.addNode(VideoTestGenNode("video1"), QtCore.QPointF(0,0))
v1 = self.graphWidget.scene.addNode(VideoTestGenNode("video2"), QtCore.QPointF(0,100))
v1.device.pattern.set_value(1)
self.graphWidget.scene.addNode(Switcher4Node("switcher1"), QtCore.QPointF(200,0))
self.graphWidget.scene.addNode(ScreenOutputNode("screen1"), QtCore.QPointF(400,0))
self.graphWidget.scene.addNode(ScreenOutputNode("screen2"), QtCore.QPointF(400,100))

self.graphWidget.scene.addWire('video1.out', 'switcher1.in1')
self.graphWidget.scene.addWire('video2.out', 'switcher1.in2')
self.graphWidget.scene.addWire('switcher1.prog_out', 'screen1.in')
self.graphWidget.scene.addWire('switcher1.prev_out', 'screen2.in')