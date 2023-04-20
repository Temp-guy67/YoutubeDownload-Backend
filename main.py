from fastapi import FastAPI, Request
from pytube import YouTube
import datetime
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Create a FastAPI instance
app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://192.168.0.110:3000",
    "http://172.24.125.101:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    version = "version : " + "3"; 
    return {"message": version}

# sample link : http://127.0.0.1:8000/youtubedownload?link=https://www.youtube.com/watch?v=dQw4w9WgXcQ

@app.get("/youtubedownload")
async def youtube_download(request: Request, link: str):

    yt = YouTube(link)
    video = []
    audio = []
    videoStreams = yt.streams.filter(progressive=True,file_extension='mp4')
    audioStreams  = yt.streams.filter(only_audio=True)

    for e in videoStreams :
        temp = {"resuloution": e.resolution , "fps" : e.fps , "link" : e.url , "size" : e.filesize_mb} 
        video.append(temp)

    for e in audioStreams :
        temp = { "link" : e.url, "bitrate" : e.abr , "size" : e.filesize_mb} 
        audio.append(temp)

    embed_link = link.replace("watch?v=","embed/")
    title = yt.title
    thumb = yt.thumbnail_url

    data = {"video": video ,"audio": audio, "embed" : embed_link ,"pic":thumb, "title": title}
    response = JSONResponse(content=data)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response