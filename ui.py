from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class UI():
    def player_window(self):
        self.resize(0, 300)
        self.setMinimumSize(0, 300)
        self.setWindowTitle('Visard')

        self.GL = QGridLayout(self)
        self.GL.setContentsMargins(5, 5, 5, 5)
        self.GL.setSpacing(5)

        self.open_button = QPushButton()
        self.open_button.setText('Open')
        self.GL.addWidget(self.open_button, 0, 0, 2, 1)

        self.artist_label = QLabel()
        self.artist_label.setAlignment(Qt.AlignRight)
        self.artist_label.setToolTip('Artist(s)')
        self.artist_label.setEnabled(False)
        self.GL.addWidget(self.artist_label, 0, 1, 1, 3)

        self.title_label = QLabel()
        self.title_label.setAlignment(Qt.AlignRight)
        self.title_label.setToolTip('Title')
        self.title_label.setEnabled(False)
        self.GL.addWidget(self.title_label, 1, 1, 1, 3)

        self.volume_slider = QSlider()
        self.volume_slider.setMaximum(100)
        self.volume_slider.setSliderPosition(100)
        self.volume_slider.setToolTip('Volume')
        self.volume_slider.setEnabled(False)
        self.GL.addWidget(self.volume_slider, 2, 0, 1, 1)

        self.image_label = QLabel()
        self.image_label.setScaledContents(True)
        self.GL.addWidget(self.image_label, 2, 1, 1, 3)

        self.position_label = QLabel()
        self.position_label.setText('00:00')
        self.position_label.setEnabled(False)
        self.GL.addWidget(self.position_label, 3, 0, 1, 2)

        self.duration_label = QLabel()
        self.duration_label.setAlignment(Qt.AlignRight)
        self.duration_label.setText('00:00')
        self.duration_label.setEnabled(False)
        self.GL.addWidget(self.duration_label, 3, 2, 1, 2)

        self.position_slider = QSlider()
        self.position_slider.setOrientation(Qt.Horizontal)
        self.position_slider.setEnabled(False)
        self.GL.addWidget(self.position_slider, 4, 0, 1, 4)

        self.play_pause_button = QPushButton()
        self.play_pause_button.setText('Play')
        self.play_pause_button.setEnabled(False)
        self.GL.addWidget(self.play_pause_button, 5, 0, 1, 1)

        self.stop_button = QPushButton()
        self.stop_button.setText('Stop')
        self.stop_button.setEnabled(False)
        self.GL.addWidget(self.stop_button, 5, 1, 1, 1)

        self.settings_button = QPushButton()
        self.settings_button.setText('Settings')
        self.GL.addWidget(self.settings_button, 5, 3, 1, 1)

        font = QFont()
        font.setPointSize(15)
        self.setFont(font)

        font.setPointSize(10)
        self.artist_label.setFont(font)