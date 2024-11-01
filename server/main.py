from fastapi import FastAPI
from pydantic import BaseModel
from glob import glob
from random import randint
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# allow specific origin points to this app
origins = [
    "http://localhost:5173",
]

# add CORS middleware for the above origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# data model
class Query(BaseModel):
    query: str
    filename: str

@app.post("/query")
async def read_query(query:Query):
    
    mypath = './data/'
    # get all files recursively
    all_files = glob(mypath + '/**', recursive=True)

    request = query.model_dump()
    query = request['query']
    filename = request['filename']

    for file in all_files:
        filen = file.split('/')[-1].split('.')[0].lower()

        ## add handling for windows-based paths
        if os.name == 'nt':
            filen = file.split('\\')[-1].split('.')[0].lower()
            
        if filen == filename.lower():
            with open(file, 'r', encoding="utf8") as f:

                data = f.readlines()
                # get random 10 lines from the file
                random_lines = [randint(1, len(data)-1) for i in range(10)]
                answer = ''.join([(data[i]) for i in random_lines])
            return {"result": answer}
        
    return {"result": "Cannot find file!"}