from fastapi import APIRouter, File
from fastapi.responses import FileResponse
from sclib import SoundcloudAPI, Track

router = APIRouter(prefix="/scdl", tags=['dl'])

@router.get("/download/", response_class=FileResponse)
def dl(link: str):
    api = SoundcloudAPI()
    track = api.resolve(link)
    assert type(track) is Track
    filename = f"files/{track.artist} - {track.title}.mp3"
    with open(filename, "wb+") as file:
        track.write_mp3_to(file)

    return filename
