from moviepy.editor import VideoFileClip

video = "test2.mp4"

video_source = VideoFileClip(video)
voice = video_source.audio
need_voice_video = VideoFileClip("output.mp4")
output_video = need_voice_video.set_audio(voice)
output_video.write_videofile("output.mp4")
