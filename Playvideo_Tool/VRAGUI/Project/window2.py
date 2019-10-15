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

class VRAWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        # co the dung class qtdesigner: loadUi('PlayVideo',self)
        self.window_name = "Voice Recognition Application"
        self.setWindowTitle(self.window_name)
        self.setGeometry(0, 0, 450, 100)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Open video to start')

        '''self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)'''

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


        openAction.triggered.connect(self.openFile)
        exitAction.triggered.connect(self.exitCall)
        extractAction.triggered.connect(self.extractAudio)
        recogAction.triggered.connect(self.recogVoice)

        # tao layout de dat widget ben trong
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)

        layout = QVBoxLayout()
        layout.addLayout(controlLayout)

        # hien thi cac layout o giua, gom video, control layout, error..
        wid = QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(layout)


    # cac ham event
    def openFile(self):
        self.statusBar.showMessage('Choose a video file')
        self.filePath, _ = QFileDialog.getOpenFileName(self, "Open Video",QDir.homePath())
        fileName = ntpath.basename(self.filePath)
        if self.filePath:
            command2 = 'open ' + self.filePath
            subprocess.Popen(command2, shell=True)
            self.setWindowTitle(fileName + " - " + self.window_name)
            self.statusBar.showMessage('Source video')


    def exitCall(self):
        sys.exit(app.exec_())


    def extractAudio(self):
        if self.filePath:
            video_path = self.filePath
            fileName = ntpath.basename(self.filePath)
            audio_path = os.path.dirname(self.filePath) + '/extract_' + fileName + '.wav'
            if os.path.exists(audio_path):
                os.remove(audio_path)
            audio = Video.ExtractAudio(video_path, audio_path)
            audio.ExportWav()
            command2 = 'open ' + audio_path
            subprocess.Popen(command2, shell=True)
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
            command = 'ffmpeg -i ' + video_path + ' -i /Users/lamphung/sub.srt -i /Users/lamphung/Downloads/subc.srt -map 0 -map 1 ' \
                                                  '-map 2 -c copy -c:a copy -c:s mov_text -metadata:s:s:0 language=eng -metadata:s:s:1 language=ger ' + output_path
            addtext = subprocess.Popen(command, shell=True)
            addtext.wait()
            command2 = 'exit ' + self.filePath
            subprocess.Popen(command2, shell=True)
            command3 = 'open ' + output_path
            self.statusBar.showMessage('Recognited')
            subprocess.Popen(command3, shell=True)
            addtext.wait()


