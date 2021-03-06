# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:07:25 2020

@author: Rashmi R
"""
#
import moviepy.editor
video=moviepy.editor.VideoFileClip('Lingashtakam by SP Balasubramaniam.mp4')
audio=video.audio
audio.write_audiofile('result.mp3')