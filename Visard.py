import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioOutput,\
                               QMediaMetaData
from PyQt5.QtCore import QUrl
from UI import Ui_Window


dialog = 'Выберите композицию'


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


class Window(QWidget, Ui_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.status = False

        self.player = QMediaPlayer()
        self.player.setNotifyInterval(100)
        self.open_button.clicked.connect(self.open_dialog)

        self.play_pause_button.clicked.connect(self.play_pause)
        self.stop_button.clicked.connect(self.stop)

        self.player.durationChanged.connect(self.track_duration)
        self.player.positionChanged.connect(self.track_position)

        self.player.mediaStatusChanged.connect(self.track_status)

        self.position_slider.sliderPressed.connect(
                                               self.change_track_position_block)
        self.position_slider.sliderReleased.connect(
                                             self.change_track_position_unblock)

        self.volume_slider.valueChanged.connect(self.player.setVolume)
        self.mute_button.clicked.connect(self.mute)

        self.playback_spinbox.valueChanged.connect(self.change_playback)

        self.player.metaDataChanged.connect(self.title)

    def play_pause(self):
        if self.status:
            self.play_pause_button.setText('Play')
            self.player.pause()
            self.status = False
        else:
            self.play_pause_button.setText('Pause')
            self.stop_button.setEnabled(True)
            self.player.play()
            self.status = True

    def stop(self):
        if self.status:
            self.play_pause_button.setText('Play')
        self.stop_button.setEnabled(False)
        self.player.stop()
        self.status = False

    def track_duration(self, duration):
        self.track_duration_label.setText(ms_to_time(duration))
        self.position_slider.setMaximum(duration)

    def track_position(self, position):
        self.track_position_label.setText(ms_to_time(position))
        self.position_slider.setValue(position)

    def change_track_position_block(self):
        self.player.positionChanged.disconnect(self.track_position)
        self.position_slider.valueChanged.connect(
                                               self.change_track_position_label)

    def change_track_position_label(self, value):
        self.track_position_label.setText(ms_to_time(value))

    def change_track_position_unblock(self):
        self.player.setPosition(self.position_slider.value())
        self.position_slider.valueChanged.disconnect(
                                               self.change_track_position_label)
        self.player.positionChanged.connect(self.track_position)

    def track_status(self, status):
        if status == 7:
            self.stop()
            self.player.setPosition(0)

    def change_playback(self, value):
        self.player.positionChanged.disconnect(self.track_position)
        position = self.player.position()
        self.player.stop()
        self.player.setPlaybackRate(value)
        self.player.play()
        self.player.setPosition(position)
        self.player.positionChanged.connect(self.track_position)

    def mute(self):
        if self.player.isMuted():
            self.player.setMuted(False)
            self.volume_slider.setEnabled(True)
            self.mute_button.setText('🔊')
        else:
            self.volume_slider.setEnabled(False)
            self.player.setMuted(True)
            self.mute_button.setText('🔈')

    def open_dialog(self):
        track = QFileDialog.getOpenFileName(
                 self, dialog, '', 'Music (*.flac *.ogg *.mp3 *.wav *.webm)')[0]
        if track:
            self.play_pause_button.setEnabled(True)
            self.position_slider.setEnabled(True)
            self.volume_slider.setEnabled(True)
            self.mute_button.setEnabled(True)
            self.playback_spinbox.setEnabled(True)
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(track)))
            self.stop()

    def title(self):
        self.title_label.setText(self.player.metaData(QMediaMetaData.Title))
        self.author_label.setText(self.player.metaData(
                                             QMediaMetaData.ContributingArtist))


start = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(start.exec())
