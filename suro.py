'''
파일명 : suro.py
제작 시작일 : 2019년 12월 15일
- 도움을 받은 곳 -
https://code.i-harness.com/ko/q/6e87e6
https://www.daleseo.com/python-random/
https://wikidocs.net/13#_16
https://stackoverflow.com/questions/42901942/how-do-we-download-a-blob-url-video
https://m.blog.naver.com/shino1025/221279112390

- 사용된 라이브러리 -
time , random , requests , os


= 트위치 구독자 전용 VOD 다운로더 b0.1 =


- 변경점 -
[b0.1]
최초 프로그램 기초 작성

[b0.2]
+ File 접근 및 다운로드 기능

[b0.3]
+ Url 구분 기능

[b0.4]
+ 순차 다운로드 기능

[1.0]
정식 릴리즈
+ 봇 감지 방지를 위한 슬립기능
+ 다운로드 실패시 알림

[1.1]
Twitch Downloader 프로젝트 합병

[1.1.1]
·moviepy 기능 테스트

[1.2]
+ FFMPEG 4.2.2 탑재
+ FFMPEG로 영상파일 연결기능
- moviepy 제거

[1.3]
+ 영상 파일 이름에 공백이 들어가면 작동이 멈추는 버그 임시 해결


'''

from requests import get
from urllib import request
import random as r
import time as t
import os


# 링크에서 파일이름 구분해서 다운로드
def download(url: object, file_name: object = None) -> object:
    if not file_name:
        file_name = url.split('/')[-1]

    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)


# 파일 이름 구분 안하고 다운로드
def non_download(url, file_name):
    with open(file_name, "wb") as file:  # open in binary mode
        response = get(url)  # get request
        file.write(response.content)  # write to file


# 파일 다운로드 실패시 확인용 / 403 Fobbiden - 봇 감지에 걸림
def check(url):
    with request.urlopen(url) as r:
        return r.read()


# 시작 옵션
def ready():
    print('''[ 수로 v1.3 ]
    (중요) Requests 라이브러리의 설치가 필요합니다.
    
    (알림)  예시 https://vod-secure.twitch.tv/00acc6386121b4a37af5_mister903_36414312512_1344611539/chunked/1500.ts
    에서 1500.ts 를 제외한 다음 링크를 입력해주세요. 
    
    (알림) 아직까지 완벽하지 않습니다. 이후 추가 예정인 기능입니다.
     영상의 최종길이를 트위치에서 확인하여 반복구간으로 입력해주세요.
    
    (알림) 이후 개선 예정
     파일의 저장경로 지정이 불가능합니다. 현재 폴더에 저장됩니다.
     파일 렌더 후 다운로드 받은 파일을 직접 제거해야 합니다.
    
    ''')


# 파일 주소 카운트 업
def count(url, loop):
    print("현재 반복 구간은:", loop, "입니다.")
    c_url = url + str(loop) + '.ts'
    print("경로는: ", c_url, "입니다.")
    return c_url


# 메인 함수
if __name__ == '__main__':
    ready()
    url = input("VOD 주소를 입력하세요:")  # F12에서 확인된 링크 에서 ???.ts 제거하고 입력
    loop = int(input("반복할 범위를 입력하세요(0 - n):"))  # F12에서 확인된 ???.ts 의 끝번호 입력
    mv_name = str(input("영상 제목을 입력해주세요:"))  # 저장할 영상 파일 제목 지정
    mv_name = mv_name.replace(' ', '_')  # 영상 제목의 공백을 _ 으로 변환
    # check(url)
    for i in range(loop + 1):
        c_url = count(url, i)
        download(c_url)
        wait = r.uniform(0.005, 5)
        print(wait, "만큼 잠듭니다.....")
        t.sleep(wait)
    # 영상 모듈
    dl_list = open('download_list.txt', 'w')  # 영상 리스트 텍스트 파일 생성
    for i in range(loop + 1):
        dl_list.write("file '%s.ts'\n" % i)  # file '0.ts' 형식으로 저장
    dl_list.close()  # 파일 저장 후 닫기
    # FFMPEG / .ts 파일 합치기
    os.system(R'bin\ffmpeg -f concat -i download_list.txt -c copy %s.ts' % mv_name)  # \f 가 이스케이프로 치환되는것을 막기위해 R 을 붙여 Raw 표현
    # FFMPEG / .ts To .mp4
    os.system(R'bin\ffmpeg -i %s.ts -acodec copy -vcodec copy %s.mp4' % (mv_name, mv_name))  # ffmpeg를 따로 설치하지않고 binary 불러오기