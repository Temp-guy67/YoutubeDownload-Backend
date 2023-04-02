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
    return {"message": "Working"}


# sample link : http://127.0.0.1:8000/youtubedownload?link=https://www.youtube.com/watch?v=dQw4w9WgXcQ


@app.get("/youtubedownload")
async def youtube_download(request: Request, link: str):

    yt = YouTube(link)
    print("\n linkreceived : " + link , " Time :- ", datetime.datetime.now())
    video = []
    audio = []
    videoStreams = yt.streams.filter(progressive=True)
    audioStreams  = yt.streams.filter(only_audio=True)

    for e in videoStreams :
        video.append(e.url)

    for e in audioStreams :
        audio.append(e.url)

    embed_link = link.replace("watch?v=","embed/")
    title = yt.title
    thumb = yt.thumbnail_url

    data = {"video": video ,"audio": audio, "embed" : embed_link ,"pic":thumb, "title": title}
    # data = { "embed" : embed_link ,"pic":thumb, "title": title, "audio": audio}

    # return {"message": context} 
    return JSONResponse(content=data)