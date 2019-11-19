import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaMetaData
from PyQt5.QtCore import Qt, QUrl
from ui import UI


def ms_to_time(ms):
    minutes = ms // 60000
    seconds = ms // 1000 % 60
    if minutes < 10:
        minutes = '0' + str(minutes)
    else:
        minutes = str(minutes)
    if seconds < 10:
        seconds = '0' + str(seconds)
    else:
        seconds = str(seconds)
    return f'{minutes}:{seconds}'


class Visard(QWidget, UI):
    def __init__(self):
        super().__init__()
        # Инициализация интерфейса в файле ui.py.
        self.player_window(self)
        # Изначально интерфейс выключен.
        self.UI_enabled = False

        # Создание плеера и установка частоты проверки позиции аудио на 250
        # миллисекунд (для правильной работы при ускоренном воспроизведении).
        self.player = QMediaPlayer()
        self.player.setNotifyInterval(250)

        # Здесь проверяется и выводится в консоль (для отлавливания
        # незапланированных рекурсий) состояние проигрывателя.
        self.status = self.player.mediaStatus()
        print(f'MS: {self.status}')
        self.player.mediaStatusChanged.connect(self.media_status)
        self.state = self.player.state()
        print(f'SS: {self.state}')
        self.player.stateChanged.connect(self.state_status)

        self.player.positionChanged.connect(self.change_position)

        self.open_button.clicked.connect(self.open_dialog)

        self.play_pause_button.clicked.connect(self.play_pause)
        self.stop_button.clicked.connect(self.stop)

        self.volume_slider.valueChanged.connect(self.player.setVolume)
        self.position_slider.sliderPressed.connect(self.change_position_freeze)
        self.position_slider.sliderReleased.connect(
                                                  self.change_position_unfreeze)

        self.player.metaDataChanged.connect(self.change_metadata)

    def change_metadata(self):
        artist = self.player.metaData(QMediaMetaData.ContributingArtist)
        title = self.player.metaData(QMediaMetaData.Title)
        if artist:
            self.artist_label.setText(artist)
        else:
            self.artist_label.setText('None')
        if title:
            self.title_label.setText(title)
        else:
            self.title_label.setText('None')

    def change_position_freeze(self):
        self.player.positionChanged.disconnect(self.change_position)
        self.position_slider.valueChanged.connect(self.change_position_label)

    def change_position_label(self, value):
        self.position_label.setText(ms_to_time(value))

    def change_position_unfreeze(self):
        self.player.setPosition(self.position_slider.value())
        self.position_slider.valueChanged.disconnect(self.change_position_label)
        self.player.positionChanged.connect(self.change_position)

    def change_position(self, position):
        self.position_slider.setSliderPosition(position)
        self.position_label.setText(ms_to_time(position))

    def keyPressEvent(self, event):
        """Если нажать на английскую M на клавиатуре, то выключится звук."""
        if self.UI_enabled:
            if event.key() == Qt.Key_M:
                if self.player.isMuted():
                    self.player.setMuted(False)
                    self.volume_slider.setEnabled(True)
                else:
                    self.player.setMuted(True)
                    self.volume_slider.setEnabled(False)

    def media_status(self, status):
        self.status = status
        print(f'MS: {status}')
        # Включение интерфейса по завершению загрузки аудио в буфер (код 3).
        if status == 3:
            self.position_slider.setMaximum(self.player.duration())
            self.duration_label.setText(ms_to_time(self.player.duration()))
            if not self.UI_enabled:
                self.UI_enabled = True
                self.play_pause_button.setEnabled(True)
                self.position_slider.setEnabled(True)
                self.volume_slider.setEnabled(True)
                self.position_label.setEnabled(True)
                self.duration_label.setEnabled(True)
                print('UIE!')
        # Возращение ползунка в начало, когда проигрывание остановится.
        if status == 7:
            self.player.setPosition(0)
            self.play_pause_button.setText('Play')
            self.stop_button.setEnabled(False)

    def state_status(self, state):
        self.state = state
        print(f'SS: {state}')

    def open_dialog(self):
        """Диалог выбора композиции."""
        track_directory = QFileDialog.getOpenFileName(self, 'Choose track', '',
                          'Music (*.flac *.ogg *.mp3 *.wav *.webm)')[0]
        # Проверка на отмену выбора, чтобы текущий трек оставался в буфере.
        if track_directory:
            if self.state == 1:
                self.play_pause_button.setText('Play')
            if self.state == 2:
                self.stop_button.setEnabled(False)
            self.player.setMedia(
                             QMediaContent(QUrl.fromLocalFile(track_directory)))

    def play_pause(self):
        # Код 0 - трек остановлен, код 2 - трек приостановлен.
        if self.state == 0 or self.state == 2:
            # Активирование стоп-кнопки, когда трек начнёт воспроизводится.
            if self.state == 0:
                self.stop_button.setEnabled(True)
            self.player.play()
            self.play_pause_button.setText('Pause')
        else:
            self.player.pause()
            self.play_pause_button.setText('Play')

    def stop(self):
        # Код 1 - трек воспроизводится.
        if self.state == 1:
            self.play_pause_button.setText('Play')
        self.player.stop()
        self.stop_button.setEnabled(False)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Visard()
    window.show()
    sys.exit(application.exec())