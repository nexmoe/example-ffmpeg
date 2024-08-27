import shutil
import subprocess
import uuid
from pathlib import Path

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse

GPU_ENABLE = True
app = FastAPI()


@app.get("/")
async def index():
    return FileResponse('index.html')


@app.get("/doc")
async def doc():
    return {
        "doc": "This is a ffmpeg api instance.",
        "endpoints": [
            {
                "path": "/video/to/mp4",
                "method": ["POST"],
                "params": {
                    "file": {
                        "type": "file",
                        "format": "video/*"
                    }
                }
            }
        ]
    }


@app.post("/video/to/mp4")
async def upload_file(file: UploadFile = File(...)):
    save_path = Path(f"uploaded_files/{file.filename}")
    save_path.parent.mkdir(parents=True, exist_ok=True)

    with save_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    unique_filename = f"{uuid.uuid4()}.mp4"
    output_path = save_path.parent / unique_filename

    if GPU_ENABLE:
        args = [
            "ffmpeg",
            "-hwaccel", "nvdec",
            "-i", str(save_path),
            "-c:v", "h264_nvenc",
            str(output_path)
        ]
    else:
        args = ["ffmpeg", "-i", str(save_path), str(output_path)]
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        error_msg = f"FFmpeg failed with return code: {e.returncode}\n"
        error_msg += f"Stdout: {e.stdout}\n"
        error_msg += f"Stderr: {e.stderr}\n"
        print(error_msg)
        raise HTTPException(status_code=500, detail="FFmpeg conversion failed!\n" + error_msg)

    return FileResponse(output_path, media_type="video/mp4", filename=unique_filename)
