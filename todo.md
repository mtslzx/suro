빨리 지워지기 전에 다운로드 받으려면 당장 만들어야 해ㅋㅋㅋ


기본적인 프로그램 작성완료.
다운로드 only

ffmpeg 라이브러리 추가예정. +++

GUI 추가예정. 

빨리 지워지기 전에 다운로드 받으려면 당장 만들어야 해ㅋㅋㅋ

---

+ ## 아이디어
    + #### 지금 moviepy lib test.py 실행시 약 1300개 정도되는 영상을 로딩시 약 25GB 정도의 RAM을 차지하게 된다.
    + #### 아직 제대로 확인하지는 못했지만 Moviepy가 인코딩을 시작한 후 컴퓨터가 못버티는건지, 프로그램의 문제인지 1시간 짜리영상이 6분 가량만 재생이 가능하다. (이 경우 영상 1개 당 용량이 5MB 였음에도 불구하고 최종영상이 120MB 정도이다.)
    + ##### 그러므로 다른 방법을 찾을 필요성이 있다.
        1. _피보나치 수열(?) 방식._
            + 1000개의 영상이 있다고 치자. 이 영상 전부를 처리하려면 매우 많은 자원을 필요로 한다.
            + 그러므로 영상을 100개 정도로 나누어 처리하는것이다. 0번 부터 99번. 100번 부터 199번. 200번 부터 ... 999번. 1000번.
            + 그러면 **영상이 10개가 될것이다**. 이 영상은 용량이 크지만 1000개를 한번에 잇는것 보다는 쉬운 작업일것이고. 즉, **자원의 소모도 낮다.**
        2. _다른 프로그램을 이용한다._
            + 정말 내가 해결할 수 없다면 이 방법밖에는 답이 없다.
            + 프로그래밍적으로는 쉽겠지만, 절차가 늘어나게 될 것이다.
            + 최종목표인 자동화에도 문제가 생길것이다. 
            
---
출처 : https://superuser.com/questions/692990/use-ffmpeg-copy-codec-to-combine-ts-files-into-a-single-mp4

Using copy or cat to combine the files like szatmary's current top answer might leave you with a file that plays far past the limit and can't seek along with playback issues.

Instead, to combine these files properly use ffmpeg as instructed in https://trac.ffmpeg.org/wiki/Concatenate. (Install ffmpeg here if you don't already have it https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg.)

If you're too lazy to read my first link, you basically have to create a .txt file listing all the files you want to combine like so (which my first link gives instructions on how to do easily) in the folder where you're doing the concatenation:

`file '/path/to/file1'
file '/path/to/file2'
file '/path/to/file3'`

Here's a copy paste from my first link on one way to create a text file if you have Windows on commandline for instance but obviously you can make the file manually or however you want:

`(for %i in (*.ts) do @echo file '%i') > mylist.txt`

Double check that your .txt file looks good and is formatted correctly!

After this, on commandline run:

`
ffmpeg -f concat -i mylist.txt -c copy all.ts
where 'mylist.txt' is the .txt file you just made.
`

Check if the resultant file plays video correctly. From here, you can transmux to mp4 as usual if you like:

`
ffmpeg -i all.ts -acodec copy -vcodec copy all.mp4
`

+ 해결방법을 찾은 것 같다. 
+ Moviepy 라이브러리는 너무 무겁고 RAM을 존나게 쳐먹기 때문에 cmd에서 FFMPEG를 직접 불러와서 명령어를 입력하는게 훨씬 빠르고 자원도 적게든다.
