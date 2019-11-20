from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QSlider, QLabel, QHBoxLayout,\
                            QWidget, QSpacerItem, QVBoxLayout
from PyQt5.QtCore import Qt


class UI():
    def player_window(self, window):
        # Инициализация окна, его размеров и ограничение на его масштабирование.
        window.resize(500, 300)
        window.setWindowTitle('Visard')
        window.setMaximumSize(500, 300)
        window.setMinimumSize(500, 300)

        # Создание виджета и горизонтальной сеточной разметки в нём для кнопок в
        # нижней части окна.
        self.HLW = QWidget(window)
        self.HLW.setGeometry(0, 250, 500, 50)

        self.HL = QHBoxLayout(self.HLW)
        self.HL.setContentsMargins(5, 5, 5, 5)
        self.HL.setSpacing(5)

        # Создание виджета и вертикальной сеточной разметки в нём для текстовых
        # ярлыков автора и названия трека.
        self.VLW = QWidget(window)
        self.VLW.setGeometry(118.75, 0, 381.25, 50)

        self.VL = QVBoxLayout(self.VLW)
        self.VL.setContentsMargins(5, 5, 5, 5)
        self.VL.setSpacing(0)

        # Создание кнопки, открывающей окно выбора файла.
        self.open_button = QPushButton(window)
        self.open_button.setGeometry(5, 5, 118.75, 40)
        self.open_button.setText('Open')
        # Создание кнопки, отвечающей за включение/паузу проигрывания аудио.
        self.play_pause_button = QPushButton(self.HLW)
        self.HL.addWidget(self.play_pause_button)
        self.play_pause_button.setEnabled(False)
        self.play_pause_button.setText('Play')
        # Создание кнопки, отвечающей за полную остановку проигрывания аудио.
        self.stop_button = QPushButton(self.HLW)
        self.HL.addWidget(self.stop_button)
        self.stop_button.setEnabled(False)
        self.stop_button.setText('Stop')
        # Пробел для выравнивания разметки.
        self.space = QSpacerItem(118.75, 40)
        self.HL.addItem(self.space)
        # Создание кнопки, открывающей окно настроек.
        self.settings_button = QPushButton(self.HLW)
        self.HL.addWidget(self.settings_button)
        self.settings_button.setText('Settings')

        # Cоздание текстового ярлыка с информацией о позиции проигрывания трека.
        self.position_label = QLabel(window)
        self.position_label.setGeometry(5, 200, 75, 20)
        self.position_label.setEnabled(False)
        self.position_label.setText('00:00')
        # Cоздание текстового ярлыка с информацией о длительности трека.
        self.duration_label = QLabel(window)
        self.duration_label.setGeometry(420, 200, 75, 20)
        self.duration_label.setAlignment(Qt.AlignRight)
        self.duration_label.setEnabled(False)
        self.duration_label.setText('00:00')

        # Ползунок, который показывает позицию трека и позволять её изменять.
        self.position_slider = QSlider(window)
        self.position_slider.setGeometry(5, 225, 490, 25)
        self.position_slider.setOrientation(Qt.Horizontal)
        self.position_slider.setEnabled(False)
        # Ползунок для изменения громкости.
        self.volume_slider = QSlider(window)
        self.volume_slider.setGeometry(470, 50, 25, 145)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setSliderPosition(100)
        self.volume_slider.setEnabled(False)
        self.volume_slider.setToolTip('Volume')

        # Cоздание текстового ярлыка с информацией об авторе трека.
        self.artist_label = QLabel(window)
        self.VL.addWidget(self.artist_label)
        self.artist_label.setAlignment(Qt.AlignRight|Qt.AlignBottom)
        # Cоздание текстового ярлыка с информацией о название трека.
        self.title_label = QLabel(window)
        self.VL.addWidget(self.title_label)
        self.title_label.setAlignment(Qt.AlignRight|Qt.AlignTop)

        # Указание размера шрифта для окна и его элементов.
        font = QFont()
        font.setPointSize(15)
        window.setFont(font)

        font = QFont()
        font.setFamily('Monospace')
        self.position_label.setFont(font)
        self.duration_label.setFont(font)

        font = QFont()
        font.setPointSize(10)
        self.artist_label.setFont(font)