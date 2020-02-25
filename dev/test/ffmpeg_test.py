import os
loop = 0

if __name__ == '__main__':
    mv_name = str(input("영상 제목을 입력해주세요:"))
    loop = int(input("마지막 영상 번호를 입력하세요(0 - n):"))
    print(str(loop) + ' 입력확인됨.')

dl_list = open('download_list.txt', 'w')  # 텍스트 파일 생성

for i in range(loop + 1):
    dl_list.write("file '%s.ts'\n"% i)  # file '0.ts' 형식으로 저장

dl_list.close()  # 파일 저장 후 닫기


# 현재 경로 저장
os.system('cd {}'.format(os.getcwd()))
output = os.popen('dir').read()
print(output)

# FFMPEG / .ts 파일 합치기
os.system(R'bin\ffmpeg -f concat -i download_list.txt -c copy %s.ts' % mv_name)  # \f 가 이스케이프로 치환되는것을 막기위해 R 을 붙여 Raw 표현

# FFMPEG / .ts To .mp4
os.system(R'bin\ffmpeg -i %s.ts -acodec copy -vcodec copy %s.mp4' % (mv_name, mv_name))  # ffmpeg를 따로 설치하지않고 binary 불러오기
