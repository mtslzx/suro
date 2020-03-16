# 수로
### 트위치 구독자 전용 VOD 다운로더 "수로"
##### Twitch Leecher가 더이상 구독자 전용 VOD를 다운받지 못하게 되자 시작한 프로젝트


## 사용된 라이브러리
time , random , requests , os

## 어떻게 사용하나요?
### 1. 다운로드 받을 영상의 링크 확인
twitch.tv 접속 후 다운로드 받을 스트리머의 VOD를 시청하는 페이지로 이동  
개발자 도구를 켜고 Network 탭으로 이동  
영상을 끝나기 10초 전으로 이동 후 Network 탭에 있는 ???.ts의 ???을 확인  
???.ts 를 우클릭해서 copy address 
### 2. 영상 정보를 수로에 입력하기
수로를 켜고 아까 복사한 링크를 붙여넣고  
https://vod-secure.twitch.tv/539...34/chunked/1500.ts 에서 1500.ts 제거 후 입력  
아까 확인한 ???.ts 의 ???을 반복 구간에 입력
영상 제목을 원하는데로 입력
### 3. 기다리기
다운로드를 보고있다보면 영상을 합치고 프로그램이 종료될 것이다
### 4. 파일 정리하기
다운로드 후 남은 .ts 파일들을 제거해준다

## 변경점 
[b0.1]
최초 프로그램 기초 작성

[b0.2]
+ ###### File 접근 및 다운로드 기능

[b0.3]
+ ###### Url 구분 기능

[b0.4]
+ ###### 순차 다운로드 기능

[1.0]
정식 릴리즈
+ ###### 봇 감지 방지를 위한 슬립기능
+ ###### 다운로드 실패시 알림

[1.1]
Twitch Downloader 프로젝트 합병
+ ###### moviepy 기능 테스트

[1.2]
+ ###### FFMPEG 4.2.2 탑재
+ ###### FFMPEG로 영상파일 연결기능
- ###### 최적화 문제로 moviepy 제거

[1.3]
+ ###### 영상 파일 제목에 공백이 포함될 경우 작동이 멈추는 버그 임시 해결



## 도움을 받은 곳
1.	https://code.i-harness.com/ko/q/6e87e6
2.	https://www.daleseo.com/python-random/
3.	https://wikidocs.net/13#_16
4.	https://stackoverflow.com/questions/42901942/how-do-we-download-a-blob-url-video
5.	https://m.blog.naver.com/shino1025/221279112390  
등등.....

## 속성
파일명 : suro.py 
제작 시작일 : 2019년 12월 15일


