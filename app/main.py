from fastapi import FastAPI, HTTPException
from generate_calendar import generate_calendar
from fastapi.encoders import jsonable_encoder
from datetime import datetime

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/calendar")
async def read_item(start_date, end_date):
    # todo - encrypt with Let's Encrypt
    if (start_date is None or start_date == "") and (end_date is None or end_date == ""):
        raise HTTPException(status_code=400, detail="Missing start and end date")

    if start_date is None or start_date == "":
        raise HTTPException(status_code=400, detail="Missing start date")

    if end_date is None or end_date == "":
        raise HTTPException(status_code=400, detail="Missing end date")

    try:
        start_date = datetime.strptime(start_date, "%Y%m%d")
        end_date = datetime.strptime(end_date, "%Y%m%d")
    except:
        raise HTTPException(status_code=400, detail="Invalid date format. Please use format YYYYMMDD.")

    if start_date > end_date:
        raise HTTPException(status_code=400, detail="Please use an end date equal to or after the start date.")
    return jsonable_encoder(generate_calendar(start_date, end_date))