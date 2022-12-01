# pip install pytube

import pytube

pytube.YouTube(input("Enter the URL: ")).streams.first().download()
