from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QSlider, QLabel, QHBoxLayout,\
                            QWidget, QSpacerItem
from PyQt5.QtCore import Qt


class UI():
    def player_window(self, window):
        # Инициализация окна, его размеров и ограничение на его масштабирование.
        window.resize(500, 300)
        window.setWindowTitle('Visard')
        window.setMinimumSize(500, 300)
        window.setMaximumSize(500, 300)

        # Указание размера шрифта для всех элементов окна.
        self.font_size = QFont()
        self.font_size.setPointSize(15)
        window.setFont(self.font_size)

        # Создание кнопки, открывающей окно выбора файла.
        self.open_button = QPushButton(window)
        self.open_button.setGeometry(5, 5, 118.75, 40)
        self.open_button.setText('Open')

        #
        self.HLW = QWidget(window)
        self.HLW.setGeometry(0, 255, 500, 45)
        self.HL = QHBoxLayout(self.HLW)
        self.HL.setContentsMargins(5, 0, 5, 5)
        self.HL.setSpacing(5)

        # Создание кнопки, отвечающей за включение/паузу проигрывания аудио.
        self.play_pause_button = QPushButton(self.HLW)
        self.HL.addWidget(self.play_pause_button)
        self.play_pause_button.setEnabled(False)
        self.play_pause_button.setText('Play')

        # Создание кнопки, отвечающей за полную остановку проигрывания аудио.
        self.stop_button = QPushButton(self.HLW)
        self.stop_button.setEnabled(False)
        self.HL.addWidget(self.stop_button)
        self.stop_button.setText('Stop')

        # Ползунок, который будет показывать позицию трека и позволять её
        # изменять.
        self.position_slider = QSlider(window)
        self.position_slider.setEnabled(False)
        self.position_slider.setOrientation(Qt.Horizontal)
        self.position_slider.setGeometry(5, 225, 490, 25)

        #
        self.font_mono = QFont()
        self.font_mono.setFamily('Monospace')

        #
        self.position_label = QLabel(window)
        self.position_label.setEnabled(False)
        self.position_label.setGeometry(5, 200, 75, 20)
        self.position_label.setFont(self.font_mono)
        self.position_label.setText('00:00')

        #
        self.duration_label = QLabel(window)
        self.duration_label.setEnabled(False)
        self.duration_label.setGeometry(420, 200, 75, 20)
        self.duration_label.setAlignment(Qt.AlignRight)
        self.duration_label.setFont(self.font_mono)
        self.duration_label.setText('00:00')

        #
        self.volume_slider = QSlider(window)
        self.volume_slider.setToolTip('Volume')
        self.volume_slider.setEnabled(False)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setSliderPosition(100)
        self.volume_slider.setGeometry(470, 50, 25, 145)

        #
        self.space = QSpacerItem(118.75, 40)
        self.HL.addItem(self.space)

        # Создание кнопки, открывающей окно настроек.
        self.settings_button = QPushButton(self.HLW)
        self.HL.addWidget(self.settings_button)
        self.settings_button.setText('Settings')

        #
        self.font_artist = QFont()
        self.font_artist.setPointSize(10)

        #
        self.artist_label = QLabel(window)
        self.artist_label.setGeometry(127.75, 5, 367.25, 15)
        self.artist_label.setAlignment(Qt.AlignRight)
        self.artist_label.setFont(self.font_artist)

        #
        self.font_title = QFont()
        self.font_title.setPointSize(15)

        #
        self.title_label = QLabel(window)
        self.title_label.setGeometry(127.75, 20, 367.25, 25)
        self.title_label.setAlignment(Qt.AlignRight)
        self.title_label.setFont(self.font_title)