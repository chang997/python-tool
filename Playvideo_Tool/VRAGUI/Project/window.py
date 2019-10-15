import sys
from PyQt5.QtCore import Qt, QDir, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QAction, QSlider, QPushButton, \
    QStyle, QFileDialog, QStatusBar
from Lam_modul import Video
import subprocess
import ntpath
import os

class VRAWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # co the dung class qtdesigner: loadUi('PlayVideo',self)
        self.window_name = "Voice Recognition Application"
        self.setWindowTitle(self.window_name)
        #self.setFixedSize(0, 0)

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 10)
        self.positionSlider.setEnabled(False)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Open video to start')

        openAction = QAction(QIcon('open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open a Video file')

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')

        saveAction = QAction(QIcon('save.png'), '&Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save a file')

        extractAction = QAction(QIcon('extract.png'), '&Extract Audio', self)
        extractAction.setShortcut('Ctrl+E')
        extractAction.setStatusTip('Extract audio from video')

        recogAction = QAction(QIcon('recog.png'), '&Recognition', self)
        recogAction.setShortcut('Ctrl+R')
        recogAction.setStatusTip('Voice Recognition')

        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)

        fileMenu1 = menuBar.addMenu(' &File')
        fileMenu1.addAction(openAction)
        fileMenu1.addAction(exitAction)

        fileMenu2 = menuBar.addMenu(' &Run')
        fileMenu2.addAction(extractAction)
        fileMenu2.addAction(recogAction)

        # tao cac event voi cac doi tuong da khoi tao, gan voi cac ham o sau
        self.playButton.clicked.connect(self.play)

        #self.runButton.clicked.connect(self.run)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        openAction.triggered.connect(self.openFile)
        exitAction.triggered.connect(self.exitCall)
        extractAction.triggered.connect(self.extractAudio)
        recogAction.triggered.connect(self.recogVoice)

        # tao widget phat video
        self.videoWidget = QVideoWidget()
        self.videoWidget.setAspectRatioMode(2)
        #self.videoWidget.setFixedSize(960, 540)


        # tao layout de dat widget ben trong
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(self.videoWidget)
        layout.addLayout(controlLayout)

        # hien thi cac layout o giua, gom video, control layout, error..
        wid = QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(layout)

        # lay cac ham xu ly media trong class nay
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        # show video
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        # trang thai
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        # silder = time
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

        self.filePath = ''

    # cac ham event
    def openFile(self):
        self.statusBar.showMessage('Choose a video file')
        self.filePath, _ = QFileDialog.getOpenFileName(self, "Open Video",QDir.homePath())
        fileName = ntpath.basename(self.filePath)
        if self.filePath:
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.filePath)))
            self.playButton.setEnabled(True)
            self.mediaPlayer.play()
            self.setWindowTitle(fileName + " - " + self.window_name)
            self.statusBar.showMessage('Source video')
            self.positionSlider.setEnabled(True)

    def exitCall(self):
        sys.exit(app.exec_())


    def extractAudio(self):
        if self.filePath:
            self.mediaPlayer.pause()
            video_path = self.filePath
            fileName = ntpath.basename(self.filePath)
            audio_path = os.path.dirname(self.filePath) + '/extract_' + fileName + '.wav'
            if os.path.exists(audio_path):
                os.remove(audio_path)
            audio = Video.ExtractAudio(video_path, audio_path)
            audio.ExportWav()
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(audio_path)))
            self.playButton.setEnabled(True)
            self.mediaPlayer.play()
            self.statusBar.showMessage('Wav extracted')

    def recogVoice(self):
        if self.filePath:
            #self.mediaPlayer.pause()
            self.statusBar.showMessage('Wait, Recogniting!')
            video_path = self.filePath
            fileName = ntpath.basename(self.filePath)
            output_path = os.path.dirname(self.filePath) + '/recog_' + fileName
            #sub_path = '/Users/lamphung/Downloads/sub.srt.rtfd'
            if os.path.exists(output_path):
                os.remove(output_path)

            '''font_file = "/Users/lamphung/Downloads/ArialBold.ttf"
            font_color = "white"
            font_size = "50"
            x_coor = '570'
            y_coor = '650'
            text = 'Frame: ' + '%{frame_num}'
            command = "ffmpeg -i " + video_path + " -vf drawtext=fontfile=" + font_file + ":fontcolor=" + font_color + \
                      ":fontsize=" + font_size + ':x=' + x_coor + ':y=' + y_coor + ':box=1' + \
            ':boxcolor=black' + ':boxborderw=1' + ":text=" + "'" + text + "' " + output_path
            print(command)'''
            # thay duong dan cua file sub
            #command = 'ffmpeg -i ' + video_path + ' -vf subtitles=/Users/lamphung/sub.srt ' + output_path
            #command = 'ffmpeg -i ' + video_path + ' -i /Users/lamphung/sub.srt -c:s mov_text -c:v copy -c:a copy ' + output_path
            command = 'ffmpeg -i ' + video_path + ' -i subvie.srt -i subeng.srt -map 0 -map 1 ' \
                                                  '-map 2 -c copy -c:a copy -c:s mov_text -metadata:s:s:0 language=vie -metadata:s:s:1 language=eng ' + output_path
            addtext = subprocess.Popen(command, shell=True)
            addtext.wait()
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(output_path)))
            self.playButton.setEnabled(True)
            self.mediaPlayer.play()
            self.statusBar.showMessage('Recognited')
            command2 = 'open ' + output_path
            subprocess.Popen(command2, shell=True)
            # khi chay cung model: dau tien tao mot file sub dinh dang srt rong,
            # moi khi model nhan dang duoc va tra ve time, text thi add no vao file theo dung cau truc

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)




