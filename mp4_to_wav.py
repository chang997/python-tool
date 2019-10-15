

import moviepy.editor as mp
import os

folder = []


def mp4_wav(folder, save_folder):
	i = 1
	for f_name in os.listdir(folder):
		f = os.path.join(folder, f_name)

		clip = mp.VideoFileClip(f)
		duration = clip.duration

		start = 0
		end = start + 300 # vì praat đọc đc đoạn tối đa 7 phút nên ta để đoạn dài 5 phút
		while start < duration:
			if end > duration:
				end = duration
			if (end - start) <=2:
				break
			subclip = clip.subclip(start,end)
			subclip.audio.write_audiofile(os.path.join(save_folder, str(i)+'.wav'))

			start = end
			end = start + 300
			i = i + 1
			print(end)




if __name__ == '__main__':
	folder = r"C:/Users/Admin/Desktop/duc_chien"
	save_folder = r"C:/Users/Admin/Desktop/wav_duc_chien"
	mp4_wav(folder, save_folder)