import cv2
from pydub import AudioSegment
import subprocess

class ImageFrames(cv2.VideoCapture):

    def __init__(self, video_path):

        super().__init__()
        # doc tu file: "filename", webcam: 0, 1...
        self.video_path = video_path
        # khoi tao
        self.video = cv2.VideoCapture(self.video_path)

    def GetFrame(self):
        ret, frame = self.video.read()
        if ret:
            return frame
        else:
            return None

    def ReleaseFrame(self):
        self.video.release()

    def GetVideo(self, num_frames, delay):
        video = []
        for i in range(num_frames):
            video.append(self.GetFrame())
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break
        self.ReleaseFrame()
        return video

class ExtractAudio:
    def __init__(self, video_path, audio_path):
        self.video_path = video_path
        self.audio_path = audio_path
    def ExportWav(self):
        video = AudioSegment.from_file(self.video_path)
        audio = self.audio_path
        video.export(audio, format="wav")

class AddText:
    def __init__(self, input_path, output_path, x_coor, y_coor, font_path, font_size, font_color, text):
        self.input_path = input_path
        self.output_path = output_path
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.font_size = font_size
        self.font_path = font_path
        self.font_color = font_color
        self.text = text
    # con thieu encode
    def AddText(self):
        command = "ffmpeg -i " + video_path + " -vf drawtext=fontfile=" + self.font_file + ":fontcolor=" + self.font_color + \
        ":fontsize=" + self.font_size + ':x=' + self.x_coor + ':y=' + self.y_coor + ':box=1' + \
        ':boxcolor=black' + ':boxborderw=1' + ":text=" + "'" + self.text + "' " + self.output_path
        subprocess.Popen(command, shell=True)
        return self.output_path
    def AddSub(self):
        # chua kip viet
        return

'''if __name__ == '__main__':
    # test extract
    video_path = "/Users/lamphung/Downloads/test.mp4"
    audio_path = "/Users/lamphung/Downloads/test.wav"
    audio = ExtractAudio(video_path, audio_path)
    audio.ExportWav()
    # test text
    # test sub


# opencv+pyqt : show_label hien thi video
camera = cv2.VideoCapture(fileName)
            while (camera.isOpened()):
                rv, frame = camera.read()
                if rv:
                    cv2.putText(frame, 'Hello World!', (50, 50), cv2.FONT_ITALIC, 0.8, 255)
                    cv2.imshow('', frame)
                    img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                    pix = QPixmap.fromImage(img)
                    self.show_label.setPixmap(pix)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            camera.release()'''




