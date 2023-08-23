from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import os
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()
port = int(os.getenv("PORT"))


@app.get("/get/transcript/{id}")
def get_transcript(id: str):
    res = {"query": id}
    results = YouTubeTranscriptApi.get_transcript(id)

    res["res"] = results
    return JSONResponse(content=res, headers={"Access-Control-Allow-Origin": "*"})


if __name__ == "__main__":
    uvicorn.run("main:app", port=port, host="0.0.0.0")

# python -m uvicorn test:app --reload
