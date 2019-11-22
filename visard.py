import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaMetaData
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QUrl
from ui import UI


def ms_to_time(ms):
    minutes = ms // 60000
    seconds = ms // 1000 % 60
    if minutes < 10:
        minutes = f'0{str(minutes)}'
    else:
        minutes = str(minutes)
    if seconds < 10:
        seconds = f'0{str(seconds)}'
    else:
        seconds = str(seconds)
    return f'{minutes}:{seconds}'


class Visard(QWidget, UI):
    def __init__(self):
        super().__init__()
        self.player_window()
        self.UI = False

        self.player = QMediaPlayer()
        self.player.setNotifyInterval(1)

        self.player.mediaStatusChanged.connect(self.media_status_changed)
        self.state = 0
        self.player.stateChanged.connect(self.state_changed)
        self.player.durationChanged.connect(self.duration_changed)
        self.player.positionChanged.connect(self.position_changed)
        self.player.metaDataChanged.connect(self.change_metadata)

        self.open_button.clicked.connect(self.open_dialog)

        self.volume_slider.valueChanged.connect(self.player.setVolume)

        self.position_slider.sliderPressed.connect(self.change_position_freeze)
        self.position_slider.sliderReleased.connect(
                                                  self.change_position_unfreeze)

        self.play_pause_button.clicked.connect(self.play_pause)
        self.stop_button.clicked.connect(self.stop)

    def media_status_changed(self, media_status):
        self.media_status = media_status
        if media_status == 7:
            self.player.setPosition(0)
            self.play_pause_button.setText('Play')
        print(f'MS: {media_status}!')

    def state_changed(self, state):
        self.state = state
        print(f'S: {state}!')

    def duration_changed(self, duration):
        self.duration_label.setText(ms_to_time(duration))
        self.position_slider.setMaximum(duration)
        print('DC!')

    def position_changed(self, position):
        self.position_label.setText(ms_to_time(position))
        self.position_slider.setSliderPosition(position)

    def change_metadata(self):
        artist = self.player.metaData(QMediaMetaData.ContributingArtist)
        title = self.player.metaData(QMediaMetaData.Title)
        image = self.player.metaData(QMediaMetaData.CoverArtImage)
        if artist:
            if type(artist) == list:
                artist = ', '.join(artist)
            self.artist_label.setText(artist)
        else:
            self.artist_label.setText('None')
        if title:
            self.title_label.setText(title)
        else:
            self.title_label.setText('None')
        if image:
            self.image_label.setPixmap(QPixmap.fromImage(image))
        else:
            self.image_label.setText('None')



    def open_dialog(self):
        track_directory = QFileDialog.getOpenFileName(self, 'Choose track', '',
                          'Music (*.flac *.ogg *.mp3 *.wav *.webm)')[0]
        if track_directory:
            if self.state != 0:
                if self.state == 1:
                    self.play_pause_button.setText('Play')
                self.stop_button.setEnabled(False)
            self.player.setMedia(
                             QMediaContent(QUrl.fromLocalFile(track_directory)))
            if not self.UI:
                self.artist_label.setEnabled(True)
                self.title_label.setEnabled(True)
                self.volume_slider.setEnabled(True)
                self.position_label.setEnabled(True)
                self.duration_label.setEnabled(True)
                self.position_slider.setEnabled(True)
                self.play_pause_button.setEnabled(True)
                self.UI = True

    def change_position_freeze(self):
        self.player.positionChanged.disconnect(self.position_changed)
        self.position_slider.sliderMoved.connect(self.change_position_label)

    def change_position_label(self, position):
        self.position_label.setText(ms_to_time(position))

    def change_position_unfreeze(self):
        self.player.setPosition(self.position_slider.sliderPosition())
        self.position_slider.sliderMoved.disconnect(self.change_position_label)
        self.player.positionChanged.connect(self.position_changed)

    def play_pause(self):
        if self.state == 1:
            self.player.pause()
            self.play_pause_button.setText('Play')
        else:
            if self.state == 0:
                self.stop_button.setEnabled(True)
            self.player.play()
            self.play_pause_button.setText('Pause')

    def stop(self):
        if self.state == 1:
            self.play_pause_button.setText('Play')
        self.player.stop()
        self.stop_button.setEnabled(False)



if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    application = QApplication(sys.argv)
    window = Visard()
    window.show()
    sys.exit(application.exec())