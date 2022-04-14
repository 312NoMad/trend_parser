import uvicorn
from fastapi import FastAPI

from modules.parser import get_articles

app = FastAPI()

@app.get('/')
def root():
    response = get_articles()
    if response:
        return {'message': response}
    return {'message': 'No trending news'}

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")
