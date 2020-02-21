''' 기본적인 틀은 이렇다 함.
from moviepy.editor import *
firstclip = VideoFileClip('0.ts')
secondclip = VideoFileClip('1.ts')
finalrender = concatenate_videoclips([firstclip, secondclip])
finalrender.write_videofile('render.mp4', codec='libx264')


'''
'''
from moviepy.editor import *
loop = 0

if __name__ == '__main__':
    loop = int(input("마지막 영상 번호를 입력하세요(0 - n):"))
    print(str(loop) +'a')


for i in range(loop + 1):
    {
        print(i)
    }
from moviepy.editor import *
firstclip = VideoFileClip(['0.ts', '1.ts', '2,ts', '3.ts', '1500.ts'])
"secondclip = VideoFileClip('1.ts')"
finalrender = concatenate_videoclips(firstclip)
finalrender.write_videofile('render.mp4', codec='libx264')
'''
loop = 0
import os

if __name__ == '__main__':
    loop = int(input("마지막 영상 번호를 입력하세요(0 - n):"))
    print(str(loop) + ' 입력확인됨.')

from moviepy.editor import *


def close_clip(clip):
    try:
        clip.reader.close()
        '''if clip.audio != None:
            clip.audio.reader.close_proc()
            del clip.audio'''
        del clip
    except Exception as e:
        print("Error in close_clip() ", e)


clips = []
for def_image in range(loop + 1):
    video_item = VideoFileClip('%s.ts' % def_image)
    #print(video_item)
    video_item_duration = video_item.duration
    #print(video_item_duration)
    clips.append(video_item)
    "clips.append(ffmpeg_tools.ffmpeg_extract_subclip(str('%s.ts' % def_image), 0, int(video_item_duration)))"
    #print("a")
    close_clip(video_item)
    #print("b")
    #print(clips)
    print(def_image + "번째 영상 처리중.")

print("[알림] 영상불러오기 성공")
final_render = concatenate_videoclips(clips)
print("[알림] 영상 컴포지팅 성공")
final_render.write_videofile('final_render.mp4', codec='libx264')
print("[완료]")
os.system("pasue")
'''      
# #Append the outro_clip to the end
clips.append(VideoFileClip('Logo_Intro_w_Stinger_Large.mp4',target_resolution = (h,w),audio=True))
slided_clips = [CompositeVideoClip([clip.fx( transfx.crossfadein, transition_seconds)]) for clip in clips]
#added 'method = compose' NEED TO TEST - supposedly removes the weird glitches.
c = concatenate_videoclips(slided_clips, method = 'compose')
c.write_videofile('F:/Extended_Play/%s_Extended_Play_vid.mp4' % letter,fps=23.98)
'''
