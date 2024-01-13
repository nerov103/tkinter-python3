from pytube import YouTube

ytlink = YouTube(input('enter the url of the video: '))
userInp = input("press(1) for video downloads (2) audio")

if userInp == "2":
    videores = input("video resoliction:")
    video = ytlink.streams.filter(res=videores).first()
    save_loc = input('enter the desticon of the video:')
    print("video start downloads...")
    video.download(save_loc)
    print("VIDEO DOWNLOADS SUCCESSFULLY")
if userInp == "1":
    auto = ytlink.streams.filter(only_audio=True).filter()
    save_l = input("enter the destination of the  audio:")
    print("AUDIO START DOWNLOADS...")
    video.download(save_l)
    print("AUDIO DOWNLOADS SUCCESSFULL")
    