from PySide2 import QtCore, QtGui, QtWidgets


class ImageViewer(QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        self.has_image = False
        self.scene = QtWidgets.QGraphicsScene(self)
        self.image_path = None
        self.image = QtWidgets.QGraphicsPixmapItem()
        self.scene.addItem(self.image)
        self.setScene(self.scene)

        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setFrameShape(QtWidgets.QFrame.NoFrame)

    def set_image(self, path):
        if path == "" or path.isspace():
            return
        image_pixmap = QtGui.QPixmap(path)
        if image_pixmap.isNull():
            return
        self.has_image = True
        self.image_path = path
        self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.image.setPixmap(image_pixmap)

    def clear_image(self):
        self.has_image = False
        self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.image.setPixmap(QtGui.QPixmap())

    def wheelEvent(self, event):
        if not self.does_have_image():
            return
        factor = 1.0
        if event.angleDelta().y() > 0:
            factor = 1.25
        elif event.angleDelta().y() < 0:
            factor = 0.8
        self.scale(factor, factor)

    def does_have_image(self):
        return self.has_image
