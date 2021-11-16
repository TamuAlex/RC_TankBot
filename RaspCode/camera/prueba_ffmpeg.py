import subprocess
import os,signal
import cv2
rtmp_url = "rtmp://tankrobotmanagement-tankrobotmanagement-euno.channel.media.azure.net:1935/live/3f37b2cd29d3446f9916d7a2f91c6021"
try: 
    # In my mac webcamera is 0, also you can set a video file name instead, for example "/home/user/demo.mp4"
    cap = cv2.VideoCapture(1)

    # gather video info to ffmpeg
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(fps)

    # command and params for ffmpeg
    command = ['ffmpeg', "-hide_banner",
               '-y',
               '-f', 'rawvideo',
               '-vcodec', 'rawvideo',
               '-pix_fmt', 'bgr24',
               '-s', "{}x{}".format(width, height),
               '-r', str(fps),
               '-i', '-',
               '-c:v', 'libx264',
               '-pix_fmt', 'yuv420p',
               '-preset', 'ultrafast',
               '-f', 'flv',
               rtmp_url]

    # using subprocess and pipe to fetch frame data
    p = subprocess.Popen(command, stdin=subprocess.PIPE)


    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("frame read failed")
            break
        cv2.imshow("culo",frame)
        # write to pipe
        p.stdin.write(frame.tobytes())
                      
except:
    print("Tus muertos")
    #print (e)

finally:
    cap.release()
    cv2.destroyAllWindows()
    #os.killpg(os.getpgid(p.pid), signal.SIGTERM)
