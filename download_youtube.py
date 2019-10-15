from pytube import YouTube



list_link = ["https://www.youtube.com/watch?v=gHeNTecQpX4&list=PLP2uWpYxMAPGaSEOUMOT5lRUe_Y3NQ8oR&index=80",
			 "https://www.youtube.com/watch?v=P_NZdVCTb78&list=PLP2uWpYxMAPGaSEOUMOT5lRUe_Y3NQ8oR&index=83"]
i = 1
for link in list_link:
	yt = YouTube(link)
	stream = yt.streams.first()
	stream.download()

	print ('complete '+ str(i))
	i = i+1

print('save in the same directory of compile')
print('----done-----')
