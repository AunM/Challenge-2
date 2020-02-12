#run pip install fastapi uvicorn

from fastapi import FastAPI
app = FastAPI()


@app.get("/integer/{number}")
async def evaluate_integer(number:int):
 """
    this api is responsible to evaluate integer for 3 and 5.
    """
    if number % 3 == 0 and number % 5 == 0:
        return {'status_code':200, 'status':'success','result': 'PE'}
    elif number % 5 == 0:
        return {'status_code':200, 'status':'success','result': 'P'}
    elif number % 3 == 0:
        return {'status_code':200, 'status':'success','result': 'E'}
    else:
        return {'status_code':200, 'status':'success','result': number}