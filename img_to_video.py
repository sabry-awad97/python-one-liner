# pip install moviepy

from moviepy.editor import ImageSequenceClip as imageSeq

imageSeq(["img1.png", "img2.png"], fps=1).write_videofile("vid.mp4")
