import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QBrush, QColor, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDial, QSlider, QLabel

class _Bar(QWidget):
    def __init__(self):
        super().__init__()
        self._padding = 2
        self._bar_solid_percent = 0.9
        self._background_color = QColor("gray")
        self._n_steps = 10
        self._steps = [QColor("red") for _ in range(self._n_steps)]

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self._background_color)
        painter.drawRect(0, 0, self.width(), self.height())

        rect = QtCore.QRect(0, 0, self.width(), self.height())
        rect.setLeft(self._padding)
        rect.setRight(self.width() - self._padding)
        rect.setHeight(rect.height() * self._bar_solid_percent)

        brush = QBrush(Qt.SolidPattern)
        for i in range(self._n_steps):
            brush.setColor(self._steps[i])
            painter.setBrush(brush)
            painter.drawRect(rect)
            rect.translate(0, rect.height())

class PowerBar(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self._bar = _Bar()
        layout.addWidget(self._bar)

        self._dial = QDial()
        self._dial.setNotchesVisible(True)
        self._dial.setRange(0, 100)
        self._dial.valueChanged[int].connect(self._on_dial_value_changed)
        layout.addWidget(self._dial)

        self._slider = QSlider(Qt.Horizontal)
        self._slider.setRange(0, 100)
        self._slider.valueChanged[int].connect(self._on_slider_value_changed)
        layout.addWidget(self._slider)

        self._label = QLabel("")
        layout.addWidget(self._label)

        self.setLayout(layout)

    def _on_dial_value_changed(self, value):
        self._slider.setValue(value)
        self._update_bar()

    def _on_slider_value_changed(self, value):
        self._dial.setValue(value)
        self._update_bar()

    def _update_bar(self):
        n_steps = self._slider.value()
        padding = int(n_steps / 10)
        solid_percent = n_steps / 100
        self._bar._padding = padding
        self._bar._bar_solid_percent = solid_percent
        self._bar._n_steps = n_steps
        self._bar.update()

        color = QColorDialog.getColor()
        if color.isValid():
            self._bar._background_color = color
            self._bar.update()

def main():
    app = QApplication(sys.argv)
    volume = PowerBar()
    volume.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
