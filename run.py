from uvicorn import run

from app.api import app as application

if __name__ == "__main__":
    run("run:application", host="0.0.0.0", port=8000, workers=4) #nosec
